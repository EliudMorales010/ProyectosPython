'''
Ejercicio 5: Crea una tupla con valores ya predefinidos del 1 al 10, 
pide un índice por teclado y muestra los valores de la tupla.
'''
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

indice = int(input("Eliga un indice: "))
for i in numeros:
    if indice == i:
        print(f"El valor que elegiste es: { numeros[indice] }")