import psycopg

with psycopg.connect("dbname=user user=user password=password host=db port=5432") as conn:
    with conn.cursor() as cur:
        cur.execute("")
        cur.execute(""")
          
                
            );
        """)