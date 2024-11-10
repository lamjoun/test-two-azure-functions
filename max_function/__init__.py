import azure.functions as func
import logging
import pandas as pd
from azure.storage.blob import BlobServiceClient
import json
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Configurer le logger
    logging.basicConfig(level=logging.DEBUG)
    logging.info("----max_function()-----")

    try:
        logging.info("----req.params.get()-----")
        # Récupérer le nom du fichier et la colonne dans les paramètres de requête
        blob_name = req.params.get('file')
        column = req.params.get('column')
        
        if not blob_name or not column:
            return func.HttpResponse("Veuillez fournir le nom du fichier et la colonne.", status_code=400)
        
        # Connexion au Blob Storage
        connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        container_name = "test21container"  # Remplacez par le nom de votre conteneur
  
        logging.info("----Acces au container...-----")      
        # Accéder au blob (fichier CSV)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        blob_data = blob_client.download_blob().content_as_text()

        # Charger les données CSV dans un DataFrame pandas
        df = pd.read_csv(pd.compat.StringIO(blob_data))
        
        # Vérifier si la colonne existe dans le fichier
        if column not in df.columns:
            return func.HttpResponse("La colonne spécifiée n'existe pas dans le fichier.", status_code=400)
        
        # Calculer le maximum pour la colonne spécifiée
        max_value = df[column].max()
        
        # Retourner le résultat en JSON
        result = {
            "max": max_value
        }
        return func.HttpResponse(json.dumps(result), mimetype="application/json", status_code=200)
    
    except Exception as e:
        return func.HttpResponse(f"Erreur lors du traitement : {str(e)}", status_code=500)
