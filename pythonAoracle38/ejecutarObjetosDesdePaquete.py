import sys
import cx_Oracle

connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

cursor = connection.cursor()
try:

    opcion = 0

    while opcion != 4:

        print('1.- Busqueda Salario y Comision')
        print('2.- Modifica Salario y comision')
        print('3.- Borrar Doctor')
        print('4.- Borrar Empleado')
        print('5.- SALIR')

        opcion = int(input("Introduce un opcion: "))

        if opcion == 1:
            nEmp = int(input("Introduzca numero de empleado: "))
            # este parametro de salida hay que indicarle el tipo oracle
            salario = cursor.var(cx_Oracle.NUMBER)
            comision = cursor.var(cx_Oracle.NUMBER)
            numero = cursor.var(cx_Oracle.NUMBER)

            args = (salario, comision, nEmp, numero)
            cursor.callproc('proc4.devolverSalCom', args)
            print(f"El salario es {salario.getvalue()}")
            print(f"La comision es {comision.getvalue()}")
            if numero.getvalue() > 0:
                print(f'Las columnas afectadas son {numero.getvalue()}')
            """
            if comision.getvalue() == 'null':
                print(f"Este empleado no tiene Comision {nEmp}")
            else:
                print(f"La comision es {comision.getvalue()}")
            """
        elif opcion == 2:
            nEmp = int(input("Introduzca numero de empleado: "))
            sal_nuevo = int(input("Introduzca Salario nuevo del empleado: "))
            com_nuevo = int(input("Introduzca comision nueva del empleado: "))
            # este parametro de salida hay que indicarle el tipo oracle

            args = (sal_nuevo, com_nuevo, nEmp)
            cursor.callproc('proc4.modificarSalCom', args)
            print(
                    f"Se acaba de modificar el empleado nº: {nEmp} con el salario nuevo: {sal_nuevo} y comision nueva: {com_nuevo}")
        elif opcion == 3:
            apellido = input("Introduzca apellido de DOCTOR a borrar: ")
            numero = cursor.var(cx_Oracle.NUMBER)

            args = (apellido, numero)
            cursor.callproc('BORRAR_DOCTOR2', args)
            print(f'Se han borrado {numero.getvalue()} registro/s con este {apellido}')
        elif opcion == 4:
            nEmp = int(input("Introduzca numero de empleado: "))
            numero = cursor.var(cx_Oracle.NUMBER)

            args = (nEmp, numero)
            cursor.callproc('BORRAR_EMPLEADO', args)
            print(f"Los registros afectados por el borrado son {numero.getvalue()}")


        elif opcion == 5:
            print('GRACIAS POR LA VISITA')
            sys.exit()


except connection.Error as error:
    print("Error: ", error)
cursor.close()
connection.close()
