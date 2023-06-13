"""
    • Dentro de un mismo tipo de objetos (por ejemplo, las bicicletas), existe una variedad de modelos 
    (normales, de carreras, de montaña, etc) que dificulta la definición de la clase genérica. Por ejemplo, 
    si defino los métodos subir_marcha() y bajar_marcha(), este método sólo se podrá aplicar a aquellas bicicletas 
    que tengan cambios.

    • Para resolver este tipo de problemas, la programación orientada a objetos hace uso de la herencia. 
    La herencia consiste en definir una clase a partir de otra ya existente. De esta forma podemos definir 
    una bicicleta genérica y mediante herencia crear otras clases más especializadas que respondan a las necesidades de 
    cada tipo de bicicleta. Se puede observar el ahorro que supone a la hora de escribir código. Por ejemplo:
"""
from claseBicicleta import Bicicleta, BicicletaCarreras

mibici = BicicletaCarreras()
print ("Velocidad: ",mibici.velocidad)
mibici.subirmarcha()
mibici.subirmarcha()
print ("Marcha: ",mibici.marcha)
mibici.bajarmarcha()
print ("Marcha: ",mibici.marcha)
mibici.subirvelocidad()
print ("Velocidad: ",mibici.velocidad)
mibici.cambiarVelMax(25)
print ("Velocidad máxima: ",mibici.Vel_max)
mibici.velocidadMaximaAutopista()
print ("Velocidad máxima en autopista: ",mibici.Vel_max)