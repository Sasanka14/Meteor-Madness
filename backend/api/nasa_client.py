# Fetch asteroid data from NASA NEO API.

# backend/api/nasa_client.py
import os
import requests

NASA_API_KEY = os.getenv("NASA_API_KEY", "DEMO_KEY")
BASE_URL = "https://api.nasa.gov/neo/rest/v1"

def fetch_neo_feed(start_date: str, end_date: str):
    """Fetch asteroid data between dates from NASA NEO API"""
    url = f"{BASE_URL}/feed"
    params = {"start_date": start_date, "end_date": end_date, "api_key": NASA_API_KEY}
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    return resp.json()

def fetch_neo_by_id(neo_id: str):
    """Fetch details for a specific asteroid by ID"""
    url = f"{BASE_URL}/neo/{neo_id}"
    params = {"api_key": NASA_API_KEY}
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    return resp.json()
