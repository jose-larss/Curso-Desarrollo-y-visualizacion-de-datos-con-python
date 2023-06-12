"""
2.- Hemos creado un diccionario con los colores en castellano y la traducción en inglés.

Si solicitamos un colore existente, la aplicación funciona:

"""

colores = dict()

colores = {
    'amarillo':'yellow',
    'rosa':'pink',
    'azul':'blue',
    'blanco':'white',
    'rojo':'red',
}

"""
con get no salta ningún error

color = input('Introduce un COLOR: ')

print(colores.get(color))
"""
def func_colores():
    try:
        color = input('Introduce un COLOR: ')
        return f'Correcto el color existe {colores[color]}'

    except KeyError:
        colores.setdefault(color, color.upper())
        colores_ordenados = sorted(colores.items())

        print(colores_ordenados)
        return f'Enhorabuena el color introducido no existe, se INSERTA {colores}'
    
print(func_colores())




