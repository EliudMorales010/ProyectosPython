x = None
factorial = None
numero = int(input("Escribe un numero"))
if numero < 0:
    print("El numero no se puede leer :(")
x = 1
factorial = 1 
while x <= numero:   
    factorial = factorial * x
    x = x + 1
print("El factorial del numero", numero, "es", factorial)
