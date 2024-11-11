import azure.functions as func
import logging
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Execution de la fonction Azure.")

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

        # Logique de traitement ici
        # Exemple de retour
        result = {"mean": 42}  # Remplacez avec la logique réelle
        return func.HttpResponse(json.dumps(result), status_code=200, mimetype="application/json")

    except ValueError:
        return func.HttpResponse("Erreur : données JSON invalides.", status_code=400)
    except Exception as e:
        logging.error(f"Erreur : {str(e)}")
        return func.HttpResponse(f"Erreur : {str(e)}", status_code=500)
