from usuarios.acciones import AccionesUsuario

flag = True
while flag == True:
    print("**********************************************")
    print("***********ACCIONES DISPONIBLES***************")
    print("**********************************************")
    print("**** 1 - Registro Usuario (opcion - 1)********")
    print("**** 2 - Logín Usuario (opcion - 2)***********")
    print("**** 3 - Salir (opcion - 3)*******************")
    print("**********************************************")
    print("**********************************************")
    opcion = int(input("Que quieres hacer?: "))
    print("**********************************************")
    print("**********************************************")

    #Hacer la instancia
    hazEl = AccionesUsuario()

    if opcion > 0 and opcion <= 3:
        if opcion == 1:
            hazEl.registro()
        elif opcion == 2:
            hazEl.login()
        elif opcion == 3:
            flag = False
    else:
        print("Opcion incorrecta introduzca número 1 - 3")