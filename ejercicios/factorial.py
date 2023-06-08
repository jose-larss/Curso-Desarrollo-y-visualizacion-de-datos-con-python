"""
    • Realizar una aplicación que nos pida por teclado un número y mostremos el factorial de dicho número.

El factorial se define como el producto de un número y sus antecesores empezando desde 1. Y se le reconoce por este símbolo: "n!".

Ejemplo de factoriales de números:

"""

numero  = int(input('Introduce NUM y te digo el Factorial: '))

factorial = 1
contador = 1
while contador < numero + 1:
    
    factorial *= contador
    contador += 1

print(f'El factorial de {numero} es : {factorial}')
