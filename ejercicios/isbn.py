"""
    • Realizar una aplicación para comprobar si el ISBN introducido por teclado es válido.
    • Debemos comprobar que el número introducido tiene 10 caracteres.


EJEMPLO DE NUMERO ISBN CORRECTO:

8441513929

PARA SABER SI ES CORRECTO, EL ALGORITMO SE REALIZA DE LA SIGUIENTE MANERA:


1.- Se descompone la cadena y se multiplica cada número por la posición que ocupa en la cadena:

 8 * 1
 4 * 2
 4 * 3
 1 * 4
 5 * 5
 .
 .
 .
 9 * 10


2.- La suma de todas estas multiplicaciones se divide entre 11, y si el resto es cero, el número ISBN es correcto.
"""

isbn = '8441513929'
resultado = 0
print('------------------------VALIDANDO ISBN----------------------------------------')
isbn = input('Introduzca número ISBN: ')

if len(isbn) == 10:
    for i in range (len(isbn)):

        linea = int(isbn[i]) * (i + 1)
        resultado += linea
        
    resto = resultado % 11
    if resto == 0:
        print('CORRECTO')
    else:
        print('INCORRECTO')
else:
    print(f'Debe introducir un ISBN de 10 digitos, este tiene {len(isbn)}')

 
