'''
Dada la siguiente tupla, 
crear una lista que sólo incluya los números menor que 5 utilizando un ciclo for: 
tupla = (13, 1, 8, 3, 2, 5, 8)
'''
numeroMenores = []
tupla = (13, 1, 8, 3, 2, 5, 8) 

for numero in tupla:
    if numero < 5:
        print(numero)
        numeroMenores.append(numero)
print(numeroMenores)
        


