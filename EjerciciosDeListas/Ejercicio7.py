# Pide una cadena por teclado, mete los caracteres en una lista sin espacios.

lista = []
cadena = str(input('Digite una cadena: '))
print('Cadena: ' + cadena)

for caracter in cadena:
    if caracter != ' ':
        lista.append(caracter)
print(lista)

