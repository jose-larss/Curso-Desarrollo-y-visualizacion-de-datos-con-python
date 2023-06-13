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


