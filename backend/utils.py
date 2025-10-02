# General helper functions (logging, unit conversions, safe loaders).

# backend/utils.py
import logging
import math

# Setup logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

def log(msg: str):
    """Simple logging helper"""
    logging.info(msg)

# ---------------- Conversions ----------------
def joules_to_megatons(energy_joules: float) -> float:
    """Convert Joules → Megatons TNT"""
    return energy_joules / 4.184e15

def megatons_to_joules(megatons: float) -> float:
    """Convert Megatons TNT → Joules"""
    return megatons * 4.184e15

def deg_to_rad(deg: float) -> float:
    """Degrees → Radians"""
    return math.radians(deg)

def rad_to_deg(rad: float) -> float:
    """Radians → Degrees"""
    return math.degrees(rad)

