import psycopg
import csv

from requests import *

if __name__ == "__main__":

    chiffre_affaire = str(select_CA())
    panier_moyen = str(select_pannier_moyen())
    article_plus_vendu = str(select_product_most_bought())
    tp_client_depense = str(select_customer_most_bought())
    chiffre_affaire_par_categorie = str(select_CA_by_categories())

    with open("analyses.txt","w",encoding='utf-8') as data_file:
            data_file.write("=== Chiffre d'affaire === \n")
            data_file.write(f"Le chiffre d’affaires total (hors commandes annulées) est de {chiffre_affaire} € \n \n")
            data_file.write("=== Panier moyen === \n")
            data_file.write(f"Le panier moyen (hors commandes annulées) est de {panier_moyen} par commande \n \n")
            data_file.write("=== Article le plus vendu === \n")
            data_file.write(f"L’article ayant généré le plus de ventes (en quantité totale) est : {article_plus_vendu} \n \n")
            data_file.write("=== Top des clients qui ont le plus dépensé === \n")
            data_file.write(f"Les trois clients ayant le plus dépensé (hors commandes annulées) sont : {tp_client_depense} \n \n")
            data_file.write("=== Chiffre d’affaires par catégorie === \n")
            data_file.write(f"Répartition du chiffre d’affaires (hors commandes annulées) par catégorie de produits : {chiffre_affaire_par_categorie} \n \n")
 
