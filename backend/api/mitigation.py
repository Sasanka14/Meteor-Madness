# Mitigation strategies (gravity tractor, kinetic impactor).

# backend/api/mitigation.py
def kinetic_impactor(delta_v: float, asteroid_velocity: float):
    """Apply velocity change to asteroid using kinetic impactor"""
    new_velocity = asteroid_velocity + delta_v
    return {"old_velocity": asteroid_velocity, "new_velocity": new_velocity}

def gravity_tractor(duration_days: float, force_newton: float, mass_kg: float, asteroid_velocity: float):
    """Deflect asteroid slowly with gravity tractor"""
    delta_v = (force_newton * duration_days * 86400) / mass_kg
    return {"old_velocity": asteroid_velocity, "new_velocity": asteroid_velocity + delta_v}
