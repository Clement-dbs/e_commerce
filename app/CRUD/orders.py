import psycopg
from init_db import DSN
from init_request import Request

# SELECT une commande par son Id
def select_order_by_id(id_order: int):
    def action(cur):
        cur.execute(
            """
                SELECT * FROM orders
                WHERE order_date BETWEEN '2024-03-01 00:00:00' AND '2024-03-15 00:00:00'
                AND id_order = %s
            """, (id_order,)
            )
        
        order = cur.fetchone()
        print(order if order else "Aucunes commande récupéré")
    return action


# SELECT tout les produits
def select_orders(cur):
    cur.execute("""
                SELECT * FROM orders
                WHERE order_date BETWEEN '2024-03-01 00:00:00' AND '2024-03-15 00:00:00'
                """
            )
    orders = cur.fetchall()

    if orders:
        for order in orders:
            print(order)
    else:
        print("Aucunes commande récupéré")

if __name__ == "__main__":
    
    # Sélection d'un commande
    print("Sélection d'une commande par son Id :")
    Request("orders", select_order_by_id(1)).commit()

    # Sélection de tous les produits
    print("Sélection de toutes les commandes :")
    Request("orders", select_orders).commit()


