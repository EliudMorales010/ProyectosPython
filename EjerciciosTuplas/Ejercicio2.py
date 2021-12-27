'''
Crea una tupla con los meses del año, pide números al usuario, 
si el numero esta entre 1 y la longitud máxima de la tupla,
muestra el contenido de esa posición sino muestra un mensaje de error.
El programa termina cuando el usuario introduce un cero.
'''
meses = ('Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre')

salir = False # salir es falso
while (not salir):# Mientras que salir no sea verdadero
    numero = int(input('Digite un numero: '))
    if numero == 0:# Si salor es igual a 0
        salir = True# Salir es igual a true y termina el prorama
    else:
        if numero >= 1 and numero <= len(meses):# Si el numero esta entre 1 y la longitud maxima de la tupla
            print(meses[numero-1])# Imprimo la tupla menos 1, osea el valor esperado
        else:
            print('Inserta un numero entre 1 y ',len(meses))
    
    
