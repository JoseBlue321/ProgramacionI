#********LIST*************

frutas = ["uva","frutilla","platano"]
asistencia = ["jose","josue","ruben","antonio","wilmer","jose"]
paises = ["haiti","españa","china"]
edades = [28, 25, 18, 15, 18, 18]
tallas = [1.73, 1.65, 1.80]

print("platano",frutas.index("platano")) #nos muesta la posicion de un datos de la lista
print( edades.count(18) ) #nos muesta la cantidad de datos que hay en la lista
frutas.extend(asistencia) #reforma la lista a una sola lista
print( frutas )

asistencia.append("logan")#agregando un registro a la lista
asistencia.append("juan")#agregando un registro a la lista
asistencia.insert(2,"porfirio") #insertar un registro a la posicion deseada

asistencia.remove("wilmer") #eliminar un registro de la lista
asistencia.remove("jose") 
asistencia.pop() #eliminar los registro de la lista (del ultimo)
asistencia.pop(1) #eliminar la posicion de la lista
del asistencia[2] #eliminar un registro de la lista segun la posicion

asistencia.clear() #vaciar la lista

join = frutas + paises #unir listas

frutas.sort() #ordena la lista de forma ascendente A- Z
paises.sort(reverse=True) #ordenar la listra de forma descendente Z - A

print( paises )

frutas2 = frutas.copy() #creamos una copia de la lista original
print( frutas2 )
