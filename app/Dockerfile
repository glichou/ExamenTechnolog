# Définir l'image de base.
FROM python:3.10-alpine

# Installer les dépendances nécessaires à l'execution du script Python
RUN pip install fastapi
RUN pip install uvicorn
RUN pip install pymongo
# RUN pip install requests

# Copie du repertoire courant dans le repertoire de travail
COPY . .

# Définir le port d'écoute du conteneur
EXPOSE 3000

# Lancer le serveur uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "3000"]