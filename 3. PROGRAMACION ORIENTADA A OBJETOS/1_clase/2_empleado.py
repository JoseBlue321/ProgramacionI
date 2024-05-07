class Empleado:

    def __init__(self):
        self.nombre = input("Ingrese el nombre del empleado: ")
        self.sueldo = float(input("ingrese el sueldo: "))
    
    def mostrar(self):
        print("Nombre: ",self.nombre)
        print("Sueldo: ",self.sueldo)

    def impuestos(self):
        if self.sueldo > 2300:
            print("Pagar impuestos")
        else:
            print("No paga impuestos")
        
        
#*******OBJETOS*******
#objeto1:
empleado1 = Empleado()
empleado1.mostrar()
empleado1.impuestos()

#objeto2:
empleado2 = Empleado()
empleado2.mostrar()
empleado2.impuestos()

#objeto3:
empleado3 = Empleado()
empleado3.mostrar()
empleado3.impuestos()