"""

    • Vamos a crear una serie de aplicaciones sencillas con error.
    • Incluir control de excepciones para controlar posibles errores en tiempo de ejecución.
    • Mostrar en pantalla información al usuario con el motivo del error.




1.- Crear una lista con los premios obtenidos en el euromillón. Incluiremos de mayor a menor los importes en euros que debe cobrar cada acertante.
"""

premios = [166116.06, 133948.48, 32353.28, 1528.28, 123.13, 66.37, 44.89, 15.91]

try: 
    premio = int(input('Introduce el numero de premio a mostrar: '))
    print(f"El premio correspondiente a {premio} es: {premios[premio]}")
except IndexError:
    print('ERROR MO HAY NINGUN PREMIO PARA ESTE NUMERO')
except ValueError:
    print('ERROR TIENES QUE INTRODUCIR VALOR NUMERICO')


