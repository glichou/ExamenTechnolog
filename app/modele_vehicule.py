from pydantic import BaseModel, validator

class ModeleVehicule(BaseModel):
    """ Représentation d'un vehicule
    """

    immatriculation: str
    marque: str
    modele: str
    prix: float
    couleur: str