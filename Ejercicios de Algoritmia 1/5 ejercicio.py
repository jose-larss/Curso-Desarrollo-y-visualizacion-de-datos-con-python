"""
Crea una variable que sea una letra, si es una a muestra el número 7, si es una b, 
el 9, si es una c el 101 y si no es ninguno de los tres, indica que se han equivocado de letra
"""

letter = 'u'

if letter == 'a':
    print(f'La letra es {letter} te muestro un 7')
elif letter == 'b':
    print(f'La letra es {letter} te muestro un 9')
elif letter == 'c':
    print(f'La letra es {letter} te muestro un 101')
else:
    print('Te has equivocado de letra')