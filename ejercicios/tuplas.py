"""

Aunque la mayoría de los desarrolladores utilizan listas, vamos a entender que son las tuplas y cuando se pueden utilizar en Python.

Principal diferencia:

    • Las listas son dinámicas. Se puede modificar una vez creado (se le suele denominar objeto mutable) 
    • Las tuplas son estáticas. No se puede modificar una vez creado  (se le suele denominar objeto no mutable


Las tuplas al ser estáticas no tienen métodos para añadir, eliminar, modificar,…



    • Crear una tupla con productos de una compra.
    • Realizar operaciones sobre las tuplas para entender el funcionamiento.
"""

print("CREANDO TUPLAS DE CADENAS")
productos = ("Manzana", "Pera", "Naranja")
# A diferencias de las listas, las tuplas se declaran con paréntesis () y no con corchetes []

for item in productos:
    print(item)
print(len(productos))

print("Producto 1: ",productos[0])
print("Producto 2: ",productos[1])
print("Producto 3: ",productos[2])