from pydantic import BaseModel, validator
import re

class ModeleVehicule(BaseModel):
    """ Représentation d'un vehicule
    """

    immatriculation: str
    marque: str
    modele: str
    prix: float
    couleur: str

    @validator("marque")
    def control_brand_name_validity(cls, value):
        """ Vérifier la validité du nom de la marque du véhicule
        """
        if value == 'FakeBrand':
            raise ValueError('Cette marque n\'est pas valide !')
        return value

    @validator("couleur")
    def control_color_name_validity(cls, value):
        """ Vérifier la validité du nom de la couleur du véhicule
        """
        value = value.lower()
        if value not in ['blanche', 'grise', 'noire']:
            raise ValueError('Cette couleur est trop originale ! Essayez autre chose...')
        return value

    @validator("immatriculation")
    def control_immatriculation_validity(cls, value):
        """ Vérifier la validité du nom de la couleur du véhicule
        """
        if not re.match("^[A-Z]{2}[-][0-9]{3}[-][A-Z]{2} (9[12345]|7[578])$", value):
            raise ValueError('Pas de ça chez nous ! Cette immatriculation n\'est pas valide !')
        return value