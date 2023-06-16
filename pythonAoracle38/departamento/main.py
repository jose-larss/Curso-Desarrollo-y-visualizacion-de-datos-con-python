import sys

from funciones import borrar, listar, modificar, insertar


print('***************************************************************')
print('*********************MENU DEPARTAMENTO*************************')
print('***************************************************************')

opcion = 0

while opcion != 5:
    print('**********1.- ALTA EN DEPARTAMENTO*******')
    print('**********2.- BAJA EN DEPARTAMENTO*******')
    print('**********3.- MODIFICAR EN DEPARTAMENTO*******')
    print('**********4.- VER DATOS EN DEPARTAMENTO*******')
    print('**********5.- SALIR**************************')

    try:
        opcion = int(input('Introduce una opción: (5 - SALIR): '))
        print('***************************************************************')

        if opcion == 1:
            codigo = int(input("Introduce numero departamento nuevo:"))
            nombre = input("Introduce nombre departamento nuevo:")
            localidad = input("Introduce localidad departamento nuevo:")
            insertar(codigo, nombre, localidad)
        elif opcion == 2:
            NumeroEmpleado = int(input("Introduce Número de departamento a eliminar:"))
            borrar(NumeroEmpleado)
        elif opcion == 3:
            numeroDepartamento = int(input("Número de departamento a modificar:"))
            nuevoLocalidad = input("Nueva localidad:")
            modificar(numeroDepartamento, nuevoLocalidad)
        elif opcion == 4:
            listar()
        elif opcion == 5:
            print('Gracias por su visita!!!!')
            sys.exit()
        else:
            print('Introduce un numero correcto del 1 al 5!!!')
    except ValueError:
        print('ERROR INTRODUCE NUMEROS, NO LETRAS')
