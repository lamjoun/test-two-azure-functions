import streamlit as st
import requests

# URL des Azure Functions
MEAN_FUNCTION_URL = "https://test21rlapp.azurewebsites.net/api/mean_function"
MAX_FUNCTION_URL = "https://test21rlapp.azurewebsites.net/api/max_function"
tesT_FUNCTION_URL = "https://test21rlapp.azurewebsites.net/api/test_function"

# Titre de l'application Streamlit
st.title("Calcul de Moyenne et Max d'une Colonne CSV sur Blob Storage")

# Nom du fichier et colonne avec valeurs par défaut
blob_name = st.text_input("Nom du fichier CSV dans Blob Storage", value="test1.csv")
column = st.text_input("Nom de la colonne", value="c1")

# Bouton pour calculer la moyenne
if st.button("Calculer Moyenne"):
    data = {'file': blob_name, 'column': column}
    response = requests.post(MEAN_FUNCTION_URL, json=data)
    if response.status_code == 200:
        result = response.json()
        st.write(f"Moyenne : {result['mean']}")
    else:
        st.error("Erreur : " + response.text)

# Bouton pour calculer le maximum
if st.button("Calculer Maximum"):
    data = {'file': blob_name, 'column': column}
    response = requests.post(MAX_FUNCTION_URL, json=data)
    if response.status_code == 200:
        result = response.json()
        st.write(f"Max : {result['max']}")
    else:
        st.error("Erreur : " + response.text)

# Bouton pour tester l'appel de tesT_FUNCTION_URL
if st.button("Tester Fonction de Test"):
    response = requests.get(tesT_FUNCTION_URL)
    if response.status_code == 200:
        result = response.json()
        st.write(f"Réponse de test : {result}")
    else:
        st.error("Erreur lors de l'appel de la fonction de test : " + response.text)
