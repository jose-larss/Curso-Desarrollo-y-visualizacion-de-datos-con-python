
import cx_Oracle

connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

# una matriz o array y losa datos que devuelva se vuelcan en esta variable
cursor = connection.cursor()
cursor2 = connection.cursor()
try:

    cursor.execute("SELECT emp.apellido, dept.loc FROM emp, dept where emp.dept_no = dept.dept_no")
    cursor2.execute('SELECT * FROM dept')

    print("Lista de empleados/localidades:")
    print("---------------------------------------")

    for apellido, localidad in cursor:
        print(f"El apellido es {apellido}, localidad es {localidad}")

    for item in cursor2:

        print(f"El departamento es {item[0]}: {item[1]} esta en {item[2]} ")


except connection.Error as error:
    print("Error: ", error)

connection.close()