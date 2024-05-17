'''
CHECKBUTTON
Mostrar una ventana con un checkbutton con un mensaje de "¿Estas de acuerdo con los terminos de referencia?"
al hacer check habilitar el boton aceptar
'''
import tkinter
class App:
    def __init__(self):
        self.ventana = tkinter.Tk()
        self.ventana.title("ejercicio 4")
        self.ventana.geometry('500x300')

        self.seleccion = tkinter.IntVar()
        self.check = tkinter.Checkbutton( self.ventana, text="¿Estas de acuerdo con los terminos de referencia?", variable=self.seleccion, command=self.cambiar )
        self.check.grid( column=0, row=0 )

        self.boton = tkinter.Button( self.ventana, text="Aceptar", state="disabled" )
        self.boton.grid( column=0, row=1 )

        self.ventana.mainloop()

    def cambiar(self):
        if self.seleccion.get() == 1:
            self.boton.configure( state="normal" )
        elif self.seleccion.get()  == 0:
            self.boton.configure( state="disabled" )

#******************
app = App()