# Desarrollar un programa que muestre los numeros pares entre 0 y "n" de forma ascendente, siendo "n" un numero solicitado por teclado.
n = int(input("Ingrese un numero n: "))
print(f"Numeros pares entre 0 y {n} en forma ascendente:")
for i in range(0, n + 1, 2):
    print(i)
