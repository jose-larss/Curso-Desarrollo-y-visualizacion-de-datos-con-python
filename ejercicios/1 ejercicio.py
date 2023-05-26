"""
Indicar cuál es el menor de tres enteros solicitados al usuario
"""
"""
numero1 = int(input('Introduce numero 1: '))
numero2 = int(input('Introduce numero 2: '))
numero3 = int(input('Introduce numero 3: '))

if numero1 > numero2 and numero1 > numero3:
    print(f"{numero1} es el mayor que {numero2} y {numero3}")

elif numero2 > numero1 and numero2 > numero3:
    print(f"{numero2} es el mayor que {numero1} y {numero3}")

elif numero3 > numero1 and numero3 > numero2:
    print(f"{numero3} es el mayor que {numero1} y {numero2}")
"""

def mayorDe3(numero1, numero2, numero3):

    if numero1 > numero2 and numero1 > numero3:
        mensaje = (f"{numero1} es el mayor que {numero2} y {numero3}")

    elif numero2 > numero1 and numero2 > numero3:
        mensaje = (f"{numero2} es el mayor que {numero1} y {numero3}")

    elif numero3 > numero1 and numero3 > numero2:
        mensaje = (f"{numero3} es el mayor que {numero1} y {numero2}")
    
    return mensaje

numero1 = int(input('Introduce numero 1: '))
numero2 = int(input('Introduce numero 2: '))
numero3 = int(input('Introduce numero 3: '))

print(mayorDe3(numero1, numero2, numero3))

