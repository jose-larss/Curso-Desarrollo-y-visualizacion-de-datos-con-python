import cx_Oracle

connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

cursor = connection.cursor()
try:
    print('la conexion esta OK')


except connection.Error as error:
    print("Error: ", error)

connection.close()