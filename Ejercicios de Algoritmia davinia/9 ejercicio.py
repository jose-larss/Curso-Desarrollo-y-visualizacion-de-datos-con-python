"""
Ejercicio Cambio

Disponemos en la caja del siguiente dinero distribuido de la siguiente manera: 234,27 € 
(información que se debe cargar en un array)

    - Billetes de 500€: 0
    - Billetes de 200€: 0
    - Billetes de 100€: 0
    - Billetes de 50€: 1
    - Billetes de 20€: 4
    - Billetes de 10€: 8
    - Billetes de 5€: 2
    - Monedas de 2€: 5
    - Monedas de 1€: 4
    - Monedas de 0.50€: 0
    - Monedas de 0.20€: 0
    - Monedas de 0.10€: 1
    - Monedas de 0.05€: 2
    - Monedas de 0.02€: 3
    - Monedas de 0.01€: 1

El programa obtiene un precio de artículo y un importe pagado desglosado 
(se deben conocer las cantidades entregadas de todos los billetes y monedas) 
y responderá si no hay cambio, si está justo o si se devuelve cambio, de nuevo con 
el desglose que debe ser lo más óptimo (es decir, si puedo devolver un billete de 20, 
no devuelvo 2 de 10, por ejemplo).

Debemos mostrar al final el desglose del cambio y el nuevo estado de la caja.

Ejemplo: articulo vale: 138.53  y pago 140 // 
1 - conocer la cantidad entregada de todos los billetes
2 - Recibiremos (si no hay cambio/si esta justo/si se devuelve cambio (de la manera mas optima))
"""
#import math 
"""
caja = [
    (500,0),
    (200,0),
    (100,0),
    (50,1),
    (20,4),
    (10,8),
    (5,2),
    (2,5),
    (1,4),
    (0.50,0),
    (0.20,0),
    (0.10,1),
    (0.05,2),
    (0.02,3),
    (0.01,1),
]


print('**********************************')
#price = float(input('Introduce precio del Articulo: 138.38: '))
#pagado = float(input('Introduce el importe que pagas: 140: '))
print('**********************************')

price = 138.38
dinero_pagado = 140.01

a_devolver = dinero_pagado - price
#redondeo a 2 decimales
a_devolver = round(a_devolver,2)

lista_tupla_dinero_pagado = []
for item_dinero in caja:
    if item_dinero[0] <= dinero_pagado:
        lista_intermedia = []
        lista_intermedia.append(item_dinero[0])
        lista_intermedia.append(1)

        tupla = tuple(lista_intermedia)

        lista_tupla_dinero_pagado.append(tupla)

        dinero_pagado -= item_dinero[0]
        #redondeo a 2 decimales
        dinero_pagado = round(dinero_pagado,2)
        #print(dinero_pagado)
        #hacer que entre al elemento de la caja actual, para ver si necesita 2 monedas iguales
        if item_dinero[0] <= dinero_pagado:
            lista_intermedia = []
            lista_intermedia.append(item_dinero[0])
            lista_intermedia.append(1)

            tupla = tuple(lista_intermedia)

            lista_tupla_dinero_pagado.append(tupla)

            dinero_pagado -= item_dinero[0]


#ahora procedo a sumar cantidades de una modena igual
diccionario = {}
for elemento in lista_tupla_dinero_pagado:
    if elemento[0] not in diccionario:
        diccionario[elemento[0]] = elemento[1]
    else:
        diccionario[elemento[0]] += elemento[1]

print(diccionario)

string = ""
for key, value in diccionario.items():
    string += f' {value} de {key}' 

print(f'He pagado este dinero: {string}')

print(f'Me tienen que devolver esto: {a_devolver}')

lista_tupla_dinero_devuelto = []
for item_dinero in caja:
    if item_dinero[0] <= a_devolver:
        #aqui controlo que haya la cantidad suficiente de este dinero, para devolver
        if item_dinero[1] > 0:
            lista_intermedia = []
            lista_intermedia.append(item_dinero[0])
            lista_intermedia.append(1)

            tupla = tuple(lista_intermedia)

            lista_tupla_dinero_devuelto.append(tupla)

            a_devolver -= item_dinero[0]
            #redondeo a 2 decimales
            a_devolver = round(a_devolver,2)
            #print(dinero_pagado)
            #hacer que entre al elemento de la caja actual, para ver si necesita 2 monedas iguales
            if item_dinero[0] <= a_devolver:
                #aqui controlo que haya la cantidad suficiente de este dinero, para devolver
                if item_dinero[1] > 0:
                    lista_intermedia = []
                    lista_intermedia.append(item_dinero[0])
                    lista_intermedia.append(1)

                    tupla = tuple(lista_intermedia)

                    lista_tupla_dinero_devuelto.append(tupla)

                    a_devolver -= item_dinero[0]

print(f'El dinero a devolver es: {lista_tupla_dinero_devuelto}')
"""     
caja = [
    [500,0],
    [200,0],
    [100,0],
    [50,1],
    [20,4],
    [10,8],
    [5,2],
    [2,5],
    [1,4],
    [0.50,0],
    [0.20,0],
    [0.10,1],
    [0.05,2],
    [0.02,3],
    [0.01,1],
]


print('**********************************')
#price = float(input('Introduce precio del Articulo: 138.38: '))
#pagado = float(input('Introduce el importe que pagas: 140: '))
print('**********************************************************************************')
print(f'La caja INICIAL es:')
print('**********************************************************************************')
for item in caja:
    print(f"{item[0]} €: {item[1]} uds")
print('**********************************************************************************')
print('**********************************************************************************')
price = 278.76
dinero_pagado = 440.70

a_devolver = dinero_pagado - price
#redondeo a 2 decimales que luego voy restando
a_devolver = round(a_devolver,2)

lista_tupla_dinero_pagado = []
for item in caja:
    
    if item[0] <= dinero_pagado:

        lista_intermedia = []
        lista_intermedia.append(item[0])
        lista_intermedia.append(1)

        tupla = tuple(lista_intermedia)

        lista_tupla_dinero_pagado.append(tupla)

        dinero_pagado -= item[0]
        #redondeo a 2 decimales
        dinero_pagado = round(dinero_pagado,2)

        #hacer que entre al elemento de la caja actual, para ver si necesita 2 monedas iguales
        if item[0] <= dinero_pagado:
            lista_intermedia = []
            lista_intermedia.append(item[0])
            lista_intermedia.append(1)

            tupla = tuple(lista_intermedia)

            lista_tupla_dinero_pagado.append(tupla)

            dinero_pagado -= item[0]



#ahora procedo a sumar cantidades de una modena igual
diccionario = {}
for elemento in lista_tupla_dinero_pagado:
    if elemento[0] not in diccionario:
        diccionario[elemento[0]] = elemento[1]
    else:
        diccionario[elemento[0]] += elemento[1]


string = ""
for key, value in diccionario.items():
    string += f' {value} uds de {key} euros, \n' 

print('**********************************************************************************')
print(f'He pagado este dinero: \n{string}')
print('**********************************************************************************')

print(f'Me tienen que devolver: {a_devolver} €')
print('**********************************************************************************')
total_a_devolver = a_devolver
lista_tupla_dinero_devuelto = []
# Recorro array Bi, item a item
for item in caja:
    # Aqui recorro el valor/la cantidad de moneda de la misma
    for j in range (item[1]):

        if item[0] <= a_devolver and item[1] > 0:

            lista_intermedia = []
            lista_intermedia.append(item[0])
            lista_intermedia.append(1)

            tupla = tuple(lista_intermedia)

            lista_tupla_dinero_devuelto.append(tupla)

            a_devolver -= item[0]
            #redondeo a 2 decimales
            a_devolver = round(a_devolver,2)
                            
            #Restamos de la caja
            item[1] -= 1
                           
#ahora procedo a sumar cantidades de una modena igual
diccionario = {}

for elemento in lista_tupla_dinero_devuelto:
    if elemento[0] not in diccionario:
        diccionario[elemento[0]] = elemento[1]
    else:
        diccionario[elemento[0]] += elemento[1]

string = ""
total_dev = 0
for key, value in diccionario.items():
    total_dev += key * value
    string += f' {value} uds de {key} € \n' 

print('**********************************************************************************')
print(f'Me devuelven este dinero: \n{string}')
print('**********************************************************************************')
total_dev = round(total_dev,2)
print(f'El total de la devolucion es: {total_dev} €')

if  total_a_devolver > total_dev:
    print('NO HAY CAMBIO')
elif total_a_devolver == total_dev:
    print('EL CAMBIO ESTA JUSTO')
elif total_a_devolver < total_dev:
    print('ENHORABUENA, SE DEVUELVE CAMBIO')

print('**********************************************************************************')
print(f'La caja FINAL es:')
print('**********************************************************************************')
for item in caja:
    print(f"{item[0]} €: {item[1]} uds")
print('**********************************************************************************')
print('**********************************************************************************') 
