from claseDni import Dni


print('***************************************INTRODUCE TU DNI Y TE DIGO QUE LETRA TE PERTENECE***********************************')
print('***************************************************************************************************************************')



usuario1 = Dni()

dni = int(input('Introduce tu DNI: '))

print(usuario1.get_letraDni(dni))
