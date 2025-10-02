# backend/app.py
from fastapi import FastAPI, Query
from backend.api import nasa_client, usgs_client, impact_calc, orbit_sim, mitigation
from .models import Asteroid, ImpactResult, OrbitPosition, MitigationResult
from .utils import log, deg_to_rad

app = FastAPI(
    title="Meteor Madness API",
    description="Asteroid Impact Simulation and Mitigation API",
    version="1.1.0",
)

# ---------------- NASA API ----------------
@app.get("/nasa/neo", response_model=dict)
def get_neo_feed(start_date: str, end_date: str):
    """Fetch Near-Earth Object (NEO) data from NASA API"""
    log(f"Fetching NEO feed from {start_date} to {end_date}")
    return nasa_client.fetch_neo_feed(start_date, end_date)

@app.get("/nasa/neo/{neo_id}", response_model=dict)
def get_neo_details(neo_id: str):
    """Fetch NEO details by ID"""
    log(f"Fetching NEO details for {neo_id}")
    return nasa_client.fetch_neo_by_id(neo_id)

# ---------------- USGS DATA ----------------
@app.get("/usgs/topography", response_model=list[dict])
def get_topography():
    """Load USGS topography dataset"""
    log("Loading USGS topography")
    return usgs_client.load_topography().to_dict(orient="records")

@app.get("/usgs/tsunami", response_model=dict)
def get_tsunami_zones():
    """Load USGS tsunami zones dataset"""
    log("Loading USGS tsunami zones")
    return usgs_client.load_tsunami_zones()

# ---------------- IMPACT CALCULATIONS ----------------
@app.get("/simulate/impact", response_model=ImpactResult)
def simulate_impact(
    diameter_m: float = Query(..., description="Asteroid diameter in meters"),
    velocity_mps: float = Query(..., description="Asteroid velocity in m/s"),
    distance_km: float = Query(500.0, description="Distance from coast for tsunami calc"),
):
    """Simulate asteroid impact (KE, crater, seismic, tsunami)"""
    log(f"Simulating impact for d={diameter_m} m, v={velocity_mps} m/s")
    ke = impact_calc.kinetic_energy(diameter_m, velocity_mps)
    megatons = impact_calc.energy_in_megatons(ke)
    crater = impact_calc.crater_size(megatons)
    seismic = impact_calc.seismic_magnitude(megatons)
    tsunami = impact_calc.tsunami_height(distance_km, megatons)

    return ImpactResult(
        diameter_m=diameter_m,
        velocity_mps=velocity_mps,
        kinetic_energy_J=ke,
        energy_megatons_TNT=megatons,
        crater_diameter_km=crater,
        seismic_magnitude=seismic,
        tsunami_height_m=tsunami,
    )

# ---------------- ORBIT SIMULATION ----------------
@app.get("/simulate/orbit", response_model=OrbitPosition)
def simulate_orbit(
    semi_major_axis_m: float = Query(..., description="Semi-major axis in meters"),
    eccentricity: float = Query(..., description="Orbital eccentricity"),
    true_anomaly_deg: float = Query(..., description="True anomaly in degrees"),
):
    """Compute orbital position using Kepler's law"""
    log(f"Simulating orbit: a={semi_major_axis_m}, e={eccentricity}, anomaly={true_anomaly_deg}")
    result = orbit_sim.kepler_position(
        semi_major_axis_m,
        eccentricity,
        deg_to_rad(true_anomaly_deg),
    )
    return OrbitPosition(**result)

# ---------------- MITIGATION STRATEGIES ----------------
@app.get("/mitigation/kinetic", response_model=MitigationResult)
def apply_kinetic_impactor(
    delta_v: float = Query(..., description="Velocity change in m/s"),
    asteroid_velocity: float = Query(..., description="Initial asteroid velocity in m/s"),
):
    """Apply kinetic impactor strategy"""
    log(f"Applying kinetic impactor: Δv={delta_v}, v={asteroid_velocity}")
    result = mitigation.kinetic_impactor(delta_v, asteroid_velocity)
    return MitigationResult(
        old_velocity=result["old_velocity"],
        new_velocity=result["new_velocity"],
        strategy="kinetic_impactor",
    )

@app.get("/mitigation/gravity", response_model=MitigationResult)
def apply_gravity_tractor(
    duration_days: float = Query(..., description="Duration of operation in days"),
    force_newton: float = Query(..., description="Force applied in Newtons"),
    mass_kg: float = Query(..., description="Asteroid mass in kg"),
    asteroid_velocity: float = Query(..., description="Initial asteroid velocity in m/s"),
):
    """Apply gravity tractor strategy"""
    log(f"Applying gravity tractor: F={force_newton}, t={duration_days} days, m={mass_kg}, v={asteroid_velocity}")
    result = mitigation.gravity_tractor(duration_days, force_newton, mass_kg, asteroid_velocity)
    return MitigationResult(
        old_velocity=result["old_velocity"],
        new_velocity=result["new_velocity"],
        strategy="gravity_tractor",
    )
