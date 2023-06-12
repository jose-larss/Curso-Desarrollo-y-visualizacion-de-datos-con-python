"""
Los sets en Python son una estructura de datos usada para almacenar elementos de una manera similar a las listas, pero con ciertas diferencias.

Los set en Python son un tipo que permite almacenar varios elementos y acceder a ellos de una forma muy similar a las listas pero con ciertas diferencias:

    Los elementos de un set son único, lo que significa que no puede haber elementos duplicados.
    Los set son desordenados, lo que significa que no mantienen el orden de cuando son declarados.
    Sus elementos deben ser inmutables.

Para entender mejor los sets, es necesario entender ciertos conceptos matemáticos como la teoría de conjuntos.

Para crear un set en Python se puede hacer con set() y pasando como entrada cualquier tipo iterable, como puede ser una lista.
Se puede ver como a pesar de pasar elementos duplicados como dos 8 y en un orden determinado, al imprimir el set no conserva ese 
orden y los duplicados se han eliminado.
"""

s = set([5, 4, 6, 8, 8, 'hola'])
print(s)       
print(type(s)) #<class 'set'>
print(4 in s)

for item in s:
    print(item)

#tambien se puede hacer asi
s = {5, 4, 6, 8, 8, 1}
print(s)       #{1, 4, 5, 6, 8}
print(type(s)) #<class 'set'>

# Union de set com operador |

s1 = set([1, 2, 3])
s2 = set([3, 4, 5])
print(f"Este es el SET unido: {s1 | s2}") #{1, 2, 3, 4, 5}

"""
Métodos sets
s.add(<elem>)

El método add() permite añadir un elemento al set.
"""

l = set([1, 2])
print(l)
l.add(3)
print(f"Añadimos elemento: {l}") #{1, 2, 3}

"""
s.remove(<elem>)

El método remove() elimina el elemento que se pasa como parámetro. Si no se encuentra, se lanza la excepción KeyError.
"""

s = set([1, 2])
print(s)
s.remove(2)
print(f"Eliminamos elemento por valor: {s}") #{1}

"""
s.discard(<elem>)

El método discard() es muy parecido al remove(), borra el elemento que se pasa como parámetro, y si no se encuentra no hace nada.
"""

s = set([1, 2])
s.discard(3)
print(s) #{1, 2}

"""
s.pop()

El método pop() elimina un elemento aleatorio del set.
"""

s = set([1, 2])
s.pop()
print(s) #{2}

"""
s.clear()

El método clear() elimina todos los elementos de set.
"""

s = set([1, 2])
s.clear()
print(s) #set()

s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1,s2)
print(f" La union es: {s1.union(s2)}") #{1, 2, 3, 4, 5}


s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1,s2)
print(f"La interseciones: {s1.intersection(s2)}") #{3}