# IMPORTANTE: Una lista es mutable (modificable)

# Definir una lista de nombres
nombres = ['Juan','Karla','Ricardo','Maria']

# Imprimir una lista
print(nombres)

# Acceder a los elementos de una lista
print(nombres[0])
print(nombres[1])

# Acceder a los elementos de manera inversa
print(nombres[-1])
print(nombres[-2])

# Imprimir un rango de elementos en una lista
print(nombres[0:2])# sin incluir el indice 2

# Ir desde el inicio de la lista hasta el indice (sin incluirlo)
print(nombres[:3])

# Ir desde el indice indicado hasta el final
print(nombres[1:])

# Cambiar un valor de la lista
nombres[3] = 'Ivone'
print(nombres)

# Iterar una lista
for nombre in nombres:
    print(nombre)
else:
    print('No existen mas nombres en la lista')

# Preguntar el largo de una lista
print(len(nombres))# devuelve la cantidad de elementos de la lista

# Agregar un elemento a la lista
nombres.append('Lorenzo')
print(nombres)

# Insertar un elemento en un indice en especifico
nombres.insert(1,'Octavio')
print(nombres)

# remover un elemento de la lista
nombres.remove('Octavio')
print(nombres)

#remover le ultimo elemento agregado
nombres.pop()
print(nombres)

# Eliminar un elemento en un indice indicado
del nombres[0]
print(nombres)

# Limpiar la lista
nombres.clear()
print(nombres)

# Eliminar la lista por completo
del nombres
print(nombres)

