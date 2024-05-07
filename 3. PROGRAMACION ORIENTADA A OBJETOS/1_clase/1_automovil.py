class Automovil:
    #atributos
    nombre = ''
    marca = ''

    #metodos
    def cargar(self,nomb,mar):
        self.nombre = nomb
        self.marca = mar

    def mostrar(self):
        print( "Nombre: ",self.nombre )
        print( "Marca: ",self.marca )


#********OBJETOS**********
#objeto1:
auto1 = Automovil()
auto1.cargar("auto 1","nissan")
auto1.mostrar()

#objeto2:
auto2 = Automovil()
auto2.cargar("auto 2","toyota")
auto2.mostrar()

#objeto3:
auto3 = Automovil()
auto3.cargar("auto 3","ferrari")
auto3.mostrar()