import cx_Oracle

connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

cursor = connection.cursor()
try:

    ConsultaBaja = ("Delete from emp where emp_no=:param1")

    NumeroEmpleado = input("Número de empleado a eliminar:")

    cursor.execute(ConsultaBaja, (NumeroEmpleado,))

    if cursor.rowcount > 0:
        print("Registro eliminado satisfactoriamente")
        connection.commit()
    else:
        print("Dato no encontrado")

except connection.Error as error:
    print("Error: ", error)

cursor.close()
connection.close()