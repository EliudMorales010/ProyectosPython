'''
Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista y la muestre por pantalla.
'''


asignatura = None
listaAsignatura = []

i = 0
num = int(input("Digite un numero de materias: "))
while i < num:
    nombre = str(input("Digite una asigantura: "))
    i += 1 
    listaAsignatura.append(nombre)    
print(listaAsignatura)
    


