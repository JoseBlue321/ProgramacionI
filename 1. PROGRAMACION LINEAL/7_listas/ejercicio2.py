#cargar una lista de un equipo de futbol (numeros)
#ordenar la lista de menor a mayor

lista_jugadores = []

for i in range(11):
    jugador = int(input("numero del jugador: "))
    lista_jugadores.append(jugador)

print("lista sin ordenar:")
print(lista_jugadores)

for k in range(10):
    for x in range(10):
        if lista_jugadores[x] > lista_jugadores[x + 1]:
            aux = lista_jugadores[x]
            lista_jugadores[x] = lista_jugadores[x + 1]
            lista_jugadores[x + 1] = aux

print("lista de jugadores ordenado")
print(lista_jugadores)
