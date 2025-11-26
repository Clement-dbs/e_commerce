import psycopg
from init_db import DSN

class Request():
    
    def __init__(self, table, function):
        self.table = table
        self.function = function
    
    def commit(self) -> None:
        try:
            with psycopg.connect(DSN) as conn:
                with conn.cursor() as cur:
                    self.function(cur)
        except psycopg.errors.SyntaxError as e:
            print(f"Table {self.table} : Erreur de syntaxe SQL")
        except Exception as e:
            print (f"Table {self.table} : Autre erreurs : ", e)


  

