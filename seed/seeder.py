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


print("Initialisation de la base de données...")
s = MongoSeeder("MongoDB")
print("Peuplement de la base de données en cours...")


s.seed()