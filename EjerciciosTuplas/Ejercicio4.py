# Crea una tupla con numeros e indica el numero con mayor valor y el de menor valor

# creo una tupla
numeros = (2, 56, 32, 34, 66, 31, 74, 43, 7, 4, 5, 65, 2, 1, 0, 15, 19, 100)

maximo = numeros[0]
minimo = numeros[0]

# indico el numero con mayor valor y el de menor valor
for i in numeros:
    if i > maximo:
        maximo = i
    if i < minimo:
        minimo = i

print("El numero menor de la tupla es: ", maximo)
print("El numero menor de la tupla es: ", minimo)

################################################3
# Otra forma seria

numeros = (2, 56, 32, 34, 66, 31, 74, 43, 7, 4, 5, 65, 2, 1, 0, 15, 19, 100)
print("Maximo numero: ",max(numeros))
print("Minimo numero: ", min(numeros))




