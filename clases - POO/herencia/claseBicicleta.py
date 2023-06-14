class Bicicleta:
    color = ""
    tamanio = ""
    Vel_max=15
    velocidad=-1
    def __init__(self):
        self.velocidad = 0

    def subirvelocidad (self):
        self.velocidad = self.velocidad + 1
    def bajarvelocidad(self):
        self.velocidad = self.velocidad - 1
    # setter
    def cambiarVelMax(self,maxVel):
        self.Vel_max = maxVel

class BicicletaCarreras(Bicicleta):
    marcha=0
    def subirmarcha(self):
        self.marcha = self.marcha + 1
    def bajarmarcha(self):
        self.marcha = self.marcha - 1
    def velocidadMaximaAutopista(self):
        super().cambiarVelMax(120)
        print(self.Vel_max)
        self.cambiarVelMax(200)

"""
bicicleta = Bicicleta()
bicicleta.subirvelocidad()
bicicleta.subirvelocidad()
bicicleta.subirvelocidad()
bicicleta.subirvelocidad()
print(bicicleta.velocidad)
bicicleta.cambiarVelMax(100)
print(bicicleta.Vel_max)
"""
biciCarreras1 = BicicletaCarreras()
biciCarreras1.cambiarVelMax(100)
print(biciCarreras1.Vel_max)
biciCarreras1.velocidadMaximaAutopista()
print(biciCarreras1.Vel_max)