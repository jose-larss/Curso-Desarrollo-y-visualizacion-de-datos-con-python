"""
AÑO BISIESTO

    • Solicitar por teclado que el usuario introduzca un número.
    • Mostraremos en pantalla si el año introducido es bisiesto.

Para calcular si un año es bisiesto:

        ◦ Paso 1: Debe ser divisible por 4 (al dividirlo por cuatro el resto dará cero)
        ◦ Paso 2: Además de ser divisible por 4 no debe ser divisible por 100(que el resto no sea cero), excepto que también sea divisible por 400(que el resto sea cero).
"""
print('------------------------COMPROBANDO AÑO----------------------------------------')
bisiesto = int(input('Introduzca año, para ver si es Bisiesto: '))

if len(str(bisiesto)) == 4:
    if bisiesto % 4 == 0 and bisiesto % 100 != 0:
            
        print(f"Enhorabuena! El año {bisiesto} es BISIESTO")

    else:
        print(f"El año {bisiesto} es INCORRECTO")
else:
    print('AÑO INCORRECTO!, DEBE TENER 4 DIGITOS')