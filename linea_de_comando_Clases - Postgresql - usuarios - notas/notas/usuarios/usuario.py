from conexion.conexion import conexion_BBDD
import datetime
import hashlib

connect = conexion_BBDD()
database = connect[0]
cursor = connect[1]

class Usuario:

    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def registrar(self):
        fecha = datetime.datetime.now()

        # Cifrado dee contraseña con haslih
        passCifrada = hashlib.sha256()
        passCifrada.update(self.password.encode('utf8'))

        usuario = (self.nombre, self.apellidos, self.email, passCifrada.hexdigest(), fecha)
        consulta = ("INSERT INTO usuarios (nombre, apellido, email, passw1, fecha) VALUES(%s, %s, %s, %s, %s)")

        try:
            cursor.execute(consulta, usuario)
            database.commit()
            return [cursor.rowcount, self]
        except:
            return [0,self]

    def identificarse(self):

        consulta = ("SELECT * FROM usuarios WHERE email = %s AND passw1 = %s")
        # Cifrado dee contraseña con haslih
        passCifrada = hashlib.sha256()
        passCifrada.update(self.password.encode('utf8'))

        usuario = (self.email, passCifrada.hexdigest())

        cursor.execute(consulta, usuario)
        usuario = cursor.fetchone()

        return [cursor.rowcount ,usuario]


