import psycopg

with psycopg.connect("") as conn:
    with conn.cursor() as cur:
        cur.execute("")
        cur.execute(""")
          
                
            );
        """)