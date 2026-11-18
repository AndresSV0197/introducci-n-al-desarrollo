# Implementar otro ciclo for para que se visualicen solo 10 numeros por renglon.
# Desarrollar un programa que muestre los numeros pares entre 0 y "n" de forma ascendente, siendo "n" un numero solicitado por teclado. Ojo: utilizar print(i, end=" ") para imprimir los datos horizontalmente.
n = int(input("Ingrese un numero n: "))
contador = 0
for i in range(0, n + 1, 2):
    print(i, end=" ")
    contador += 1
    if contador == 10:
        print()
        contador = 0
if contador != 0:
    print()
