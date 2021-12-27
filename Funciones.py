def miFuncion(nombre, apellido):
    print("Saludos desde mi funcion")
    print(f'Nombre: {nombre}, Apellido: {apellido}')

miFuncion('Eliud','Morales')
miFuncion('Karla','Lara')

# Uso de return
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(resultado)

# Asignar valor default a los parametros de una funcion
''' Si a la funcion no se le pasa algun valor del parametro, automaticamente se le asiga el valor de 0 '''


# Argumentos variables en Funciones Tuplas
# será comun encontrar *args en lugar de *nombres
def listarNombres(*nombres):# El asterisco indica que no se sabe el valor de las variables, por lo tanto se convierte en una tupla que alamacenará nombres
    for nombre in nombres:
        print(nombre)
listarNombres('Juan','Karla','Maria','Ernesto')


# Ejercicio 1
'''
Crear una función para sumar los valores recibidos de tipo numérico, utilizando argumentos variables 
*args como parámetro de la función y regresar como resultado la suma de todos los valores pasados como argumentos.
'''
def sumar(*args):
    resultado = 0
    for valor in args:
        resultado += valor
        return resultado
print(sumar(2,4))

# Ejercicio 2
'''
Crear una función para multiplicar los valores recibidos de tipo numérico, 
utilizando argumentos variables *args como parámetro de la función 
y regresar como resultado la multiplicación de todos los valores pasados como argumentos.
'''

def multiplicar(*args):
    resultado = 1
    for valor in args:
        resultado *= valor
        return resultado
print(multiplicar(9,1))

# Argumentos variables en Funciones Diccionarios
def listarTerminos(**terminos):
    # se recorrerá la llave y su valor, en los terminos, 
    for llave, valor in terminos.items():# accedemos a los items de los terminos y asi poder acceder a cada uno de los elementos
        print(f'Llave: {llave}: {valor}')
listarTerminos(IDE = 'Integrated Development Enviroment',PK = 'Primary Key')


# Argumentos variables en Funciones Listas
def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
    
nombres = ['Juan','Karla','Pedro']
desplegarNombres(nombres)
desplegarNombres('Carlos')
desplegarNombres((8, 9))# Tuplas
desplegarNombres([10, 11])# Listas

