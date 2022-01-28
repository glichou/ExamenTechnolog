from pymongo import MongoClient

DB_HOST: str = "MongoDB"

def database():
    """ Récupérer la connexion à la base de données MongoDB
    """
    client = MongoClient(host=f'{DB_HOST}')
    db = client.registre
    return db