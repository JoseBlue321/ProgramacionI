'''
2. Realizar un juego lanzando 2 datos
- si los dos dados salen iguales -> ganaste
- caso contrario perdiste
'''
from random import randint

class Dado:
    def lanzar(self):
        self.valor = randint(1,6)
    
    def mostrar(self):
        print( self.valor )
    
    def devolver(self):
        return self.valor

class Juego:
    def __init__(self):
        self.dado1 = Dado()
        self.dado2 = Dado()
    
    def jugar(self):
        self.dado1.lanzar()
        self.dado2.lanzar()
        print( self.dado1.mostrar(), self.dado2.mostrar() )
        if self.dado1.devolver() == self.dado2.devolver():
            print("Ganaste")
        else:
            print("Perdiste")



#******MAIN*********
juego = Juego()
juego.jugar()