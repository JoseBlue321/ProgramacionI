#0. Cargar una lista de 5 precios de productos
#1. mostrar la suma de los 5 productos
#2. mostrar el promedio
#3. mostrar el producto mas caro
#4. mostrar el producto mas barato
#5. ordenar la lista de productos

#0. Cargar una lista de 5 precios de productos
def cargar(list):
    for i in range(5):
        valor = int(input("ingrese el precio del producto: "))
        list.append(valor)
    return list

#1. mostrar la suma de los 5 productos
def suma(list):
    sum = 0
    for i in range(len(list)):
        sum = sum + list[i]
    return sum

#2. mostrar el promedio
def promedio(list):
    prom = suma(list) / 5
    return prom

#3. mostrar el producto mas caro
def caro(list):
    mayor = list[0]
    for i in range(1,len(list)):
        if list[i] > mayor:
            mayor = list[i]
    return mayor

#4. mostrar el producto mas barato
def barato(list):
    menor = list[0]
    for i in range(1,len(list)):
        if list[i] < menor:
            menor = list[i]
    return menor

#5. ordenar la lista de productos
def ordenar(list):
    for k in range(4):
        for x in range(4):
            if list[x] > list[x + 1]:
                aux = list[x]
                list[x] = list[x + 1]
                list[x + 1] = aux
    return list


#**************MAIN******************
list = []
list = cargar(list)
print(list)
print("la suma de los productos es: ", suma(list) )
print("el promedio de los productos es: ", promedio(list) )
print("el producto mas caro es: ", caro(list) )
print("el producto mas barato es: ", barato(list) )
print("La lista ordenada es: ", ordenar(list) )

