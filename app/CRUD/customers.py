import psycopg
from init_db import DSN
from init_request import Request

# SELECT un client par son Id
def select_customer_by_id(id_customer: int):
    def action(cur):
        cur.execute(
            """
                SELECT * FROM customers
                WHERE id_customer = %s
            """, (id_customer,)
            )
        
        customer = cur.fetchone()
        print(customer if customer else "Aucun client récupéré")
    return action


# SELECT tout les client
def select_customers(cur):
    cur.execute("""
                SELECT * FROM customers
                ORDER BY date_of_account_creation ASC
                """
            )
    customers = cur.fetchall()
    print(customers if customers else "Aucun client récupéré")




if __name__ == "__main__":
    
    # Sélection d'un client
    print("Sélection d'un client' par son Id :")
    Request("customers", select_customer_by_id(1)).commit()

    # Sélection de tous les clients
    print("Sélection de tous les clients :")
    Request("customers", select_customers).commit()


