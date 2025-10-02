
# 🌌 Meteor Madness 🚀

An **interactive asteroid impact simulator** built for the **NASA Space Apps Challenge 2025**.  
Our tool enables users to **explore asteroid orbits, simulate impact scenarios, predict consequences, and evaluate mitigation strategies** using real datasets from **NASA** and **USGS**.  

---

## 📌 Problem Statement
Current asteroid-tracking tools focus on **detection and orbital tracking**, but they lack accessible simulations of **impact effects** (craters, tsunamis, seismic events) and **deflection strategies**.  
This creates a gap between **scientists, policymakers, and the public**.  

---

## 🎯 Our Solution
Meteor Madness bridges this gap with a **web-based interactive simulator** that combines:  
- 🛰️ **NASA NEO API** → Asteroid characteristics (size, velocity, trajectory)  
- 🌍 **USGS datasets** → Topography, seismic activity, tsunami risk zones  
- ⚙️ **Physics models** → Kinetic energy, crater scaling, orbital mechanics  
- 🛰️ **Mitigation strategies** → Kinetic impactor, gravity tractor  

---

## 📂 Project Structure
```

Meteor-Madness/
│
│── backend/                         # Python FastAPI backend
│   │── **init**.py
│   │
│   │── api/
│   │   ├── **init**.py
│   │   ├── nasa_client.py           # NASA NEO API client
│   │   ├── usgs_client.py           # USGS datasets client
│   │   ├── impact_calc.py           # Impact physics (KE, crater, seismic)
│   │   ├── orbit_sim.py             # Orbital mechanics
│   │   └── mitigation.py            # Deflection strategies
│   │
│   ├── app.py                       # FastAPI server entrypoint
│   ├── models.py                    # Data models
│   └── utils.py                     # Helper functions
│
│── data/
│   ├── sample_asteroids.json        # Mock NASA data
│   ├── usgs_topo.csv                # Mock elevation data
│   └── tsunami_zones.json           # Mock tsunami zones
│
│── frontend/
│   ├── index.html                   # Landing page
│   ├── simulator.html               # Main simulator UI
│   │
│   ├── css/style.css                # Tailwind + custom CSS
│   │
│   ├── js/
│   │   ├── api.js                   # API calls
│   │   ├── orbitViewer.js           # Three.js orbit visualization
│   │   ├── impactMap.js             # Leaflet impact zones
│   │   ├── controls.js              # UI sliders/inputs
│   │   ├── resultsPanel.js          # Results (KE, crater, tsunami)
│   │   └── mitigation.js            # Mitigation strategy comparisons
│
│── .env                             # API Keys (NASA_API_KEY=...)
│── requirements.txt                 # Python dependencies
│── package.json                     # (Optional) for frontend npm packages
│── readme.md                        # Project overview

````

---

## ⚙️ Tech Stack
- **Backend:** FastAPI (Python), Uvicorn  
- **Frontend:** HTML, CSS (Tailwind), JavaScript, Three.js, Leaflet  
- **Data Sources:** NASA NEO API, USGS datasets  
- **Other:** JSON datasets for offline demo  

---

## 🚀 Getting Started

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-repo/meteor-madness.git
cd meteor-madness
````

### 2️⃣ Backend Setup

```bash
cd backend
python3 -m venv Neo
source venv/bin/activate   # On Windows: venv\Scripts\activate #On Mac: source Neo/bin/activate
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```
NASA_API_KEY=your_api_key_here
```

Run the FastAPI server:

```bash
uvicorn backend.app:app --reload
```

API docs available at 👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

### 3️⃣ Frontend Setup

You can open the frontend directly in your browser:

```
frontend/index.html
```

Or serve it locally with Python:

```bash
cd frontend
python3 -m http.server 3000
```

Frontend runs at 👉 [http://127.0.0.1:3000](http://127.0.0.1:3000)

---

## 🌍 Features

* 🔭 **3D Orbit Viewer** (Three.js)
* 🌊 **Impact Heatmap** (Leaflet + USGS data)
* 📊 **Impact Results Panel** (energy, crater size, seismic, tsunami effects)
* 🛰️ **Mitigation Panel** (before vs after deflection strategies)
* 🎮 **Interactive Controls** (size, velocity, trajectory sliders)

---

## 📸 Screenshots / Demo

### 🏠 Landing Page

![Landing Page](./assets/screenshots/landing.png)

### 🚀 Simulator Dashboard

![Simulator](./assets/screenshots/simulator.png)

### 🔭 Orbit Visualization

![Orbit Viewer](./assets/screenshots/orbit.png)

### 🌊 Impact Map

![Impact Map](./assets/screenshots/impactmap.png)

---

## 👨‍🚀 Team Orbital-Skylab

* **Sasanka Sekhar Kundu** — Backend & API Engineer
  [![GitHub](https://img.shields.io/badge/GitHub-000?logo=github\&logoColor=white)](https://github.com/sasanka)
  [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?logo=linkedin\&logoColor=white)](https://linkedin.com/in/sasanka)

* **Raad Dalwai** — Frontend & UI/UX Developer
  [![GitHub](https://img.shields.io/badge/GitHub-000?logo=github\&logoColor=white)](https://github.com/raad)
  [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?logo=linkedin\&logoColor=white)](https://linkedin.com/in/raad)

* **Shastang** — Physics & Simulation Specialist
  [![GitHub](https://img.shields.io/badge/GitHub-000?logo=github\&logoColor=white)](https://github.com/shastang)
  [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?logo=linkedin\&logoColor=white)]()

* **Arnesh** — Mathematical Modeling & Algorithms
  [![GitHub](https://img.shields.io/badge/GitHub-000?logo=github\&logoColor=white)](https://github.com/arnesh)
  [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?logo=linkedin\&logoColor=white)](https://linkedin.com/in/arnesh)

* **Annayna** — Research & Content Strategist
  [![GitHub](https://img.shields.io/badge/GitHub-000?logo=github\&logoColor=white)]()
  [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?logo=linkedin\&logoColor=white)]()

* **Simran** — Validation & Outreach
  [![GitHub](https://img.shields.io/badge/GitHub-000?logo=github\&logoColor=white)]()
  [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?logo=linkedin\&logoColor=white)](https://linkedin.com/in/simran)

---

## 📜 License

MIT License — free to use, modify, and share.
