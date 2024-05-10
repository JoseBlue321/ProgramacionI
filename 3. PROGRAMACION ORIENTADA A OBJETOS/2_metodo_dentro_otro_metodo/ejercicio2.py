'''
Plantear una clase que administre dos listas de 5 nombres de estudiantes y sus notas. 
Mostrar un menú de opciones que permita:
1- Cargar estudiantes.
2- Mostrar a los estudiantes con sus notas.
3- Mostrar estudiantes con notas mayores o iguales a 7.
4- Finalizar programa.
'''

class Estudiante:
    
    def __init__(self):
        self.nombres = []
        self.notas = []

    def cargar(self):
        for i in range(5):
            nombre = input("Nombre: ")
            nota = int(input("Nota: "))
            self.nombres.append(nombre)
            self.notas.append(nota)
    
    def mostrar(self):
        for i in range( 5 ):
            print( self.nombres[i], self.notas[i] )
    
    def mayores_siete(self):
        for i in range(5):
            if self.notas[i] >= 7:
                print(self.nombres[i], self.notas[i])

    def menu(self):
        opcion = 0
        while opcion != 4:
            print("1. cargar")
            print("2. mostrar")
            print("3. mostrar estudiantes con nota mayor igual a 7")
            print("4. salir")
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1:
                self.cargar()
            elif opcion == 2:
                self.mostrar()
            elif opcion == 3:
                self.mayores_siete()


#**********MAIN**************
estudiante1 = Estudiante()
estudiante1.menu()