import psycopg2

def conexion_BBDD():
    database =  psycopg2.connect(
            database="APPlineaComandoClases", 
            user="postgres", 
            password="1234"
        ) 
    cursor = database.cursor()

    return [database, cursor]
    
    

