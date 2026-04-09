from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import math

app= FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"]
    allow_methods=["*"]
    allow_headers=["*"]
)

G=6.6743*(10**-11) #in m^3 kg^-1 s^-2
c=299792458 #in m/s
M_sun= 1.989*(10**30)


@app.get("/api/blackhole/{solar_masses}")
def get_blackhole_data(solar_masses: float):
    mass_kg = solar_masses * M_sun
    rs_meters = (2 * G * mass_kg)/(c**2)
    
    photon_sphere = 1.5 * rs_meters
    
    scale_factor= 1e-3
    
    return{
        "solar_masses": solar_masses,
        "event_horizon_radius": rs_meters * scale_factor,
        "photon_sphere_radius": photon_sphere * scale_factor,
        "lensing_strength": math.log10(solar_masses + 1) * 2.0
    }
