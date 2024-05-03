'''
Una tupla permite almacenar una coleccion de datos
no necesariamente del mismo tipo
Nota: una ves definido la tupla no podemos modificarla
'''
coordenadas = (12.45 , 456.56)
fecha_nacimiento = (19, "marzo", 1996)

persona = ['jose apaza', 28, fecha_nacimiento, 72533587 , coordenadas]
persona.append(coordenadas)

print( type(fecha_nacimiento) )
print( persona )