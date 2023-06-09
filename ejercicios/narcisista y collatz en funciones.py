"""
    • Organizar en dos funciones el ejercicio de comprobación de número narcisista y el ejercicio de conjetura de collatz.
    • Crear a continuación de las dos funciones una prueba para trabajar con las dos funciones.
"""
import sys


def narcisista(numero):

    resultado = 0
    for i in numero:
    
        fila = pow(int(i), len(numero))
        resultado += fila

    if resultado == int(numero):
        mensaje = 'Es narcisista'
    else:
        mensaje = 'No es narcisista'
    
    return mensaje

def collatz(numero):

    resultado = ""

    while numero != 1:
        
        if (numero % 2 == 0):
            numero = numero / 2
        else:
            numero = (numero * 3) + 1

        resultado += f'{numero} '

    return f"Resultado conjetura {resultado}"
   

print('--------------------------------------------------------')
print('--------------PULSA UNA OPCION--------------------------')
print('--------------------------------------------------------')

opcion = 1

while opcion != 3:

    print('1.- COMPROBAR NÚMERO NARCISISTA')
    print('2.- MOSTRAR CONJETURA DE COLLAZT')
    print('3.- SALIR')
    print('--------------------------------------------------------')
    print('--------------------------------------------------------')

    opcion = int(input('Introduce una Opcion: '))

    if opcion == 1:
        print('--------------------------------------------------------')
        print('-----------------narcisista-----------------------------')
        print('--------------------------------------------------------')
        numero = input('Introduce un numero para ver si es narcisista: ')
        mensaje = narcisista(numero)
        print('--------------------------------------------------------')
        print(mensaje)
        print('--------------------------------------------------------')
    elif opcion == 2:
        print('--------------------------------------------------------')
        print('--------------------collatz-----------------------------')
        print('--------------------------------------------------------')
        numero = int(input('Introduce un numero y te lo desgloso en COLLATZ: ' ))
        resultado = collatz(numero)
        print('--------------------------------------------------------')
        print(resultado)
        print('--------------------------------------------------------')
    elif opcion == 3:
        sys.exit()

