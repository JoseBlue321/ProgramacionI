'''
La herencia significa que se puede crear nuevas clases a partir de clases ya existentes.
Tendra los atributos y metodos de la superclase o clase padre.
Ademas que se puede agregar otros atributos y metodos propios.
'''
#1. Crear una clase persona, atributos(nombre,edad) metodos(cargar(), mostrar())
#2. crear una clase empleado que se hereda de la clase persona aumentar los atribustos de (telefono, sueldo) metodos(impuestos())

class Persona:
    def __init__(self):
        self.nombre = input("Nombre: ")
        self.edad = int(input("Edad: "))
    
    def mostrar(self):
        print(self.nombre, "-" , self.edad)

class Empleado (Persona):
    def __init__(self):
        super().__init__()
        self.telefono = int(input("Telefono: "))
        self.sueldo = float(input("Sueldo: "))
    
    def mostrar(self):
        super().mostrar()
        print(self.telefono , "- ", self.sueldo)
    
    def impuesto(self):
        if self.sueldo >= 2550:
            print("Pagar impuestos")
        else:
            print("No paga impuestos")
    

#*********MAIN***********
empleado1 = Empleado()
empleado1.mostrar()
empleado1.impuesto()