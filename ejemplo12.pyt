# reto velocidad
velocidadX = float(input("Ingrese la velocidad X (en km/h): "))
print("Seleccione la zona:")
print("1. Zonas escolares (30 km/h)")
print("2. Vías urbanas (60 km/h)")
print("3. Vías rurales (80 km/h)")
print("4. Rutas nacionales (100 km/h)")
opcion = int(input("Ingrese el numero de la zona en la que se encuentra (1-4): "))
if opcion == 1:
    grupo = "Zonas escolares"
    limite = 30
elif opcion == 2:
    grupo = "Vías urbanas"
    limite = 60
elif opcion == 3:
    grupo = "Vías rurales"
    limite = 80
elif opcion == 4:
    grupo = "Rutas nacionales"
    limite = 100
else:
    grupo = "Desconocido"
    limite = 0
if grupo != "Desconocido":
    print(f"Pertenece al grupo de {grupo} (Límite: {limite} km/h)[élite: 4]")
    if velocidadX > limite:
        print("Estado: ¡ESTÁ INFRINGIENDO los límites de velocidad!")
    else:
        print("Estado: No está infringiendo los límites de velocidad.")
else:
    print("Opción de zona no válida.")
