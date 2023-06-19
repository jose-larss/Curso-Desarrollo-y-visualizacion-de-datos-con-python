import sys
import psycopg2

class DepartamentosCrud:
    def __init__(self):

        self.connection = psycopg2.connect(
            database="cursoPython", 
            user="postgres", 
            password="1234")
        
        self.cursor = self.connection.cursor()
        self.opcion = 0
        self.numero_departamento = ""
        self.nombre = ""
        self.localidad_nueva = ""
        self.mensaje = ""
        
    def menu(self):

        try:
            while self.opcion != 5:
                print('**********1.- ALTA EN DEPARTAMENTO*****************************')
                print('**********2.- BAJA EN DEPARTAMENTO*****************************')
                print('**********3.- MODIFICAR EN DEPARTAMENTO************************')
                print('**********4.- VER DATOS EN DEPARTAMENTO************************')
                print('**********5.- SALIR********************************************')
                print('***************************************************************')
                print('***************************************************************')
                print('***************************************************************')
                try:
                    self.opcion = int(input('Introduce una opción: (5 - SALIR): '))
                    print('***************************************************************')

                    if self.opcion == 1:
                        self.numero_departamento = int(input("Introduce numero departamento nuevo:"))
                        nombre = input("Introduce nombre departamento nuevo:")
                        self.localidad_nueva = input("Introduce localidad departamento nuevo:")
                        self.mensaje = self.insertar(self.numero_departamento, nombre, self.localidad_nueva)
                        print(self.mensaje)
                    elif self.opcion == 2:
                        self.numero_departamento = int(input("Introduce Número de departamento a eliminar:"))
                        self.mensaje = self.borrar(self.numero_departamento)
                        print(self.mensaje)
                    elif self.opcion == 3:
                        self.numero_departamento = int(input("Número de departamento a modificar:"))
                        self.localidad_nueva = input("Nueva localidad:")
                        self.mensaje = self.modificar(self.numero_departamento, self.localidad_nueva)
                        print(self.mensaje)
                    elif self.opcion == 4:
                        self.mensaje = self.listar()
                        print(self.mensaje)
                    elif self.opcion == 5:
                        print('Gracias por su visita!!!!')
                        sys.exit()
                    else:
                        print('Introduce un numero correcto del 1 al 5!!!')
                except ValueError:
                    print('ERROR INTRODUCE NUMEROS, NO LETRAS')
        except self.connection.Error as error:
            print("Error: ", error)

        self.cursor.close()
        self.connection.close()


    def insertar(self,numero_departamento, nombre, localidad):

        from datetime import date
        ConsultaAlta = ("INSERT INTO dept "
                            "(dept_no,dnombre,loc) "
                            "VALUES (%s, %s, %s)")
        datosDepartamento = (numero_departamento, nombre, localidad)
        self.cursor.execute(ConsultaAlta, datosDepartamento)
        self.connection.commit()
        self.mensaje += f'******************************************************************** \n'
        self.mensaje += f'Enhorabuena has insertado el departamento {numero_departamento} {nombre} {localidad} con EXITO!! \n'
        self.mensaje += f'******************************************************************** \n'

        return self.mensaje
    
    def listar(self):

        listardatos = ("select * from dept")
        self.cursor.execute(listardatos)
        if self.cursor.rowcount > 0:
            print('***********************************************************')
            print('***************LISTADO DE DEPARTAMENTOS********************')
            print('***********************************************************')
            for item in self.cursor:
                print(f"*************{item[0]} {item[1]} {item[2]}")
            print('***********************************************************')
            print('***********************************************************')
            self.mensaje += f"******************Listado con éxito!!****************** \n"
        else:
            self.mensaje += f"Tabla vacia!, No hay registros"

        return self.mensaje

    def borrar(self,numero_departamento):

        ConsultaBaja = ("Delete from dept where dept_no=%s")
        self.cursor.execute(ConsultaBaja, (numero_departamento,))
        if self.cursor.rowcount > 0:
            self.connection.commit()

            self.mensaje += f'*************************************************************** \n'
            self.mensaje += f"Enhorabuena has borrado el departamento {numero_departamento} de satisfactoriamente \n"
            self.mensaje +='*************************************************************** \n'
            
        else:
            self.mensaje += f"Departamento no encontrado, NO EXISTE, INSERTALO!! \n"

        return self.mensaje
    
    def modificar(self, numero_departamento, nuevoLocalidad):

        ConsultaModificacion = ("Update dept set loc=%s where dept_no=%s")
        self.cursor.execute(ConsultaModificacion, (nuevoLocalidad, numero_departamento))
        if self.cursor.rowcount > 0:
            self.connection.commit()

            self.mensaje += f'*************************************************************** \n'
            self.mensaje += f"Enhorabuena!! Registro {numero_departamento} modificado satisfactoriamente la ciudad a {nuevoLocalidad} \n"
            self.mensaje += f'*************************************************************** \n'
            
        else:
            self.mensaje += f"Departamento no encontrado, NO EXISTE, INSERTALO!! \n"

        return self.mensaje










