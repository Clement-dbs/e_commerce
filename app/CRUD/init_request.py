import psycopg
from CRUD.init_db import DSN

class Request():
    
    def __init__(self, operation_name, function):
        self.operation_name = operation_name
        self.function = function
    
    def commit(self) -> None:
        try:
            with psycopg.connect(DSN) as conn:
                with conn.cursor() as cur:
                    self.function(cur)
        except psycopg.errors.SyntaxError as e:
            print(f"Opération : {self.operation_name} : Erreur de syntaxe SQL")
        except Exception as e:
            print (f"Opération {self.operation_name} : Autre erreurs : ", e)


  

