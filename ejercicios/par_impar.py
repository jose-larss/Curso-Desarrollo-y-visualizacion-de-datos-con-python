"""
NÚMERO PAR O IMPAR

    • Introducir por teclado un número.
    • Mostrar en pantalla si el número introducido es par o impar.
    • Recordamos que un número es par si al multiplicarlo por dos, el resto es cero.
"""

numero = int(input('Introduce un numero: '))
modulo = numero % 2

if modulo == 0:
    print('El numero es PAR')
else:
    print('El numero es IMPAR')