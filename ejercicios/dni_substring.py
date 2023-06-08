print('***************************************INTRODUCE TU DNI Y TE DIGO QUE LETRA TE PERTENECE***********************************')
print('***************************************************************************************************************************')

dni = int(input('Introduce tu DNI: '))
resultado = dni % 23
letrasDNI = 'TRWAGMYFPDXBNJZSQVHLCKET'

letra = letrasDNI[resultado]
print("la letra de tu DNI : ",letra)