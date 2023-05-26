"""
Solicita al usuario dos fechas del mismo año e indica la cantidad de días que hay entre ellas.
"""
"""
from datetime import datetime

fecha1 = datetime.strptime("2021-1-25", "%Y-%m-%d")
fecha2 = datetime.strptime("2021-10-31", "%Y-%m-%d")

if fecha1.year == fecha2.year:

    diferencia = fecha2-fecha1
    print(f"La diferencia es de {diferencia.days} días y {diferencia.seconds} segundos. La diferencia total es de {diferencia.total_seconds()} segundos")
else:
    print(f'Los años tienen que ser iguales {fecha1.year} - {fecha2.year}')
"""
"""
Ejemplo: fecha1 : 10/02/23 // fecha2: 10/08/23
"""

fecha1 = input('Introduce una fecha 1 (DIA/MES/AÑO):')
fecha2 = input('Introduce una fecha 2 (DIA/MES/AÑO):')

yearFecha1 = fecha1[6] + fecha1[7]
yearFecha2 = fecha2[6] + fecha2[7]

if yearFecha1 == yearFecha2:
    dia1Fecha1 = yearFecha1[0] + yearFecha1[1]
    dia2Fecha2 = yearFecha2[0] + yearFecha2[1]
    mes1Fecha1 = fecha1[3] + fecha1[4]
    mes2Fecha2 = fecha2[3] + fecha2[4]

    #vamos a pasar a dias los meses
    contadorDiasFecha1 = 0

    for i in range(int(mes1Fecha1)):
        if i == 1 or i== 3 or i == 5 or i == 7 or i == 9 or i == 11:
            contadorDiasFecha1 += 31
        elif i == 2:
            contadorDiasFecha1 += 28
        else:
            contadorDiasFecha1 += 30
    dias_totales_fecha1 = contadorDiasFecha1 + int(dia1Fecha1)

    #vamos a pasar a dias los meses
    contadorDiasFecha2 = 0

    for i in range(int(mes2Fecha2)):
        if i == 1 or i== 3 or i == 5 or i == 7 or i == 9 or i == 11:
            contadorDiasFecha2 += 31
        elif i == 2:
            contadorDiasFecha2 += 28
        else:
            contadorDiasFecha2 += 30
    dias_totales_fecha2 = contadorDiasFecha2 + int(dia2Fecha2)

    dias_entre_ambos = dias_totales_fecha1 - dias_totales_fecha2
    print(f'Los dias totales que van desde {fecha1} y {fecha2} son {dias_entre_ambos}')

else:
    print('Los años tienen que ser IGUALES')


