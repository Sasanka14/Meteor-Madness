# Define data models (schemas) for Asteroid, Impact Results, Mitigation Results.
# Using Pydantic (built into FastAPI).

# backend/models.py
from pydantic import BaseModel
from typing import Optional

class Asteroid(BaseModel):
    id: str
    name: str
    diameter_m: float
    velocity_mps: float
    miss_distance_km: float
    close_approach_date: str

class ImpactResult(BaseModel):
    diameter_m: float
    velocity_mps: float
    kinetic_energy_J: float
    energy_megatons_TNT: float
    crater_diameter_km: float
    seismic_magnitude: float
    tsunami_height_m: Optional[float]

class OrbitPosition(BaseModel):
    x: float
    y: float
    r: float

class MitigationResult(BaseModel):
    old_velocity: float
    new_velocity: float
    strategy: str
