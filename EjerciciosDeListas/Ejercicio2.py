'''
Escriba un programa que permita crear una lista de palabras y que, 
a continuación, pida una palabra 
y diga cuántas veces aparece esa palabra en la lista.
'''
palabras = []
num = int(input('Digite un numero: '))
i = 0
while i < num:
    nombre = input('Digite un nombre: ')
    i += 1
    palabras.append(nombre)
print(palabras)

buscarPalabra = input('Digite una palabra a buscar: ')
cont = 0
for i in palabras:
    if i == buscarPalabra:
        cont += 1
if cont == 0:
    print(f'La palabra: {buscarPalabra} no esta en la lista')
elif cont == 1:
    print(f'La palabra: {buscarPalabra} aparece 1 vez en la lista')
else:
    print(f'La palabra: {buscarPalabra} aparece {cont} veses en la lista')