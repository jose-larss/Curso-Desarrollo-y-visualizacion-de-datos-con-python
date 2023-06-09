"""
pov potencia

NUMERO NARCISISTA

    • Realizar una aplicación para averiguar si un número introducido en una caja de texto es Narcisista o no.
    • La teoría para saber si un número es narcisista es la siguiente:
“Un número narcisista es aquel que, elevando a la potencia de su longitud de caracteres cada uno de sus números individuales, dan como resultado de su suma, el mismo número.”

Ejemplo de número narcisista:   371

Número de caracteres: 3
Potencia: 3

3 elevado a 3 = 27
7 elevado a 3 = 343
1 elevado a 3 = 1

La suma de sus N valores es 27 + 343 + 1 = 371  
El número es narcisista.

Otro ejemplo de número narcisista: 9474.
"""

numero = input('Introduce un numero para ver si es narcisista: ')

resultado = 0
for i in numero:
  
    fila = pow(int(i), len(numero))
    resultado += fila

if resultado == int(numero):
    print('Es narcisista')
else:
    print('No es narcisista')

    
   
