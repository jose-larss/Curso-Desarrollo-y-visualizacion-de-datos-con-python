class Dni:

    def __init__(self):
        
        self.resultado = 0
    
    def get_letraDni(self, dni):
    
        self.dni = dni
        self.resultado = self.dni % 23

        print(self.get_DNI_substring(51075775))

        if self.resultado == 0:
            print('La letra de tu DNI es T: ', self.resultado)
        elif self.resultado == 1:
            print('La letra de tu DNI es: R', self.resultado)
        elif self.resultado == 2:
            print('La letra de tu DNI es: W', self.resultado)
        elif self.resultado == 3:
            print('La letra de tu DNI es: A', self.resultado)
        elif self.resultado == 4:
            print('La letra de tu DNI es: G', self.resultado)
        elif self.resultado == 5:
            print('La letra de tu DNI es: M', self.resultado)
        elif self.resultado == 6:
            print('La letra de tu DNI es: Y', self.resultado)
        elif self.resultado == 7:
            print('La letra de tu DNI es: F', self.resultado)
        elif self.resultado == 8:
            print('La letra de tu DNI es: P', self.resultado)
        elif self.resultado == 9:
            print('La letra de tu DNI es: D', self.resultado)
        elif self.resultado == 10:
            print('La letra de tu DNI es: X', self.resultado)
        elif self.resultado == 11:
            print('La letra de tu DNI es: B', self.resultado)
        elif self.resultado == 12:
            print('La letra de tu DNI es: N', self.resultado)
        elif self.resultado == 13:
            print('La letra de tu DNI es: J', self.resultado)
        elif self.resultado == 14:
            print('La letra de tu DNI es: Z', self.resultado)
        elif self.resultado == 15:
            print('La letra de tu DNI es: S', self.resultado)
        elif self.resultado == 16:
            print('La letra de tu DNI es: Q', self.resultado)
        elif self.resultado == 17:
            print('La letra de tu DNI es: V', self.resultado)
        elif self.resultado == 18:
            print('La letra de tu DNI es: H', self.resultado)
        elif self.resultado == 19:
            print('La letra de tu DNI es: L', self.resultado)
        elif self.resultado == 20:
            print('La letra de tu DNI es: C', self.resultado)
        elif self.resultado == 21:
            print('La letra de tu DNI es: K', self.resultado)
        elif self.resultado == 22:
            print('La letra de tu DNI es: E', self.resultado)
        elif self.resultado == 23:
            print('La letra de tu DNI es: T', self.resultado)

        

    def get_DNI_substring(self, dni):

        resultado = dni % 23
        letrasDNI = 'TRWAGMYFPDXBNJZSQVHLCKET'

        letra = letrasDNI[resultado]

        return f"La letra de tu DNI funcion substringes: {letra}"
        
