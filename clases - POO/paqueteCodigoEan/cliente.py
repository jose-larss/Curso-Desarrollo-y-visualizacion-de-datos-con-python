from claseEan import CodigoEan

cliente = CodigoEan()
try:
    numero = int(input('Introduzca un numero EAN (8 o 13 caracteres): '))
    mensaje = cliente.funcionEan(numero)
    print(mensaje)
except ValueError:
    print('Value Error, Introduce números')




