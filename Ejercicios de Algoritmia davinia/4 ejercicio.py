"""
Permite validar a un usuario con 3 intentos y los datos de validación correctos almacenados en dos constantes predefinidas.
"""

USER = 'jose'
PASSWORD = 1234
contador = 0
flag = False #variable para controlar si un user es correcto se cambia a True

while contador < 3:
    
        name = input('Introduce usuario: ')
        try:
            password = int(input('Introduce Password: '))
        except ValueError:
            print('La password tiene que ser Numérica')

        if name == USER and password == PASSWORD:
            print(f'El usuario {name} es correcto!! VALIDACION OK')
            flag = True
        else:
            print('usuario incorrecto!! Repite de nuevo')

        contador += 1
        if contador == 3 and flag == False:
            print('has agotado los intentos intentalo de nuevo!!')


