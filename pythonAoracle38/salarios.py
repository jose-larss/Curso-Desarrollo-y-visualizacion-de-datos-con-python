import cx_Oracle

connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

cursor = connection.cursor()
try:
    print('***********************************************************************************')
    print('**********************INTRODUCE RANGO SALARIAL: ***********************************')
    print('***********************************************************************************')
    try:
        salario1 = input("Introduce Salario1 del  Empleado:")
        salario2 = input("Introduce Salario2 del  Empleado:")
    except ValueError:
        print(f'Error tienes que introducir Numeros en {salario1}!!')
        print(f'Error tienes que introducir Numeros en {salario2}!!')

    print('***********************************************************************************')
    print('***********************************************************************************')
    consulta = ("SELECT * FROM emp where salario>=:parametro1 and salario <= :parametro2 or salario>=:parametro2 and salario <= :parametro1")
    cursor.execute(consulta, (salario1,salario2, salario2, salario1))
    # Si en un único parámetro tenemos que poner ',' a continuación del valor de la variable
    contador = 1
    if len(cursor != 0):
        for item in cursor:

            print(f"{contador} El empleado {item[1]} que es {item[2]} tiene un sueldo de {item[5]}")
            contador += 1
    else:
        print('ERROR CONSULTA VACIA')
except connection.Error as error:
    print("Error: ", error)

connection.close()