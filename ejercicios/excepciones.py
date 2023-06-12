"""
Python implementa excepciones con el propósito de conseguir código robusto. 
Cuando ocurre un error en un programa, el código que encuentra el error lanza 
una excepción que se puede capturar desde la aplicación con el propósito de recuperarse de ella. 

"""
def controlErrores():
    
    try:
        numero = int(input("Introduce número:"))
        print("Número:",numero)
    except ValueError:
        print(f'error estas introduciendo un numero no entero:')
        controlErrores()

controlErrores()