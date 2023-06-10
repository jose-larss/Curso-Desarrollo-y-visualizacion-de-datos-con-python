"""
CALCULAR DIA DE NACIMIENTO DE LA SEMANA
Pedir una fecha al usuario para calcular el día de la semana que nació.  Tenemos que tener la tabla de días de la semana para la correspondencia comenzando en sábado:
DIA
NÚMERO
Sábado
0
Domingo
1
Lunes
2
Martes
3
Miércoles
4
Jueves
5
Viernes
6

Debemos pedir el día, el número de mes y el año que el usuario haya nacido.
A partir de esto datos hay que calcular lo siguiente para averiguar el día de la semana de nacimiento:
Ejemplo  15/06/1997

Hay que tener en cuenta el mes para realizar el cálculo, si el mes es Enero, el Mes será 13 y restaremos uno al año. Si el Mes es Febrero, el Mes será 14 y restaremos uno al año.
 
Para poder calcular las el número final de la semana debemos seguir los siguientes pasos:

    1. Multiplicar el Mes más 1 por 3 y dividirlo entre 5

 ((6 + 1) * 3) / 5   4

    2. Dividir el año entre 4
  1997 / 4   499

    3. Dividir el año entre 100

  1983 / 100  19

    4. Dividir el año entre 400

  1983 / 400  4

    5. Sumar el dia, el doble del mes, el año, el resultado de la operación 1, el resultado de la operación 2, menos el resultado de la operación 3 más la operación 4 más 2.

  15 + (6 * 2) + 1997 + 4 + 499 - 19 + 4 + 2  2514

    6. Dividir el resultado anterior entre 7.

  2514 / 7  359

    7. Restar el número del paso 5 con el número del paso 6 por 7.

 	  2514 – (359 * 7)  1

    8. Miramos la tabla y vemos que el número 1 corresponde a DOMINGO
"""

print("-----CALCULO DÍA DE NACIMIENTO-----")
dia = int(input('Introduzca su dia de nacimiento:'))
mes = int(input('Introduzca su mes de nacimiento:'))
anio = int(input('Introduzca su año de nacimiento:'))
diasSemana=('Sábado','Domingo','Lunes','Martes','Miércoles','Jueves','Viernes')
if mes == 1:
  mes = 13
  anio-= 1
elif mes == 2:
  mes = 14 
  anio-=1

paso1 = int(((mes + 1) * 3) / 5)
paso2 = int(anio / 4)
paso3 = int(anio / 100)
paso4 = int(anio / 400)
paso5 = int(dia + 2 * mes + anio + paso1 + paso2 - paso3 + paso4 + 2)
paso6 = int(paso5 / 7)
resultadoFinal = int(paso5 - paso6 * 7)
print('Su día de nacimiento fué:', diasSemana[resultadoFinal])


"""
tupla = ('sabado', 
         'domingo', 
         'lunes', 
         'martes', 
         'miercoles', 
         'jueves', 
         'viernes')

fecha = input('Dime tu fecha de nacimiento 15/06/1997 con este formato: ')

dia = fecha[0] + fecha[1]
mes = fecha[3] + fecha[4]
anno = fecha[6] + fecha[7] + fecha[8] + fecha[9]

print(dia)
print(mes)
print(anno)

operacion1 = ((int(mes) + 1) * 3) / 5  
print(f'la operacion mes es {operacion1}')
operacion2 = int(anno) / 4
print(f'La operacion de anno es {operacion2}')
operacion3 = int(anno) / 100
print(f'La operacion de anno / 100 es {operacion3}')
operacion4 = int(anno) / 400
print(f'La operacion de anno / 400 es {operacion4}')

operacion5 = int(dia) + (int(mes) * 2) + int(anno) + operacion1 + operacion2 - operacion3 + operacion4 + 2

operacion6 = operacion5 / 7

operacion7 = operacion5 - (operacion6 * 7)

print(f'El numero final es: {round(operacion7)}')

for i in range (len(tupla)):
    
    if i == operacion7:
        print(tupla[i])
"""  
