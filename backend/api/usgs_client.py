# Fetch USGS datasets 

# backend/api/usgs_client.py
import pandas as pd

def load_topography(file_path="data/USGC.csv"):
    """Load topography data from USGC dataset and Load tsunami zones dataset"""
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        return pd.DataFrame({"lat": [], "lon": [], "elevation": []})
