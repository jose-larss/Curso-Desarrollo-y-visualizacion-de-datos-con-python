"""
FUNCIONES EN PYTHON

En Python podemos crear funciones utilizando la palabra reservada “def” seguido del nombre la función. 
Las funciones se pueden crear en cualquier lugar de un programa.

Imaginemos que en muchos bloques de código necesitamos añadir IVA a los precios de nuestros productos. Lo ideal sería crear una función par no repetir ese código en varios puntos.

En el siguiente ejemplo crearemos una función donde pediremos el precio de un producto y añadiremos el 21% de Iva al precio introducido.
"""

def calcularIVA():
    importe = int(input("Precio del producto: "))
    total = importe* 1.21
    print (f"IVA incluido (21%): {total}")
    return

print("LLAMANDO A LA FUNCIÓN")
calcularIVA()


def calcularIVA(importe):
    print (f"Precio del producto: {importe}")
    total = importe* 1.21
    print (f"IVA incluido (21%): {total}")
    return

print("LLAMANDO A LA FUNCIÓN")
calcularIVA(600)

def calcularIVA(importe):
    total = importe* 1.21
    return importe,total


print("LLAMANDO A LA FUNCIÓN")
precio,result=calcularIVA(2000)

print(f"Precio del producto: {precio}")
print(f"IVA incluido (21%): {result}")