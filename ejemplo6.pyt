# Ejercicio lado cuadrado
lado_cuadro = float(input("Ingrese el lado del cuadro"))
if lado_cuadro > 0:
    area_cuadro = lado_cuadro * lado_cuadro
    print("el area es: ", str(area_cuadro))
else:
    print("lado no puede ser menor o igual a 0")
print("fin del programa")
