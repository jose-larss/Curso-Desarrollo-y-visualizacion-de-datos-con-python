"""
Permite validar a un usuario con 3 intentos y los datos de validación correctos almacenados en dos constantes predefinidas.
"""

USER = 'jose'
PASSWORD = 1234
contador = 0

while contador < 3:
    name = input('Introduce usuario: ')
    password = input('Introduce Password: ')

    if name == USER and password == PASSWORD:
        print(f'El usuario {name} es correcto!! VALIDACION OK')
    else:
        print('usuario incorrecto!! Repite de nuevo')

    contador += 1
else:
    print('has agotado los intentos intentalo de nuevo!!')
