
numero = int(input("Digite un numero entre 1 y 3: "))
numeroTexto = ''

if numero == 1:
    numeroTexto = "numero uno"
elif numero == 2:
    numeroTexto = "numero dos"
elif numero == 3:
    numeroTexto = "numero tres"
else:
    numeroTexto = "Numero no reconocible"
    
print(f" Numero Proporcionado: ' { numero } : { numeroTexto } ")
