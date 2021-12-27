'''
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
'''
i = 0
NumeroLista = []
num = int(input("Digite un numero: "))
while i < num:
    numerosGanadores = int(input("Digite un numero ganador: "))
    i += 1
    NumeroLista.append(numerosGanadores)
NumeroLista.sort()# sort: acomoda los valores de menor a mayor
print(NumeroLista)