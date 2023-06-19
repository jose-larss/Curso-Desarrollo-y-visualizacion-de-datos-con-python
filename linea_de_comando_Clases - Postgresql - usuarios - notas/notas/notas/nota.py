from conexion.conexion import conexion_BBDD
import datetime

connect = conexion_BBDD()
database = connect[0]
cursor = connect[1]

class Nota:

    def __init__(self, titulo, contenido, usuario_id):
        self.titulo = titulo
        self.contenido = contenido
        self.usuario_id = usuario_id

    def actualizar(self, nota):
        fecha = datetime.datetime.now()
        
        par_modificar = (self.titulo, self.contenido, fecha, nota, self.usuario_id)
        consulta = ("UPDATE notas SET titulo = %s, contenido = %s, fecha = %s WHERE titulo = %s and usuarios_id = %s")

        cursor.execute(consulta, par_modificar)
        database.commit()

        return [cursor.rowcount, self] 


    def borrarNota(self):

        nota = (self.titulo, self.usuario_id)
        consulta = ("DELETE FROM notas WHERE titulo = %s and usuarios_id = %s")

        cursor.execute(consulta, nota)
        database.commit()

        return [cursor.rowcount, self]
        

    def guardarNota(self):
        fecha = datetime.datetime.now()

        nota = (self.usuario_id, self.titulo, self.contenido, fecha)
        consulta = ("INSERT INTO notas (usuarios_id, titulo, contenido, fecha) VALUES(%s, %s, %s, %s)")

        cursor.execute(consulta, nota)
        database.commit()

        return [cursor.rowcount, self]

    def leerNotas(self):

        nota = (self.usuario_id, )
        consulta = ("SELECT * FROM notas WHERE usuarios_id = %s")

        cursor.execute(consulta, nota)
        notas = cursor.fetchall()

        return notas
        
