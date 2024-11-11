from azure.storage.blob import BlobServiceClient
import azure.functions as func
from io import StringIO
import pandas as pd
import logging
import json
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Execution de la fonction Azure: mean_function...")

    try:
        # Vérifiez si les données JSON sont bien reçues
        req_body = req.get_json()
        blob_name = req_body.get('file')
        column = req_body.get('column')

        # Vérifiez la récupération des paramètres
        logging.info(f"Nom du fichier: {blob_name}")
        logging.info(f"Nom de la colonne: {column}")

        # Assurez-vous que le fichier et la colonne sont fournis
        if not blob_name or not column:
            return func.HttpResponse("Paramètres 'file' ou 'column' manquants.", status_code=400)

        # calcul du mean
        # Connexion au Blob Storage
        connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        container_name = "test21container"
        
        # Accéder au blob (fichier CSV)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        blob_data = blob_client.download_blob().content_as_text()

        # Charger les données CSV dans un DataFrame pandas
        df = pd.read_csv(StringIO(blob_data))
        
        # Vérifier si la colonne existe dans le fichier
        if column not in df.columns:
            return func.HttpResponse("La colonne spécifiée n'existe pas dans le fichier.", status_code=400)
        
        # Calculer la moyenne pour la colonne spécifiée
        mean_value = str(df[column].mean())
        result = {"mean": mean_value}  # Remplacez avec la logique réelle
        return func.HttpResponse(json.dumps(result), status_code=200, mimetype="application/json")

    except ValueError:
        return func.HttpResponse("Erreur : données JSON invalides.", status_code=400)
    except Exception as e:
        logging.error(f"Erreur : {str(e)}")
        return func.HttpResponse(f"Erreur : {str(e)}", status_code=500)
