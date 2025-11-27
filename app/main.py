import psycopg
from CRUD.init_db import DSN
from CRUD.init_request import Request
from CRUD.requests import *
from write import WriteInFile

if __name__ == "__main__":
    
    # Récupère le chiffre d'affaire
    print("Récupère le chiffre d'affaire")
    request = select_CA()
    print(request)
    #WriteInFile("fichier_analyses", request).write()

    # Récupère le panier moyen
    print("Récupère le panier moyen")
    request = select_pannier_moyen()
    print(request)

    # Récupère l'article le plus vendu
    print("Récupère l'article le plus vendu")
    request = select_product_most_bought()
    print(request)

    # Récupère le top des clients qui ont le plus dépensé
    print("Récupère le top des clients qui ont le plus dépensé")
    request = select_customer_most_bought()
    print(request)

    # Récupère le chiffre d’affaires par catégorie
    print("Récupère le chiffre d’affaires par catégorie")
    request = select_CA_by_categories()
    print(request)
