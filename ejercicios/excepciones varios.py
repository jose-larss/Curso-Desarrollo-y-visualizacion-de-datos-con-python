"""
Dentro del bloque “try” se pueden producir varios errores, por ese motivo 
Python nos permite incluir varios bloques “except”, para capturar diferentes excepciones.

En el siguiente ejemplo realizaremos una división de dos números, controlando que se 
introduzcan número y que el divisor no sea cero.
"""
"""
def controlErrores():
    try:
        dividendo = int(input("Introduce dividendo:"))
        divisor = int(input("Introduce divisor:"))
        resultado = dividendo / divisor
        print(f"Resultado división: {resultado}")
    except ValueError:
        print("Error, debes introducir un número")
    except ZeroDivisionError:
        print("¡¡¡Error!!!. El divisor no puede ser cero")

controlErrores()
"""
"""
Se puede utilizar la sentencia except sin especificar ningún nombre de excepción para 
captura cualquier tipo de error.

Modificamos el ejemplo anterior para que entre en la excepción ValueError o ZeroDivisionError si 
se producen sus respectivos errores, pero si se produce cualquier otro entrará en el último except.
"""
import sys

def controlErrores():
    try:
        dividendo = int(input("Introduce dividendo:"))
        divisor = int(input("Introduce divisor:"))
        resultado = dividendo / divisor
        print(f"Resultado división: {resultado}")
    
    except ValueError:
        print("Error, debes introducir un número")
    except ZeroDivisionError:
        print("¡¡¡Error!!!. El divisor no puede ser cero")
    except:
        #Este fragmento muestra el error en si, específicamente
        print(f"Error general {sys.exc_info()}")


controlErrores()

