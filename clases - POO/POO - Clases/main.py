import clases

persona1 = clases.Persona() #instancia de persona

# Usando Metodos Setter
persona1.setNombre("victor")
persona1.setApellidos("robles")
persona1.setAltura("190 cm")
persona1.setEdad(28)
#Usando metodos Getter
print(persona1.getNombre(), persona1.getApellidos(), persona1.getAltura(), persona1.getEdad())
print(persona1.hablar())

#FUNCIONAMIENTO DE LA HERENCIA INFORMATICO COMO OBJETO
informatico1 = clases.Informatico() #Creamos la instancia de informatico

informatico1.setNombre("jose")
informatico1.setApellidos("castro")
print(f"El informatico se llama: {informatico1.getNombre()} {informatico1.getApellidos()} sabe: {informatico1.getLenguajes()}")
print(informatico1.caminar())
print(informatico1.experiencia) #esto no es aconsejable aunque funcione, se deberia definir funcion getter

tecnico1 = clases.TecnicoRedes() #Instancia de tecnico redes
print(f"El tecnico de redes tiene experiencia de: {tecnico1.auditarRedes}")
tecnico1.setNombre("gustavo")
print(tecnico1.getNombre())
#tecnico1.setAprender("python")

# Para acceder a las propiedades como lenguajes, de la clase padre(Informatico) 
# necesito hacer que herede el metodo constructor la clase hija
print(tecnico1.getLenguajes()) 

tecnico2 = clases.TecnicoRedes()
print(f"El tecnico de redes2 sabe {tecnico2.reparaPc()} tiene {tecnico2.experiencia} experiencia, ademas de {tecnico2.auditarRedes}")


