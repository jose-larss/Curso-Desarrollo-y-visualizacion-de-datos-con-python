class Persona():
    """
    nombre
    apellidos
    altura
    edad
    """
    #GETTER
    def getNombre(self):
        return self.nombre

    def getApellidos(self):
        return self.apellidos

    def getAltura(self):
        return self.altura

    def getEdad(self):
        return self.edad
    #SETTER
    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellidos(self, apellidos):
        self.apellidos = apellidos

    def setAltura(self, altura):
        self.altura = altura

    def setEdad(self, edad):
        self.edad = edad
    #Funciones
    def hablar(self):
        return "Estoy hablando"
    
    def caminar(self):
        return "Estoy caminando"
    
    def dormir(self):
        return "Estoy durmiendo"

class Informatico(Persona):
    #hereda todos ls metodos y propiedades de persona
    def __init__(self):
        self.lenguajes = ("HTML, CSS, Javascript, PHP")
        self.experiencia = 5

    def getLenguajes(self):
        return self.lenguajes

    def setAprender(self,lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes

    def programar(self):
        return "Estoy Programando"

    def reparaPc(self):
        return "He reparado el PC"

class TecnicoRedes(Informatico):
    #hereda todos los metodos y propiedades de persona e informatico
    def __init__(self):
        super().__init__()
        self.auditarRedes = "experto"
        self.experiencia = 15

    def auditoria(self):
        return "Estoy auditando redes"

    
