from notas.acciones import AccionesNota
from usuarios.usuario import Usuario

class AccionesUsuario:

    def registro(self):
        print("****************************************")
        print("OK!! Vamos a registrarnos en el sistema.")
        print("****************************************")
        nombre = input("Introduce tu nombre: ")
        apellido = input("Introduce tu apellido: ")
        email = input("Introduce tu e-mail: ")
        password = input("Introduce tu contraseña: ")

        usuario = Usuario(nombre, apellido, email, password)
        #Recogemos lo que devuelve de la clase Usuario.registrar()
        registro = usuario.registrar() 
   
        if registro[0] >= 1:
            print("****************************************************************")
            print(f"Perfecto!! {registro[1].nombre} te has registrado con este e-mail: {registro[1].email}")
            print("****************************************************************")
        else:
            print("****************************************************************")
            print(f"No se ha guardado el usuario {registro[1].nombre} porque el email {registro[1].email} ya existe!!")
            print("****************************************************************")
        
    def login(self):
        print("**********************************")
        print("Vale Identificate en el sistema!: ")
        print("**********************************")
        email = input("Introduce tu e-mail: ")
        password = input("Introduce tu contraseña: ")

        usuario = Usuario("", "", email, password)
        login = usuario.identificarse()
        
        if login[0] >= 1:
            
            print("****************************************************************")
            print(f"Bienvenido {login[1][1]} te has identificado en el sistema el día: {login[1][5]}")
            print("****************************************************************")
            # Crear la instancia y llamar a metodo de la clase Notas
            hazEl = AccionesNota()
            hazEl.proximasAcciones(login)
        else:
            print("****************************************************************")
            print(f"ERROR el e-mail {email} o la contraseña NO existen!")
            print("****************************************************************")   

      
