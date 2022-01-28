""" Script utilisé pour peupler la base de donnée lors du premier lancement
"""

from pymongo import MongoClient

class MongoSeeder:

    def __init__(self, db_host: str):
        """ Initialisation de la base de données.
        """
        client = MongoClient(host=f'{db_host}')
        self.__db = client.registre

    @property
    def db(self):
        """ Récupérer la connexion à la base de données.
        """
        return self.__db

    def seed(self):
        """ Peupler la base de données avec des véhicules possédant des
        données valides. 
        """
        # Vider tous les véhicules dans la base de données.
        self.db.vehicules.drop()

        # Initialiser une liste de véhicules.
        vehicules = []

        # Créer un premier véhicules.
        vehicules.append(
            {
                "immatriculation": "NE-212-BA 91",
                "marque": "Cadillac",
                "modele": "Escalade ESV",
                "prix": 150000.00,
                "couleur": "noire"
            }
        )
        # Insérer dans la base de données les véhicules.
        self.db.vehicules.insert_many(vehicules)

    def dispayDBContent(self): 
        """ Afficher les informations dans la base MongoDB
        """
        cursor = self.db.vehicules.find()
        for vehicule in cursor:
            print(vehicule)



print("Initialisation de la base de données...")
s = MongoSeeder("MongoDB")
print("Peuplement de la base de données en cours...")
s.seed()
print("Affichage du contenu de la base...")
s.dispayDBContent()