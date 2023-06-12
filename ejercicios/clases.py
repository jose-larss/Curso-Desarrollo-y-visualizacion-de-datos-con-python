"""
TEORIA
    • En Python se define una clase con la palabra reservada class seguido del nombre la clase.
 
    class Nombre
	Propiedades y métodos de la clase



    • El constructor en Python se define con el método __init__ 

    • Las propiedades o atributos de una clase en Python serán las variables.

    • Las acciones o comportamiento conocidos en POO como métodos, en Python serán las funciones.

    • Todos los métodos tienen de primer parámetro uno que se llama self. Será una referencia a la instancia del objeto.
"""

"""
Automaticamente al instaciar una clase, procede lo primero con el metodo __init__ constructor
"""

class Bicicleta:
    
    color = ""
    tamanio = ""
    Vel_max = 15
    velocidad = -1
    
    def __init__(self):
       self.velocidad = 0
    def subirmarcha (self):
        self.velocidad = self.velocidad + 1
    def bajarmarcha(self):
        self.velocidad = self.velocidad - 1
    def cambiarVelMax(self,maxVel):
        self.Vel_max = maxVel
    
    def __str__(self):
        #return f"{self.velocidad}"
        return "Velocidad Actual:" + str(self.velocidad) + " Velocidad Máxima: " + str(self.Vel_max)


mibici = Bicicleta()
print(mibici.velocidad)
mibici.subirmarcha()
mibici.subirmarcha()
print (mibici.velocidad)
mibici.bajarmarcha()
print (mibici.velocidad)
mibici.cambiarVelMax(25)
print (mibici.Vel_max)

#sobreescribe el metodo toostring de los lenguajes antiguos, si llamamos mibici a secas va al __str__
print(f"la variable miBici {mibici}")
