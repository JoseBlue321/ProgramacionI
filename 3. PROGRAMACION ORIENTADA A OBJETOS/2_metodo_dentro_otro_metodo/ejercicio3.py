'''
Confeccionar una clase que administre una agenda personal. 
Se debe almacenar el nombre de la persona, teléfono y su correo
Debe mostrar un menú con las siguientes opciones:
1- Carga de un contacto en la agenda.
2- Listado completo de la agenda.
3- Consulta ingresando el nombre de la persona.
4- Finalizar programa.
'''
class Agenda:
    def __init__(self):
        self.contactos = []
        self.persona = {}
    
    def cargar(self):
        nombre =  input("Nombre: ")
        telefono =  input("Telefono: ")
        correo =  input("Correo: ")
        self.persona = {
            'nombre':nombre,
            'telefono':telefono,
            'correo':correo
        }
        self.contactos.append( self.persona )

    def mostrar(self):
        for i in range( len(self.contactos)):
            print(self.contactos[i])

    def consultar(self):
        nombre = input("Consultar nombre: ")
        for i in range( len(self.contactos) ):
            if nombre in self.contactos[i]['nombre']:
                print( self.contactos[i]['nombre'], self.contactos[i]['telefono'], self.contactos[i]['correo']  )

    def menu(self):
        opcion=0
        while opcion!=4:
            print("1- Carga de un contacto en la agenda")
            print("2- Listado completo de la agenda")
            print("3- Consulta ingresando el nombre de la persona")
            print("4- Modificacion del telefono y mail")
            print("5- Finalizar programa")
            opcion=int(input("Ingrese su opcion:"))
            if opcion==1:
                self.cargar()
            elif opcion==2:
                self.mostrar()
            elif opcion==3:
                self.consultar()

    


#**************MAIN******************
agenda1 = Agenda()
agenda1.menu()