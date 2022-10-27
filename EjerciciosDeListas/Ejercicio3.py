# Mete los valores del 1 al 100 en una lista.

lista = []
i = 1
while i <= 100:
    lista.append(i)
    i += 1 # es igual que i = i + 1
print(lista)


# Otra forma
lista = list(range(1, 101))
print(lista)