'''
Pide números y mételos en una lista, 
cuando el usuario meta un 0 ya dejaremos de insertar. 
Por último, muestra los números ordenados de mayor a menor.
'''

lista = []
i = 0
salir = False
while not salir:
    numero = int(input('Digite un numero: '))
    if numero == 0:
        salir = True
    else:
        lista.append(numero)
lista.sort(reverse = True)# Ordena la lista de mayor a menor
print(lista)
    