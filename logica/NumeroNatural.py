class NumeroNegativoExeption(Exception):
    pass


class NumeroNatural():
    def validarTipo(self):
        while True:
            try:
                self.numeroNatural = int(input("Ingrese un número natural: "))
                if self.numeroNatural < 0:
                    raise NumeroNegativoExeption
                break
            except ValueError as err:
                print("Oops!  Ingrese un número natural.  Intente otra vez...")
            except NumeroNegativoExeption as err:
                print("Oops!  Ingrese un número entero y positivo.  Intente otra vez...")
            return self.numeroNatural

    def divisores(self):
        numero = self.numeroNatural
        contador = 0
        for divisor in range(1, numero + 1):
            if (numero % divisor) == 0:
                print(divisor, "es divisor")
                contador += 1
        print("el numero ", numero, " tiene ", contador, " divisores")

    def calcularMCD(self, otro_numero):
        a = self.numeroNatural
        b = otro_numero

        while b:
            a, b = b, a % b

        return a


if __name__ == '__main__':
    numero1 = NumeroNatural()
    numero1.validarTipo()

    numero2 = NumeroNatural
    numero2.validarTipo()

    mcd = numero1.calcularMCD(numero2.numeroNatural)
    print("El MCD de", numero1.numeroNatural, "y", numero2.numeroNatural, "es:", mcd)

