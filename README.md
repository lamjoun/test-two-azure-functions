
# Azure Function App - Multi-Function Project

## Objectif

Ce dépôt GitHub héberge plusieurs Azure Functions intégrées dans une même Function App. Ce projet vise à démontrer l’utilisation de trois fonctions Azure, incluant la lecture de fichiers CSV stockés dans un Azure Blob Storage.

Les fonctions incluses dans ce dépôt sont les suivantes :
- **test_function** : première fonction de test avec un fichier `requirements.txt` spécifique.
- **max_function** : calcul du maximum de la colonne `c1` du fichier `test1.csv` situé dans le container `test21container`.
- **mean_function** : calcul de la moyenne de la colonne `c1` du fichier `test1.csv`.

## Structure du dépôt

Chaque dossier de fonction inclut un fichier `requirements.txt` contenant les dépendances nécessaires :
```plaintext
pandas
azure-functions
azure-storage-blob
```

## Prérequis - Azure Storage Connection String

Pour accéder aux données stockées dans Azure Blob Storage, vous devez configurer une chaîne de connexion pour le compte de stockage Azure. Voici les étapes à suivre :

1. **Créer un compte de stockage** : `santest21`.
2. **Créer un container** : `test21container` (via Data storage --> Containers).
3. **Uploader le fichier `test1.csv`** dans `test21container`.
4. **Obtenir la chaîne de connexion** :
   - Dans le compte de stockage, allez dans **Sécurité + réseau** -> **Clés d'accès**.
   - Copiez l'une des chaînes de connexion disponibles (par exemple, de la forme `DefaultEndpointsProtocol=https;AccountName=santest21;AccountKey=xxxxxxxxxx;EndpointSuffix=core.windows.net`).

## Application client - Streamlit

Le fichier `app.py` contient une application client Streamlit permettant d’interagir avec les fonctions Azure via une interface Web.

### Installation et Exécution

1. **Créer un environnement virtuel Python** :
   ```bash
   python -m venv client_env
   source ./client_env/Scripts/activate  # Sur Windows, utilisez .\client_env\Scripts\activate
   ```
2. **Installer les dépendances** :
   ```bash
   pip install streamlit requests
   ```
3. **Lancer l'application** :
   ```bash
   streamlit run app.py
   ```

Note : Assurez-vous de mettre à jour les URLs des Azure Functions dans `app.py` avec les valeurs correctes.

## Déploiement continu avec GitHub Actions

1. **Créer une Function App** :
   - Choisir l'option **Consumption** (facturation à l'usage).
   - Sélectionner la région : *East US2*.
   - Choisir Python 3.9 et le système Linux.
   - Garder l'accès public activé par défaut.

2. **Configurer le déploiement GitHub** :
   - Lier la Function App à votre dépôt GitHub.
   - Activer l'authentification de base (Basic authentication).
   - Un fichier de configuration GitHub Action (`.github/workflows`) sera généré automatiquement et permettra le déploiement à chaque `push` sur le dépôt.

## Fonctions disponibles

### `test_function`
- **Objectif** : Fournit une fonction de test pour vérifier la configuration de l'API.

### `max_function`
- **Objectif** : Calcule la valeur maximale de la colonne `c1` du fichier `test1.csv` situé dans le container Azure Blob `test21container`.

### `mean_function`
- **Objectif** : Calcule la moyenne de la colonne `c1` du fichier `test1.csv`.

## Technologies utilisées

- **Azure Functions** : Hébergement et exécution des fonctions.
- **Streamlit** : Interface utilisateur pour interagir avec les fonctions.
- **GitHub Actions** : Déploiement continu sur Azure.
- **Python** : Langage de développement des fonctions.

## Configuration des paramètres

### Variables d'environnement

Définissez les variables d'environnement suivantes dans Azure pour accéder au Blob Storage :
- **AZURE_STORAGE_CONNECTION_STRING** : Chaîne de connexion pour le compte de stockage.

---
