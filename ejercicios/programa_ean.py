def funcionEan(codigo):
    if len(str(codigo)) >= 8 and len(str(codigo)) <= 13:
        
        codigo = str(codigo)
        longitud = len(codigo)
        ultimo_digito = codigo[longitud - 1]
        
        #recorrer la parte delantera sin el ultimo digito PARES
        suma_pares = 0
        for i in range (len(codigo) - 1):
            if int(codigo[i]) % 2 == 0:
                suma_pares += int(codigo[i])

        #recorrer la parte delantera sin el ultimo digito PARES
        suma_impares = 0
        for i in range (len(codigo) - 1):
            if int(codigo[i]) % 2 != 0:
                suma_impares += int(codigo[i])

        mensaje = ' '
        if len(codigo) == 8:
            suma_impares = suma_impares * 3
            resultado = suma_impares + suma_pares
            division = resultado % 10
            resta = 10 - division 
            

            mensaje +=  f'Codigo Ean: {codigo} \n'
            mensaje +=  f'Digito de control: {division} \n'
            mensaje += f'Codigo de control: {ultimo_digito} \n'
            if resta == ultimo_digito:
                mensaje += 'Es correcto \n'
            else:
                mensaje += 'Es incorrecto \n'
            
            return mensaje

        elif len(codigo) == 13:
            suma_pares = suma_pares * 3
            resultado = suma_impares + suma_pares
            division = resultado % 10
            resta = 10 - division 

            mensaje +=  f'Codigo Ean: {codigo} \n'
            mensaje +=  f'Digito de control: {division} \n'
            mensaje += f'Codigo de control: {ultimo_digito} \n'
            
            if resta == ultimo_digito:
                mensaje += 'Es correcto \n'
            else:
                mensaje += 'Es incorrecto \n'

            return mensaje

    else: 
        print('codigo incorrecto No tiene LOS CARACTERES SUFICIENTES:')


codigo = 12345678
mensaje = funcionEan(12345678)
print(mensaje)