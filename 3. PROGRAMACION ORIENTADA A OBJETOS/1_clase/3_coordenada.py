'''
Desarrollar una clase que represente un punto en el plano.
Atributo: x,y
Methodos: 
- init (x,y)
- imprimir en que cuadrante se encuentra
'''
class Coordenada:

    def __init__(self):
        self.x = int(input("ingrese el valor de x: "))
        self.y = int(input("ingrese el valor de y: "))

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            print("primer cuadrante")
        else:
            if self.x < 0 and self.y < 0:
                print("segundo cuadrante")
            else:
                if self.x < 0 and self.y < 0:
                    print("tercer cuadrante")
                else:
                    if self.x > 0 and self.y < 0:
                        print("cuarto cuadrante")

#********Objetos*********
#objeto1
coordenada1 = Coordenada()
coordenada1.cuadrante()
