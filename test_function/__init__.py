import azure.functions as func
import logging

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
    
    # Traitement de la requête
    try:
        # Code de votre fonction ici
        # Par exemple : traitement sur un fichier CSV
        result = {'mean': 42}  # Valeur d'exemple
        logging.info(f"Calcul réussi avec résultat : {result}")
        
        return func.HttpResponse(f"Moyenne calculée : {result['mean']}", status_code=200)
    
    except Exception as e:
        logging.error(f"Erreur lors du calcul : {str(e)}")
        return func.HttpResponse(f"Erreur: {str(e)}", status_code=500)
