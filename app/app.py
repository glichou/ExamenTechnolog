from fastapi import FastAPI, HTTPException
from modele_vehicule import ModeleVehicule
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

@app.post("/vehicules/")
def create_vehicule(vehicule: ModeleVehicule):
    """ Ajouter un véhicule à la base de données
    """
    db = database()

    if db.vehicules.find_one({"immatriculation": vehicule.immatriculation}) is not None:
        HTTPException(status=403, detail="Ce véhicule a déjà été enregistré dans la base.")
    result = db.vehicules.insert_one(vehicule.dict())
    return vehicule.dict()

