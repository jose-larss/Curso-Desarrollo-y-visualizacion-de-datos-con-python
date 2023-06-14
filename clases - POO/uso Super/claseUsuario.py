class Usuarios:
	tipo_usuario = "Free"
	publicidad = True

	def __init__(self, nid, alias, nombre, apellidos):
		self.nid = nid
		self.alias = alias
		self.nombre = nombre
		self.apellidos = apellidos

	def muestra_datos(self):
		print("El nombre y los apellidos del usuario son: " + self.nombre, self.apellidos)
		print("El ID de usuario es: " + self.nid + ".")
		print("El alias del usuario es: " + self.alias + ".")


class UsuariosPremium(Usuarios):

	def __init__(self, participacion_sorteos, puntos_premios):
		super().__init__(self.nid, self.alias, self.nombre, self.apellidos)
		self.participacion_sorteos = participacion_sorteos
		self.puntos_premios = puntos_premios
		self.contenido_premium = True



class UsuariosPremiumPlus(UsuariosPremium):
		participacion_sorteos = 25
		
