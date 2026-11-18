while True:
    print("----- MENÚ DE PRODUCTOS -----")
    print("1. Leche")
    print("2. Pan")
    print("3. Arroz")
    print("4. Huevos")
    print("5. Aceite")
    print("6. Salir")
    opcion = input("Elija un producto (0-5): ")
    if opcion == "1":
        print("Leche: $3.200")
    elif opcion == "2":
        print("Pan: $1.200")
    elif opcion == "3":
        print("Arroz: $3.500")
    elif opcion == "4":
        print("Huevos: $3.000")
    elif opcion == "5":
        print("Aceite: $12.500")
    elif opcion == "6":
        print("Gracias por su visita. Hasta pronto!")
        break
    else:
        print("Opcion no valida. Intente de nuevo.")
    volver = input("¿Desea volver al menú? (s/n): ")
    if volver.lower() != "s":
        print("Gracias por su visita. Hasta pronto!")
        break
