Meteor-Madness/
│
│── backend/                         # Python FastAPI backend
│   │── __init__.py                  # Marks backend as a package
│   │
│   │── api/                         # API modules
│   │   │── __init__.py              # Marks api as a sub-package
│   │   ├── nasa_client.py           # Fetch asteroid data from NASA NEO API
│   │   ├── usgs_client.py           # Fetch topography, seismic, tsunami data
│   │   ├── impact_calc.py           # Physics formulas: KE, crater scaling, seismic, tsunami
│   │   ├── orbit_sim.py             # Orbital mechanics (Kepler equations)
│   │   └── mitigation.py            # Deflection strategies (gravity tractor, kinetic impactor)
│   │
│   ├── app.py                       # Main API server (FastAPI routes)
│   ├── models.py                    # Data models (Asteroid, ImpactResult, MitigationResult)
│   └── utils.py                     # Helper functions (logging, conversions)
│
│── data/                            # Sample datasets
│   ├── sample_asteroids.json        # Example NASA data (offline demo)
│   ├── usgs_topo.csv                # Elevation data (mock)
│   └── tsunami_zones.json           # Tsunami dataset (mock)
│
│── frontend/                        # Hackathon-ready vanilla frontend
│   ├── index.html                   # Landing page
│   ├── simulator.html               # Main simulation page
│   │
│   ├── css/
│   │   └── style.css                # Tailwind CDN + custom styling
│   │
│   ├── js/
│   │   ├── api.js                   # Handles fetch() calls to backend
│   │   ├── orbitViewer.js           # Three.js orbit visualization
│   │   ├── impactMap.js             # Leaflet map for impact zones
│   │   ├── controls.js              # Sliders/inputs for asteroid params
│   │   ├── resultsPanel.js          # Display KE, crater, tsunami, seismic
│   │   └── mitigation.js            # Show mitigation strategies (impact vs deflection)
│
│── .env                             # API Keys (NASA_API_KEY=...)
│── requirements.txt                 # Python backend dependencies
│── package.json                     # (Optional) if you later use npm for frontend libs
│── readme.md                        # Project overview + setup instructions
