# IMPORTANTE: Una tupla es inmutable (no es modificable)

# Definir una tupla
frutas = ('Naranja', 'Platano', 'Guayaba')

# Preguntar el largo de una tupla
print(len(frutas))

# # Acceder a los elementos de una tupla
print(frutas[0])
print(frutas[1])

# Acceder a los elementos de manera inversa
print([-1])

# Imprimir un rango de elementos en una tupla
print(frutas[0:1])# Desde el indice 0 hasta el indice 1 sin contar el 1
print(frutas[0:2])# Desde el indice 0 hasta el indice 2 sin contar el 2

# Recorrer elementos de la tupla
for fruta in frutas:
    print(frutas)

# cambiar valor de una tupla
frutasLista = list(frutas) # list: le pasamos la tupla para convertirla en una lista
frutasLista[0] = 'Pera' # siendo una lista, podemos modificar cualquier valor
frutas = tuple(frutasLista) # tuple: le pasamos la lista para convertirla en una tupla

# Eliminar la tupla
del frutas
print(frutas)
