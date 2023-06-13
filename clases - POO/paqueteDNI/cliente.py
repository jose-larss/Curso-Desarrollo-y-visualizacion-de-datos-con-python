from claseDni import Dni


print('***************************************INTRODUCE TU DNI Y TE DIGO QUE LETRA TE PERTENECE***********************************')
print('***************************************************************************************************************************')

usuario1 = Dni()

dni = int(input('Introduce tu DNI: '))
usuario1.get_letraDni(dni)

"""
print('*****************************INTRODUCE TU DNI Y TE DIGO QUE LETRA TE PERTENECE SUBSTRING***********************************')
print('***************************************************************************************************************************')

usuario2 = Dni()

dni = int(input('Introduce tu DNI: '))
print(usuario2.get_DNI_sbstring(dni))

"""