"""
Suma o resta dos números reales solicita la información al usuario
"""
"""
numero1 = int(input('Introduce el primer numero1: '))
numero2 = int(input('Introduce el primer numero2: '))

operacion = input('Que operación quieres realizar: (SUMA/RESTA) presiona q si quieres salir: ')


if operacion == 'SUMA':
    print(f'La suma de {numero1} + {numero2} = {numero1 + numero2}')
elif operacion == 'RESTA':
    print(f'La resta de {numero1} + {numero2} = {numero1 - numero2}')
"""

def operations(numero1, numero2, op):

    if op == 'SUMA':
        msj = f'La suma de {numero1} + {numero2} = {numero1 + numero2}'
    elif op == 'RESTA':
        msj = f'La resta de {numero1} + {numero2} = {numero1 - numero2}'
    else:
        msj = 'La OPERACION NO ES VALIDA!!'

    return msj

numero1 = int(input('Introduce el primer numero1: '))
numero2 = int(input('Introduce el primer numero2: '))

op = input('Que operación quieres realizar: (SUMA/RESTA) presiona q si quieres salir: ')

print(operations(numero1, numero2, op))
