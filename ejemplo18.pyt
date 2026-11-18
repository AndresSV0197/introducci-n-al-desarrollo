# Ejercicio 18: División entre cero
# Intentamos realizar una operación matemática
try:
    # Dividimos 10 entre 0
    resultado = 10 / 0
    # Mostramos el resultado si la división es válida
    print("Resultado:", resultado)
# Capturamos el error de división entre cero
except ZeroDivisionError:
    # Mostramos un mensaje explicando el error
    print("Error: No se puede dividir entre cero.")
