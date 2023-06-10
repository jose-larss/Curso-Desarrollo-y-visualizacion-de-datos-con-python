"""
La serie Fibonacci es una famosa secuencia matemática en la que se representarían los siguientes números: 

1,1,2,3,5,8,13,21,...

Cada número es el resultado de la suma de los 2 números anteriores.

Por lo tanto, después de 1 y 1, el siguiente número es 1+1=2, el siguiente es 1+2=3, el siguiente es 2+3=5 y así continúa.

Realizar una aplicación en la que mostraremos la secuencia de Fibonacci hasta un número que el usuario nos indique.
"""

"""
numero = 9

fibonacci = 1
lista_fib = []
lista_fib.append(lista_fib)

for i in range (1,numero + 1):
    
    print(fibonacci)
    lista_fib.append(fibonacci[i] - fibonacci[i - 1])
    print()
"""
secuencia=int(input("Introduzca hasta que numero desea ver la secuencia: "))
num1 = 0
num2 = 1

suma = num1 + num2
print("SERIE FIBONACCI")
print("--------------------")
print(suma)
while suma < secuencia:
    num1 = num2
    num2 = suma
    print(suma)
    suma = num1 + num2;   

def fib(num):
    lista = []
    for i in range(num):
        if i == 0:
            lista.append(i)
        if i == 1:
            lista.append(i)
        if i > 1:
            lista.append((lista[i - 1])+(lista[i - 2]))
    return lista

lista = fib(15)
print(f"La serie completa es: {lista}")
print(f"El resultado de la serie es: {lista[-1]}")
#print(f"La serie completa es: {fib(15)}")
  
