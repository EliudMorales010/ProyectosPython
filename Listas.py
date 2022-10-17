# Definir una lista de tipo str (string)
nombres = ['Juan','Karla','Ricardo','Maria']

# Imprimir lista de nombres
print(nombres)

# Acceder a los elementos de una lista 
print(nombres[0])
print(nombres[1])

# Acceder a los elementos de una lista de manera inversa
print(nombres[-1])
print(nombres[-2])

# Imprimir un rango
print(nombres[0:2])# sin incluir el indice 2

# Ir al inicio de la lista (sin incluirlo)
print(nombres[ :3])

# Desde el indice indicado hasta el final
print(nombres[1:])

# Cambiar un valor
nombres[3] = "Ivone"
print(nombres)

# Iterar o recorrer una lista
for nombre in nombres:
    print(nombre)
else:
    print("No existen mas nombres en la lista")

# Eliminar un indice
del nombres[0]
print(nombres)

# Remover el ultimo indice agregado
nombres.pop()
print(nombres)

# Limpiar una lista
nombres.clear()
print(nombres)

# Borrar lista por completo
del nombres
print(nombres)