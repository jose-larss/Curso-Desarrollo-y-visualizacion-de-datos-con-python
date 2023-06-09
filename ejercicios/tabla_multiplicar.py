"""
Realizar una página que muestre la tabla de multiplicar del número introducido.
"""
numero = int(input('Introduce numero y te calculo la tabla: '))

print(f'**********La tabla de {numero}: ********************')
for indice in range(1,11):
    
    print(f'{numero} x {indice} = {numero * indice}')


"""
print("--------------TABLA DE MULTIPLICAR------------")

mult=int(input("Introduzca un número:"))
imprimir="\n"
for i in range(1,11):
    imprimir = imprimir + str(mult) + " * " + str(i) + " = " + str(mult * i) + "\n"

print(f"Resultado Tabla {imprimir} ")
"""