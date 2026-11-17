# Crea un programa que valide si a un usuario se le puede otorgar una tarjeta de crédito.
edad = int(input("Ingrese su edad: "))
salario = float(input("Ingrese su salario: "))
if edad > 15 and salario > 400000:
    print("Te otorgaremos una tarjeta visa clasica")
