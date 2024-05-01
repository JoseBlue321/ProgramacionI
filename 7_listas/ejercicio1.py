#cargar una lista de 5 edades
#identificar la mayor edad

lista_edades = [] #creamos una lista vacia

#leemos los valores y lo agregamos a la lista_edades
for i in range(5):
    valor = int(input("edad: ")) #leemos un valor por teclado
    lista_edades.append(valor) #agregamos el valor a la lista que se lee por teclado

#identifacamos la mayor edad
mayor = lista_edades[0]
for i in range(1,5):
    if lista_edades[i] > mayor:
        mayor = lista_edades[i]
print(lista_edades)
print("el mayor de la lista es: ")
print(mayor)