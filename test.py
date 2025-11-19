import math

def mmc_dos(a, b):
    if a == 0 or b == 0:
        raise ValueError("El MMC no está definido cuando uno de los números es 0")
    return abs(a * b) // math.gcd(a, b)


def mmc_lista(numeros):
    if not numeros:
        raise ValueError("La lista no puede estar vacía")

    resultado = numeros[0]
    for n in numeros[1:]:
        resultado = mmc_dos(resultado, n)
    return resultado


if __name__ == "__main__":
    A = int(input("Introduce el valor de A: "))
    B = int(input("Introduce el valor de B: "))

    print(f"MMC de {A} y {B} = {mmc_dos(A, B)}")
