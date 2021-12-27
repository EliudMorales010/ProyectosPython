edad = int(input('Digite su edad entre (0 -30): '))
etapa = None
if edad <= 10:
    etapa = 'La infancia es increible'
elif edad >= 11 and edad<= 20:
    etapa = 'Mucho cambios y mucho estudio'
elif edad >=21 and edad <= 30:
    etapa = 'Amor y comienza el trabajo'
else:
    etapa = 'Etapa de vida NO reconocida'
print(f'Tienes {edad} y tu estapa dice que {etapa}')
    