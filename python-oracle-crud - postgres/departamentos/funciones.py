
import psycopg2

def borrar(NumeroEmpleado):

    connection = psycopg2.connect(
        database="cursoPython", 
        user="postgres", 
        password="1234")
    cursor = connection.cursor()
    try:

        ConsultaBaja = ("Delete from dept where dept_no=%s")
        cursor.execute(ConsultaBaja, (NumeroEmpleado,))

        if cursor.rowcount > 0:
            print('***************************************************************')
            print(f"Enhorabuena has borrado el departamento {NumeroEmpleado}  satisfactoriamente")
            print('***************************************************************')
            connection.commit()
        else:
            print("Dato no encontrado")

    except connection.Error as error:
        print("Error: ", error)

    cursor.close()
    connection.close()

def listar():
    connection = psycopg2.connect(
        database="cursoPython", 
        user="postgres", 
        password="1234")
    cursor = connection.cursor()
    try:

        listardatos = ("select * from dept")
        cursor.execute(listardatos)
        print('***********************************************************')
        print('***************LISTADO DE DEPARTAMENTOS********************')
        print('***********************************************************')
        for item in cursor:

            print(f"*************{item[0]} {item[1]} {item[2]}")
        print('***********************************************************')
        print('***********************************************************')
    except connection.Error as error:
        print("Error: ", error)

    cursor.close()
    connection.close()

def modificar(numeroDepartamento, nuevoLocalidad):
    connection = psycopg2.connect(
        database="cursoPython", 
        user="postgres", 
        password="1234")
    cursor = connection.cursor()
    try:

        ConsultaModificacion = ("Update dept set loc=%s where dept_no=")

        cursor.execute(ConsultaModificacion, (nuevoLocalidad, numeroDepartamento))
        if cursor.rowcount > 0:
            print('***************************************************************')
            print(f"Enhorabuena!! Registro {numeroDepartamento} modificado satisfactoriamente la ciudad a {nuevoLocalidad}")
            print('***************************************************************')
            connection.commit()
        else:
            print("Dato no encontrado")

    except connection.Error as error:
        print("Error: ", error)
    cursor.close()
    connection.close()

def insertar(codigo, nombre, localidad):

    from datetime import date
    connection = psycopg2.connect(
        database="cursoPython", 
        user="postgres", 
        password="1234")

    cursor = connection.cursor()
    try:

        ConsultaAlta = ("INSERT INTO dept "
                        "(dept_no,dnombre,loc) "
                        "VALUES (%s, %s, %s)")

        datosDepartamento = (codigo, nombre, localidad)

        cursor.execute(ConsultaAlta, datosDepartamento)
        print('********************************************************************')
        print(f'Enhorabuena has insertado el departamento {codigo} {nombre} {localidad} con EXITO!!')
        print('********************************************************************')

        connection.commit()

    except connection.Error as error:
        print("Error: ", error)

    connection.close()






