import psycopg
from init_db import DSN
from init_request import Request

# SELECT un produit par son Id
def select_product_by_id(id_product: int):
    def action(cur):
        cur.execute(
            """
                SELECT name,price FROM products
                WHERE id_product = %s
            """, (id_product,)
            )
        
        product = cur.fetchone()
        print(product if product else "Aucun produit récupéré")
    return action


# SELECT tout les produits
def select_products(cur):
    cur.execute("""
                SELECT name, price FROM products
                """
            )
    products = cur.fetchall()

    if products:
        for product in products:
            print(product)
    else:
        print("Aucun produit récupéré")

# SELECT tout les produits
def select_products(cur):
    cur.execute("""
                SELECT name, price FROM products
                """
            )
    products = cur.fetchall()

    if products:
        for product in products:
            print(product)
    else:
        print("Aucun produit récupéré")

if __name__ == "__main__":
    
    # Sélection d'un produit
    print("Sélection d'un produit' par son Id :")
    Request("products", select_product_by_id(1)).commit()

    # Sélection de tous les produits
    print("Sélection de tous les produits :")
    Request("products", select_products).commit()


