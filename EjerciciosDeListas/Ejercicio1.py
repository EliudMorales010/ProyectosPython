'''
Escriba un programa que permita crear una lista de palabras. 
Para ello, el programa tiene que pedir un número 
y luego solicitar ese número de palabras para crear la lista. 
Por último, el programa tiene que escribir la lista.
'''

# lista de palabras vacia
palabras = []

# Pido un numero
# Solicito el numero de palabras para crear la lista
num = int(input('Digite un numero: '))

i = 0
while i < num:
    palabra = input('Digite una palabra: ')
    i += 1
    palabras.append(palabra)
print(palabras)
