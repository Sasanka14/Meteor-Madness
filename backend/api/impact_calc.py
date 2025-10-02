# Physics formulas: KE, crater scaling, seismic, tsunami.

# backend/api/impact_calc.py
import math

DENSITY = 3000  # kg/m^3 (avg asteroid density)

def kinetic_energy(diameter_m: float, velocity_mps: float):
    """Compute kinetic energy in Joules"""
    radius = diameter_m / 2
    volume = (4/3) * math.pi * radius**3
    mass = volume * DENSITY
    return 0.5 * mass * velocity_mps**2

def energy_in_megatons(energy_joules: float):
    """Convert Joules → Megatons TNT"""
    joules_per_megaton = 4.184e15
    return energy_joules / joules_per_megaton

def crater_size(energy_megatons: float):
    """Estimate crater size from impact energy"""
    # Simplified scaling law: diameter ≈ k * E^0.33
    k = 1.161  # empirical constant
    return k * (energy_megatons ** (1/3))

def seismic_magnitude(energy_megatons: float):
    """Estimate seismic magnitude (Richter scale)"""
    return 0.67 * math.log10(energy_megatons * 4.184e15) - 5.87

def tsunami_height(distance_km: float, energy_megatons: float):
    """Rough estimate of tsunami height at a distance"""
    return (energy_megatons ** 0.25) / (distance_km ** 0.5)

