# Un diccionario consta de: key = llave y value = valor de la llave
# No existen indices para los elementos
# No se puede agregar llaves duplicadas, si lo hace, sobrescribe la llave con el nuevo valor

diccionario = {
    'IDE':'Integrated Development Enviroment',
    'OOP':'Object Oriented Programing',
    'DBMS':'Database Management System'
}
print(diccionario)

# Preguntar el largo de un diccionario
print(len(diccionario))

# Acceder a un elemento mediante la (key)
print(diccionario['IDE'])

# Otra froma de accerder a un elemento del diccionario
print(diccionario.get('OOP'))

# Modificar elementos de un diccionario
diccionario['IDE'] ='integrated development enviroment'  
print(diccionario)

# Recorrer los elemento en un diccionario
for termino, valor in diccionario.items():# items: para que nos muestre el termino y el valor del diccionario
    print(termino, valor)
    
# Recorrer los elemento en un diccionario pero solo las llaves
for termino in diccionario.keys():# keys: para que nos muestre solo el termino del diccionario
    print(termino) 
    
# Recorrer los elementos de un diccionario pero solo los valores 
for termino in diccionario.values():# values: para que nos muestre solo el valor del diccionario
    print(termino)
    
# Comprobar existencia de algun elemento en el diccionario
print('IDE' in diccionario) # Devuelve un valor booleano

# Agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

# Remover un elemento
diccionario.pop('DBMS')
print(diccionario)

# Limpiar el diccionario
diccionario.clear()
print(diccionario)

# Eliminar el diccionario
del diccionario



