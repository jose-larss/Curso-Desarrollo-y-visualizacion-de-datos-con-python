"""
EJECUTAR PROCEDIMIENTOS ALMACENADOS
    • Insertar registros en la tabla DEPT a través de procedimientos almacenados.
    • Pasar los tres parámetros al procedimiento almacenado.

"""

import cx_Oracle

connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

cursor = connection.cursor()
try:

    dp = input("Número de departamento:")
    nombre = input("Nombre departamento:")
    localidad = input("localidad:")

    cursor.callproc("InsertarDEPT", (dp, nombre, localidad))
    print(cursor.rowcount)
    if cursor.rowcount > 0:
        print("Registro insertado satisfactoriamente")
    else:
        print("Dato no encontrado")



except connection.Error as error:
    print("Error: ", error)
cursor.close()
connection.close()