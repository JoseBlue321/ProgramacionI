'''
Podemos llamar a un metodo dentro de otro metodo
'''
class Operacion:
    def __init__(self):
        self.n1 = int(input("Ingrese numero 1: "))
        self.n2 = int(input("Ingrese numero 2: "))
        self.suma()
        self.resta()

    def suma(self):
        sum = self.n1 + self.n2
        print("la suma es: ",sum)

    def resta(self):
        res = self.n1 - self.n2
        print("La resta es: ",res)

#***********Objetos*************
operacion = Operacion()