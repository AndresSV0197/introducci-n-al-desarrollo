# Utilizando un ciclo while, visualizar un menú de 3 productos y mostrar el precio del producto solicitado por el usuario.
print("----- MENU -----")
print("GASEOSA---1")
print("PAN-------2")
print("LECHE-----3")
num = int(input("Ingrese numero de acuerdo al menu"))
while num != 0:
    if num == 1:
        print(f"{num} El valor es 1000 del producto GASEOSA--1")
    elif num == 2:
        print(f"{num} El valor es 2000 del producto PAN-----2")
    elif num == 3:
        print(f"{num} El valor es 3000 del producto LECHE---3")
    else:
        print("Ingresaste un numero no valido")
    num = int(input("Ingrese numero de acuerdo al menu o presiona 0 para salir"))
