from claseBicicleta import Bicicleta

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