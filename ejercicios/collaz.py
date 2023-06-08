"""

CONJETURA DE COLLATZ

Realizar una página que muestre la conjetura de Collatz


Conjetura de Collatz

Todo número entero positivo llegará siempre a ser UNO siguiendo las siguientes reglas matemáticas:

    • Si el número es par: Dividimos entre dos
    • Si el número es impar: Multiplicados por tres y sumamos 1

Ejemplo práctico:

Número 6

6 / 2 = 3
3 * 3 + 1 = 10
10 / 2 = 5
5 * 3 + 1 = 16
16 / 2 = 8
8 / 2 = 4
4 / 2 = 2
2 / 2 = 1
"""

"""
numero = int(input('Introduce un numero y te lo desgloso en COLLATZ: ' ))
collatz = 0
resultado = 0

collatz = numero % 2

if collatz == 0:

    while resultado != 1:
        print(resultado)
        operacion = resultado / 2
        resultado = numero % 2
        if resultado == 0:
            resultado /= 2

        else:
            resultado = (resultado * 3) + 1
else:
    pass
"""
numero = int(input('Introduce un numero y te lo desgloso en COLLATZ: ' ))
resultado = ""

while numero != 1:
    resultado += '\n'
    if (numero % 2 == 0):
        numero = numero / 2
    else:
        numero = (numero * 3) + 1

    resultado += str(numero)
    resultado += '\n'

    print(numero) 
print(f"Resultado conjetura {resultado}")


