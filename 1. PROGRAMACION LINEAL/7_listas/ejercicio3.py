frutas = ["uva","frutilla","platano"]
asistencia = ["jose","josue","ruben","antonio","wilmer","jose"]
paises = ["haiti","españa","china"]
edades = [28, 25, 18, 15, 18, 18]
tallas = [1.73, 1.65, 1.80]

#funciones con listas
print( len(asistencia) ) #nos muestra la longitud de la lista
print( max(frutas), max(edades) )  #nos retorna el maximo o mayor de la lista
print( min(asistencia), min(tallas) ) #nos retorna el minimo o menor de la lista
print( sum(edades) ) #nos retorna la suma de la lista (datos de tipo numerico)

#comparacion de listas
print( 25 in edades ) #nos retorna True o False, la pregunta es si el valor esta en la lista
print(edades is tallas) #nos retorna True o False, la pregunta es si la lista edades es equivalente a tallas
print( edades == tallas) #nos pregunta si son iguales a nivel de valores