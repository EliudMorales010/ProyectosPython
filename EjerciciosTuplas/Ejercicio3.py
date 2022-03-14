'''
Crea una tupla con numeros
pide un numero por teclado e indica cuantas veses se repite
'''
# creo la tupla
numeros = (2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30)

# pido el numero por teclado
num = int(input("Digite un numero: "))

# indico cuantas veses se repite
contador = 0
for i in numeros:
    if num == i:
        contador +=1 # contador = contador + 1 
print("Se encuentran",contador, "veses en la tupla")