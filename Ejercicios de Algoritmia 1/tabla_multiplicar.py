"""
Realizar una página que muestre la tabla de multiplicar del número introducido.
"""
numero = int(input('Introduce numero y te calculo la tabla: '))

print(f'**********La tabla de {numero}: ********************')
for indice in range(1,11):
    
    print(f'{numero} x {indice} = {numero * indice}')