'''
- a) Registrar una lista de productos.
- b) mostrar la lista de los productos.
'''
import tkinter
class App:
    def __init__(self):
        self.list = []
        self.contador = 0
        self.ventana = tkinter.Tk()
        self.ventana.title("ejercicio5")
        self.ventana.geometry('500x300')

        self.text1 = tkinter.Label( self.ventana, text="Ingrese el nombre del producto: " )
        self.text1.grid( column=0, row=0 )

        self.producto = tkinter.StringVar()
        self.entry1 = tkinter.Entry( self.ventana, width=15, textvariable=self.producto )
        self.entry1.grid( column=0, row=1 )

        self.boton1 = tkinter.Button( self.ventana, text="Registrar", command=self.registrar )
        self.boton1.grid( column=0, row=2 )

        self.ver = tkinter.Label( self.ventana, text="" )
        self.ver.grid( column=0, row=3 )

        self.boton2 = tkinter.Button( self.ventana, text="Mostrar", command=self.mostrar )
        self.boton2.grid( column=0, row=4 )

        self.listbox = tkinter.Listbox( self.ventana )
        self.listbox.grid( column=0, row=5 )

        self.ventana.mainloop()

    def registrar(self):
        self.list.append( self.producto.get() )
        self.ver.config( text=self.list )
        self.entry1.delete(0, tkinter.END)
        
    def mostrar(self):
        for indice,valor in enumerate( self.list ):
            self.listbox.insert( indice,valor )
            

#******************
app = App()