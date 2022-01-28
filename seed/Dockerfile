# Définir l'image de base.
FROM python:3.10.1-slim-bullseye

# Installer les dépendances nécessaires à l'execution du script Python
RUN pip install pymongo

# Copier dans le conteneur le script Python
COPY seeder.py .

# Executer le script d'alimentation de la BDD.
CMD python seeder.py