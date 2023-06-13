
class Coche():

    """
    #Atributos / Propiedades
    color = "rojo"
    marca = "ferrari"
    modelo = "aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2
    """
    # Este es el CONSTRUCTOR
    
    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):

        #Atributos / Propiedades
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas
        self.soyAtribPublico = "soy un atributo publico"
        self.__soyAtribPrivado = "soy atributo privado"
      
    # GETTER = Acceden al dato / lo muestran  
    # SETTER = Asignan valores / datos

    #Modificar los valores de las propiedades/atributos del coche SETTER
    def setColor(self, color):
        self.color = color

    def setModelo(self, modelo):
        self.modelo = modelo

    def setMarca(self, marca):
        self.marca = marca

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1
    #Saca / muestra los valores de las propiedades/atributos del coche GETTER
    def getColor(self):
        return self.color

    def getModelo(self):
        return self.modelo

    def getMarca(self):
        return self.marca

    def getVelocidad(self):
        return self.velocidad
    # Definir metodo para acceder a atributos privados
    def getPrivado(self):
        return self.__soyAtribPrivado
    # Metodos / Funciones 
    def getInfo(self):
        info = ""
        info += "\n Color: " + self.getColor() 
        info += "\n Marca: " + self.getMarca() 
        info += "\n Modelo: " + self.getModelo()
        info += "\n Velocidad: " + str(self.getVelocidad())
        return info
    
    #Fin definicion de una clase

#Crear un Objeto / Instancia de la clase

coche1 = Coche("amarillo", "renault", "clio", 150,200, 4)
coche2 = Coche("verde", "seat", "panda", 240,200, 4)
coche3 = Coche("azul", "citroen", "xsara", 100,180, 4)
coche4 = Coche("rojo", "mercedes", "clase A", 350,400, 5)



print(type(coche4))

print(coche4.soyAtribPublico)
print(coche4.getPrivado())
"""
print(coche.marca)
print(f"la velocidad actual es {coche.velocidad}")
coche.acelerar()
print("Velocidad actual", coche.velocidad)
"""
print("-----------------------------------")
#coche.setColor("amarillo")
#coche.setModelo("murcielago")
#print(coche.getColor(), coche.getModelo())
print(coche1.getInfo())
print("************************************")
print(coche2.getInfo())
print("************************************")
print(coche3.getInfo())
print("************************************")
print(coche4.getInfo())


"""
print("************************************")
coche2 = Coche()
coche2.setColor("verde")
print(f"El coche 2 es de color: {coche2.getColor()}, modelo: {coche2.getModelo()}")
"""