"""
La serie Fibonacci es una famosa secuencia matemática en la que se representarían los siguientes números: 

1,1,2,3,5,8,13,21,...

Cada número es el resultado de la suma de los 2 números anteriores.

Por lo tanto, después de 1 y 1, el siguiente número es 1+1=2, el siguiente es 1+2=3, el siguiente es 2+3=5 y así continúa.

Realizar una aplicación en la que mostraremos la secuencia de Fibonacci hasta un número que el usuario nos indique.
"""

numero = 9

fibonacci = 1
lista_fib = []
lista_fib.append(lista_fib)

for i in range (1,numero + 1):
    
    print(fibonacci)
    lista_fib.append(fibonacci[i] - fibonacci[i - 1])
    print()
    
  
