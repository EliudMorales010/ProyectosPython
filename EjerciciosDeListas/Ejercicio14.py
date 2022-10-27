'''
Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista, pregunte al usuario la nota que ha sacado en cada asignatura 
y elimine de la lista las asignaturas aprobadas. 
Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
'''

listaAsignatura = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
listaAprobados = []

for asignatura in listaAsignatura:
    nota = float(input("¿Qué nota has sacado en " + asignatura + "?"))
    if nota >= 5:
        listaAprobados.append(asignatura)
        
for asignatura in listaAprobados:
    listaAsignatura.remove(asignatura)
print("Tienes que repetir " + str(listaAsignatura))