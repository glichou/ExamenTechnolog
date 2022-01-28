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
        raise HTTPException(status_code=403, detail="Ce véhicule a déjà été enregistré dans la base.")
    result = db.vehicules.insert_one(vehicule.dict())
    return vehicule.dict()

@app.get("/vehicules/{immatriculation}")
def fetch_vehicules_by_immatriculation(immatriculation: str):
    """ Rétrouver les informations d'un véhicule à partir de son immatriculation
    """
    db = database()
    result = db.vehicules.find_one({"immatriculation": immatriculation})
    if(result is not None):
        return {
            "immatriculation": result['immatriculation'],
            "marque": result['marque'],
            "modele": result['modele'],
            "prix": result['prix'],
            "couleur": result['couleur']
        }
    raise HTTPException(status_code=404, detail="Ce véhicule n'existe pas dans la base.")
    
@app.delete("/vehicules/{immatriculation}")
def delete_vehicule_by_immatriculation(immatriculation: str):
    """ Supprimer un véhicule à partir de son immatriculation
    """
    db = database()
    db.vehicules.delete_one({"immatriculation": immatriculation})