# Orbital mechanics (Keplerian elements).

# backend/api/orbit_sim.py
import math

MU_SUN = 1.327e20  # Gravitational parameter of Sun (m^3/s^2)

def kepler_position(semi_major_axis_m, eccentricity, true_anomaly_rad):
    """Return orbital position in Cartesian coords (simplified 2D)"""
    r = semi_major_axis_m * (1 - eccentricity**2) / (1 + eccentricity * math.cos(true_anomaly_rad))
    x = r * math.cos(true_anomaly_rad)
    y = r * math.sin(true_anomaly_rad)
    return {"x": x, "y": y, "r": r}
