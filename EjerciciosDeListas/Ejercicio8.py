# Pide una cadena por teclado, mete los caracteres en una lista sin repetir caracteres.

lista = []
cadena = str(input('Digite una cadena: '))

for caracter in cadena:
    if caracter not in lista:
        lista.append(caracter)
print(lista)
        