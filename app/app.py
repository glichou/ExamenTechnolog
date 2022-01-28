from fastapi import FastAPI, HTTPException
from utility import database

app = FastAPI()

@app.get("/vehicules")
def fetch_vehicules():
    """ Récupérer la liste des véhicules enregistrés
    """
    db = database()
    results = db.vehicules.find()
    vehicules = []

    for result in results:
        vehicule = {
            "immatriculation": result['immatriculation'],
            "marque": result['marque'],
            "modele": result['modele'],
            "prix": result['prix'],
            "couleur": result['couleur']
        }
        vehicules.append(vehicule)
    return vehicules

