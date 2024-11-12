import azure.functions as func
import logging
import json
# import numpy as np  # Importer NumPy

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Configurer le logger
    logging.basicConfig(level=logging.DEBUG)
    
    # Exemple de log avec différents niveaux
    logging.debug("Ceci est un message de débogage.")
    logging.info("Ceci est un message d'information.")
    logging.warning("Ceci est un message d'avertissement.")
    logging.error("Ceci est un message d'erreur.")
    logging.critical("Ceci est un message critique.")
    
    # Log de la requête entrante
    logging.info(f"Requête reçue avec les paramètres : {req.params}")
    
    try:
        # test 
        import numpy as np  # Importer NumPy
        # Récupération des données de la requête
        req_body = req.get_json()
        values = req_body.get("values", [])
        
        # Vérifier si des valeurs sont fournies
        if not values:
            raise ValueError("Aucune donnée fournie pour le calcul.")

        # Utiliser NumPy pour calculer la moyenne
        mean_value = np.mean(values)
        result = {'mean': mean_value}  # Résultat avec NumPy
        
        logging.info(f"Calcul réussi avec résultat : {result}")
        
        # Retourner une réponse JSON avec le résultat
        return func.HttpResponse(
            json.dumps(result),  # Convertir le dictionnaire en JSON
            mimetype="application/json",  # Spécifier le type de contenu comme JSON
            status_code=200
        )
    
    except ValueError as ve:
        logging.error(f"Erreur de validation : {str(ve)}")
        return func.HttpResponse(f"Erreur: {str(ve)}", status_code=400)
    
    except Exception as e:
        logging.error(f"Erreur lors du calcul : {str(e)}")
        return func.HttpResponse(f"Erreur: {str(e)}", status_code=500)
