"""
EJECUTAR PROCEDIMIENTO CON VARIOS PARÁMETROS DE SALIDA
    • Realizar un procedimiento almacenado en la base de datos que pasándole un número de la seguridad social, nos devuelva el apellido del enfermo, así como el sexo (Hombre o mujer).
    • Si el sexo es F devolverá MUJER, si es M devolverá HOMBRE.

"""

import cx_Oracle

connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

cursor = connection.cursor()
try:

    nseg = input("Número numero de la seguridad social: ")
    #este parametro de salida hay que indicarle el tipo oracle
    apellido = cursor.var(cx_Oracle.STRING)
    sexo = cursor.var(cx_Oracle.STRING)

    #La select es de este tipo Select apellido, decode(turno, ‘T’, ‘TARDE’, ‘M’, ‘MAÑANA’, ‘N’, NOCHE)
    args = (apellido, sexo, nseg)
    cursor.callproc('DevolverNomSexoMetodo2', args)

    print(apellido.getvalue())
    print(sexo.getvalue())


except connection.Error as error:
    print("Error: ", error)
cursor.close()
connection.close()