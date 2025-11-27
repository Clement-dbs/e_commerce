import psycopg

DSN = "dbname=supershop user=user password=password host=localhost port=5432"

# 1. Chiffre d’affaires total
def select_CA():
    try:
        with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                        SELECT SUM(o_i.quantity * o_i.unit_price) as chiffre_affaire
                        FROM order_items o_i
                        JOIN orders o
                            ON o.id_order = o_i.id_order_items
                        WHERE o.status IN ('PAID', 'SHIPPED');
                    """
                    )
                
                return str(cur.fetchone()[0])
            
    except psycopg.errors.SyntaxError as e:
            print(f"Opération  :  SELECT CA, Erreur de syntaxe SQL")
    except Exception as e:
            print (f"Opération : SELECT CA, Autre erreurs : ", e)

# 2. Panier moyen

def select_pannier_moyen():
    try:
        with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                        SELECT AVG(o_i.quantity * o_i.unit_price) as pannier_moyen
                        FROM order_items o_i
                        JOIN orders o
                            ON o.id_order = o_i.id_order_items
                        WHERE o.status IN ('PAID', 'SHIPPED');
                    """
                    )
                
                return str(cur.fetchone()[0])
                
    except psycopg.errors.SyntaxError as e:
            print(f"Opération  :  SELECT CA, Erreur de syntaxe SQL")
    except Exception as e:
            print (f"Opération : SELECT CA, Autre erreurs : ", e)


# 3. Article le plus commandé (en quantité totale).
def select_product_most_bought():
    try:
        with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT p.name, SUM(o_i.quantity) as total_quantity
                    FROM products p
                    JOIN order_items o_i  
                        ON o_i.id_product = p.id_product
                    JOIN orders o
                        ON o_i.id_order = o.id_order
                    GROUP BY p.id_product
                    ORDER BY total_quantity DESC
                    LIMIT 1
                """)
                
                return str(cur.fetchone()[0])

    except psycopg.errors.SyntaxError:
        print("Erreur SQL dans select_product_most_bought()")

    except Exception as e:
        print("Erreur dans select_product_most_bought() :", e)

# 4. Top 3 clients par montant dépensé.

def select_customer_most_bought():
    try:
        with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:
                cur.execute(  
                """
                    SELECT c.id_customer,c.first_name,c.last_name,
                    (
                        SELECT SUM(o_i.quantity * o_i.unit_price)
                        FROM orders o
                        JOIN order_items o_i 
                            ON o.id_order = o_i.id_order
                        WHERE o.id_customer = c.id_customer
                    ) AS total_depense
                    FROM customers c
                    ORDER BY total_depense DESC
                """
                )
              
                return str(cur.fetchall())
          
    except psycopg.errors.SyntaxError as e:
            print(f"Opération :  SELECT customers, Erreur de syntaxe SQL")
    except Exception as e:
            print (f"Opération : SELECT customers, Autre erreurs : ", e)

# 5. Chiffre d’affaires par catégorie.

def select_CA_by_categories():
    try:
        with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:
                cur.execute( 
                    """
                        SELECT c.name, SUM(o_i.quantity * o_i.unit_price) as chiffre_affaires_total
                        FROM categories c
                        JOIN products p 
                            ON p.id_category = c.id_category
                        JOIN order_items o_i  
                            ON o_i.id_product = p.id_product
                        JOIN orders o
                            ON o_i.id_order = o.id_order
                        GROUP BY c.id_category, c.name
                    """
                    )
                return str(cur.fetchall())
           
    except psycopg.errors.SyntaxError as e:
            print(f"Opération : SELECT CA by categories, Erreur de syntaxe SQL")
    except Exception as e:
            print (f"Opération : SELECT CA by categories, Autre erreurs : ", e)

