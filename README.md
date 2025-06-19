Une structure minimale pour commencer le backend de l'application avec la connexion à l'api de dolibarr
structure du dossier:
    -api:
        -contient les appels d'api vers dolibarr
        -dans apis, on a les classes qui font les requetes http vers dolibarr
        -dans config on a la base url et l'api key (il faudra le changer selon les votres)
        -dans db on a la classe qui s'occupe de la connection à mysql DbConnector
        -dans dependancy on a les variables de connexion à l'api de dolibarr API et une instance DbConnector
    -entity
        -classe représentant les entités , ici on a également celles gérées par dolibarr.
    -repository
        -contient des classes implémentant les fonctions des appels d'api et utilisant les classes d'entity (persistence)
    -service
        -la logique métier.

installation:
-lancer d'abord votre environnement virtuel python avec:
    python -m venv venv
-activer le 
    venv\bin\activate
-puis intaller les dépendances avec;
    pip install -r requirements.txt