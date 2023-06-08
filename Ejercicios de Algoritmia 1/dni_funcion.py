"""
CALCULAR LETRA DNI

    • Realizar una aplicación para conocer la letra del Documento Nacional de Identidad a través del número de DNI. 
    • Debe asegurarse de que en la caja DNI sólo se puedan introducir números y que no esté vacía.
    • La fórmula para calcular la letra del número del DNI se halla de la siguiente manera:
Se calcula el valor de la siguiente resta ( nº DNI - (Ent(nº DNI / 23) * 23)), tal que Ent es la función parte entera de un número.
    • Se mira la equivalencia en la siguiente tabla

0=T
4=G
8=P
12=N
16=Q
20=C
1=R
5=M
9=D
13=J
17=V
21=K
2=W
6=Y
10=X
14=Z
18=H
22=E
3=A
7=F
11=B
15=S
19=L
23=T

Para calcular la letra del DNI hayq ue peter el dni y aplicar el modulo 23

"""

def calcular_dni(numero):

    if resultado == 0:
        return 'T'
    elif resultado == 1:
        return 'T'
        print('La letra de tu DNI es: W', resultado)
    elif resultado == 3:
        return 'T'
        print('La letra de tu DNI es: A', resultado)
    elif resultado == 4:
        return 'T'
        print('La letra de tu DNI es: G', resultado)
    elif resultado == 5:
        return 'T'
        print('La letra de tu DNI es: M', resultado)
    elif resultado == 6:
        print('La letra de tu DNI es: Y', resultado)
    elif resultado == 7:
        return 'T'
        print('La letra de tu DNI es: F', resultado)
    elif resultado == 8:
        return 'T'
        print('La letra de tu DNI es: P', resultado)
    elif resultado == 9:
        return 'T'
        print('La letra de tu DNI es: D', resultado)
    elif resultado == 10:
        return 'T'
        print('La letra de tu DNI es: X', resultado)
    elif resultado == 11:
        return 'T'
        print('La letra de tu DNI es: B', resultado)
    elif resultado == 12:
        return 'T'
        print('La letra de tu DNI es: N', resultado)
    elif resultado == 13:
        return 'T'
        print('La letra de tu DNI es: J', resultado)
    elif resultado == 14:
        return 'T'
        print('La letra de tu DNI es: Z', resultado)
    elif resultado == 15:
        return 'T'
        print('La letra de tu DNI es: S', resultado)
    elif resultado == 16:
        return 'T'
        print('La letra de tu DNI es: Q', resultado)
    elif resultado == 17:
        return 'T'
        print('La letra de tu DNI es: V', resultado)
    elif resultado == 18:
        return 'T'
        print('La letra de tu DNI es: H', resultado)
    elif resultado == 19:
        return 'T'
        print('La letra de tu DNI es: L', resultado)
    elif resultado == 20:
        return 'T'
        print('La letra de tu DNI es: C', resultado)
    elif resultado == 21:
        return 'T'
        print('La letra de tu DNI es: K', resultado)
    elif resultado == 22:
        return 'T'
        
    elif resultado == 23:
        return 'T'
       


print('***************************************INTRODUCE TU DNI Y TE DIGO QUE LETRA TE PERTENECE***********************************')
print('***************************************************************************************************************************')

dni = int(input('Introduce tu DNI: '))
resultado = dni % 23

if resultado == 0:
    print('La letra de tu DNI es T: ', resultado)
elif resultado == 1:
    print('La letra de tu DNI es: R', resultado)
elif resultado == 2:
    print('La letra de tu DNI es: W', resultado)
elif resultado == 3:
    print('La letra de tu DNI es: A', resultado)
elif resultado == 4:
    print('La letra de tu DNI es: G', resultado)
elif resultado == 5:
    print('La letra de tu DNI es: M', resultado)
elif resultado == 6:
    print('La letra de tu DNI es: Y', resultado)
elif resultado == 7:
    print('La letra de tu DNI es: F', resultado)
elif resultado == 8:
    print('La letra de tu DNI es: P', resultado)
elif resultado == 9:
    print('La letra de tu DNI es: D', resultado)
elif resultado == 10:
    print('La letra de tu DNI es: X', resultado)
elif resultado == 11:
    print('La letra de tu DNI es: B', resultado)
elif resultado == 12:
    print('La letra de tu DNI es: N', resultado)
elif resultado == 13:
    print('La letra de tu DNI es: J', resultado)
elif resultado == 14:
    print('La letra de tu DNI es: Z', resultado)
elif resultado == 15:
    print('La letra de tu DNI es: S', resultado)
elif resultado == 16:
    print('La letra de tu DNI es: Q', resultado)
elif resultado == 17:
    print('La letra de tu DNI es: V', resultado)
elif resultado == 18:
    print('La letra de tu DNI es: H', resultado)
elif resultado == 19:
    print('La letra de tu DNI es: L', resultado)
elif resultado == 20:
    print('La letra de tu DNI es: C', resultado)
elif resultado == 21:
    print('La letra de tu DNI es: K', resultado)
elif resultado == 22:
    print('La letra de tu DNI es: E', resultado)
elif resultado == 23:
    print('La letra de tu DNI es: T', resultado)