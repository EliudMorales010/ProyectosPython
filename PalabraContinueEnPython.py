# Imprimir numeros pares en un rango de datos
'''
for i in range(100):# el rango es de 100
    if i % 2 == 0:# el numero es divisible entre 2? 
        print(f'Valor: {i}')# imprimo el valor
'''

# palabra continue
for i in range(6):
    if i % 2 != 0:
        continue
    print(f'Valor: {i}')# imprimo el valor
