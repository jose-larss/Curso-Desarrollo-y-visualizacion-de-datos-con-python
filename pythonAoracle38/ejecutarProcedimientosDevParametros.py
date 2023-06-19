"""
EjecutarProcedimientoSalida.py

Podemos recuperarlo declarando el parámetro con el tipo de dato con var(cx_Oracle.TIPODEDATO):

cx_Oracle.STRING
cx_Oracle.NUMBER



"""


import cx_Oracle

connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

cursor = connection.cursor()
try:

    dp = input("Número de departamento:")
    #este parametro de salida hay que indicarle el tipo oracle
    loc = cursor.var(cx_Oracle.STRING)
    #loc = ""

    args = (loc, dp)
    cursor.callproc('DevolverLocalidad', args)
    #print(dato[0])
    #print(dato[1])
    #print(cursor.callproc)

    #print(loc.getvalue())
    print(loc.getvalue())

except connection.Error as error:
    print("Error: ", error)
cursor.close()
connection.close()