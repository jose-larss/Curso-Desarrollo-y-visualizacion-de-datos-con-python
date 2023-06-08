"""
Dispones de frase y una letra, solicitados al usuario y debes mostrar la cantidad de veces que aparece la letra en la frase.
"""
"""
string = input('Introduce una frase: ')
letter = input('Introduce una letra para buscarla en la frase: ')
cont_letra = 0

for letra in string:
    if letra == letter:
        cont_letra += 1

print(f"La frase {string} tiene {cont_letra} veces la letra {letter}")
"""

def countLetter(string, letter):

    cont_letra = 0

    for letra in string:
        if letra == letter:
            cont_letra += 1

    return f"La frase {string} tiene {cont_letra} veces la letra {letter}"

string = input('Introduce una frase: ')
letter = input('Introduce una letra para buscarla en la frase: ')

print(countLetter(string, letter))