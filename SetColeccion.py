# No permite almacenar elementos duplicados
# No mantiene un orden
# No es posible modificar los elementos almacenados 
# Si es posible agregar elementos o eliminarlos
# No existen indices para cada elemento

planetas = {'Marte','Jupiter','Venus'}
print(planetas)# No se imprimen en orden

# Preguntar el largo de una tupla
print(len(planetas))

# Revisar su un elemento esta presente en el set
print('Marte' in planetas)# Devuelve un valor boooleano

# Agregar un elemento
planetas.add('Tierra')
print(planetas)

# Eliminar elementos posiblemente arrojando un error
planetas.remove('Tierra')# remove: hace posible eliminar un elemento
print(planetas)

# Eliminar elemento sin arrojar error
planetas.discard('Jupiter')# discard: hace posible eliminar un elemento 
print(planetas)

# Limpiar el set
planetas.clear()
print(planetas)

# Eliminar el set
del planetas
print(planetas)
