MATERIAS = 1
nombre = input("Nombre completo: ")
grado = input("Grado: ")
grupo = input("Grupo: ")

# Hacer un ciclo, pedir datos y sumar la calificación
contador = 1
sumatoria = 0
while contador <= MATERIAS:
    nombre_materia = input("Nombre de la materia {}: ".format(contador))
    calificacion = float(input("Calificación en {}: ".format(nombre_materia)))
    # Sumar la calificación a la sumatoria
    sumatoria = sumatoria + calificacion
    # Aumentar el contador para no hacer un ciclo infinito
    contador = contador + 1

# Hacer cálculos e imprimir resultados
promedio = sumatoria / MATERIAS
print("""***** Resultados *****
Alumno: {} | {} {}
*******************************
* Promedio: {}
*******************************
""".format(nombre, grupo, grado, promedio))