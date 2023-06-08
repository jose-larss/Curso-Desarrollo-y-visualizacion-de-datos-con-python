"""
Crea una variable que sea una letra, si es una a muestra el número 7, si es una b, 
el 9, si es una c el 101 y si no es ninguno de los tres, indica que se han equivocado de letra
"""

letter = 'a'

def letras(letter):
    if letter == 'a':
        msj = f'La letra es {letter} te muestro un 7'
    elif letter == 'b':
        msj = f'La letra es {letter} te muestro un 9'
    elif letter == 'c':
        msj = f'La letra es {letter} te muestro un 101'
    else:
        msj = 'Te has equivocado de letra'
    return msj

print(letras(letter))