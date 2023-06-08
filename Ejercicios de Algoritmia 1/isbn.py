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
contador = 1

for caracter in isbn:
    linea = int(caracter) * contador
    
    resultado += int(linea)
    print(resultado)
    contador += 1

print(resultado / 11)

 
