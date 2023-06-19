
import cx_Oracle

connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

# una matriz o array y losa datos que devuelva se vuelcan en esta variable
cursor = connection.cursor()
try:

    cursor.execute("SELECT emp_no, apellido FROM emp")

    print("Lista de empleados:")
    print("---------------------------------------")

    for numero,ape in cursor:
            print("Número empleado:", numero, "Apellido:", ape)


except connection.Error as error:
    print("Error: ", error)

connection.close()