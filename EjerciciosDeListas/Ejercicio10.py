'''
Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, 
donde <asignatura> es cada una de las asignaturas de la lista.
'''

asignatura = None
i = 0
listaAsignatura = []

num = int(input("Digite el numero de asignaturas: "))
while i < num:
    nombre = str(input("Digite una Asignatura: "))
    i += 1
    listaAsignatura.append(nombre)
    
for asig in listaAsignatura:
    print("Yo estudio: " + asig)