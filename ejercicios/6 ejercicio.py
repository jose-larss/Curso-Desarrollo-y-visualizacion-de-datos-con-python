"""
Dispones de tres números enteros H, M, S correspondientes a hora, minutos y segundos respectivamente, 
debes comprobar si se trata de una hora válida.
"""

HORA = 100
MINUTO = 70
SEGUNDOS = 89

if HORA < 25:
    print(f'La hora {HORA} es INVALIDA')
elif MINUTO < 61:
    print(f'Los minutos {MINUTO} No son correctos')
elif SEGUNDOS < 61:
    print(f'Los segundos {SEGUNDOS} No son correctos')

else:
    print('La hora es VALIDA!!!')