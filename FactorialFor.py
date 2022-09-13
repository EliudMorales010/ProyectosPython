factorial = 1
numero = int(input("Escribe un numero: "))
if numero < 0:
    print("Error!")
elif numero == 0:
    print("El factorial de 0 es 1")
else:
    for i in range(1, numero + 1):
        factorial = factorial * i
    print("El factorial de el numero", numero, "es", factorial)