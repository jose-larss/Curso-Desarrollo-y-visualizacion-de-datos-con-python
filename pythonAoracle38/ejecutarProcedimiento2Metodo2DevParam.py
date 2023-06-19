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


    args = (apellido, sexo, nseg)
    cursor.callproc('DevolverNomSexo', args)

    print(apellido.getvalue())

    if sexo.getvalue() == 'M':
        print('MASCULINO')
    else:
        print('FEMENINO')

except connection.Error as error:
    print("Error: ", error)
cursor.close()
connection.close()