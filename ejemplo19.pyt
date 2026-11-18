# Ejercicio 19: Error de formato numérico
# Intentamos convertir el dato ingresado a entero
try:
    # Solicitamos un número al usuario
    numero = int(input("Ingrese un número entero: "))
    # Mostramos el número ingresado
    print("Número ingresado:", numero)
# Capturamos el error si el dato no es válido
except ValueError:
    # Mostramos un mensaje indicando el error
    print("Error: Debe ingresar un número válido.")
