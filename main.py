from logica.NumeroNatural import NumeroNatural

if __name__ == '__main__':
    numero1 = NumeroNatural()
    numero1.validarTipo()

    numero2 = NumeroNatural()
    numero2.validarTipo()

    mcd = numero1.calcularMCD(numero2.numeroNatural)

    print("El MCD de", numero1.numeroNatural, "y", numero2.numeroNatural, "es:", mcd)
