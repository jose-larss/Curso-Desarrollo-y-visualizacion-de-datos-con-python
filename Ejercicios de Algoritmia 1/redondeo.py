print("--------------REDONDEANDO-------------")
#Ejemplo de redondeo, redondeo inferior y redondeo superior
num1=20
num2=3
resultado=round(num1/num2,2)

print("Resultado redondeado:",resultado)

""" Importamos de la biblioteca Math las funciones floor y ceil, de lo contrario
 no se podrán utilizar"""

from math import floor,ceil
#floor es siempre inferior
#ceil es siempre superior

resultado=floor(num1/num2)
print("Resultado redondeado al número inferior:",resultado)

resultado=ceil(num1/num2)
print("Resultado redondeado al número superior:",resultado)