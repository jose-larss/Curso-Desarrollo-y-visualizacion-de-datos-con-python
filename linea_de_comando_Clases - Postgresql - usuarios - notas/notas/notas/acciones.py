from notas.nota import Nota

class AccionesNota:

    def proximasAcciones(self, usuario):

        print("**********************************************")
        print("***********ACCIONES DISPONIBLES***************")
        print("**********************************************")
        print("**** 1 - Crear Nota (opcion - 1)**************")
        print("**** 2 - Mostrar Nota (opcion - 2)************")
        print("**** 3 - Eliminar Nota (opcion - 3)***********")
        print("**** 4 - Actualizar Nota (opcion - 4)*********")
        print("**** 5 - Salir (opcion - 5)*******************")
        print("**********************************************")
        print("**********************************************")
        opcion = int(input("Que quieres hacer?: "))
        print(usuario)
        if opcion > 0 and opcion <= 5:
            if opcion == 1:
                self.crearNota(usuario)
                self.proximasAcciones(usuario)
            elif opcion == 2:
                self.mostrarNotas(usuario)
                self.proximasAcciones(usuario)
            elif opcion == 3:
                self.eliminarNota(usuario)
                self.proximasAcciones(usuario)
            elif opcion == 4:
                print("Actualizar Nota")
                self.actualizarNota(usuario)
                self.proximasAcciones(usuario)
            elif opcion == 5:
                 
                print("**********************************")
                print(f"OK!! {usuario[1][1]} acabas de salir del programa!, Hasta pronto!!")
                print("**********************************")
                exit()
        else:
            print("******************************************")
            print("Opcion incorrecta introduzca número 1 - 5")
            print("******************************************")


    def actualizarNota(self, usuario):
         
        print(f"OK!! {usuario[1][1]} vamos a actualizar una nota!!")
        print("**********************************")
        titulo = input("Introduce la nota a ACTUALIZAR: ")
        titulo_nuevo = input("Introduce la nota nueva: ")
        contenido_nuevo = input("Introduce el contenido nuevo: ")
        usuario_id = usuario[1][0]

        nota = Nota(titulo_nuevo, contenido_nuevo, usuario_id)
        nota = nota.actualizar(titulo)
        
        if nota[0] >= 1:
            print("*****************************************")
            print(f"Perfecto!! has Actualizado la nota {titulo} a {nota[1].titulo}!!")
            print("*****************************************")
        else:
            print("*****************************************")
            print(f"Error la nota {titulo} que quieres modificar, NO EXISTE, O la has metido Mal escrita")
            print("*****************************************")            


    def eliminarNota(self, usuario):

        print(f"OK!! {usuario[1][1]} Vamos a eliminar una nota!")
        nota_borrar = input("Introduce nota a Borrar: ") 
        usuario_id = usuario[1][0]   
        nota = Nota(nota_borrar, "", usuario_id)
        nota = nota.borrarNota()
        
        if nota[0] >= 1:
            print("***************************************************")
            print(f"Se ha borrado la nota: {nota[1].titulo} Correctamente")
            print("***************************************************")

    def mostrarNotas(self, usuario):
          
        print(f"Vale!! {usuario[1][1]} aquí tienes tus notas.") 
        usuario_id = usuario[1][0]
        nota = Nota("", "", usuario_id)
        notas= nota.leerNotas()

        contador = 1
        if len(notas) != 0:
            for nota in notas:
                print("**********************************")
                print(f"La nota {contador} es: {nota[2]}")
                print(f"Contenido: {nota[3]}")
                print("**********************************")
                contador += 1
        else:
            print("*****************************************")
            print(f"Error {usuario[1][1]} todavía no hay ninguna nota, Registra Una!!")
            print("*****************************************")


    def crearNota(self, usuario):
    
        print(f"OK!! {usuario[1][1]} vamos a crear una nota!!")

        print("**********************************")
        nota = input("Introduce una nota: ")
        contenido = input("Introduce un contenido para esta nota: ")
        usuario_id = usuario[1][0]
        
        nota = Nota(nota, contenido, usuario_id)
        nota = nota.guardarNota()

        if nota[0] >= 1:
            print("*****************************************")
            print(f"Perfecto!! has guardado la nota {nota[1].titulo}!!")
            print("*****************************************")
        


         