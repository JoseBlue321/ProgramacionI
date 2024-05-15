'''
1. mostrar una ventana con 1 label y 2 button
los botones deben ser de "incremento" y "decremento" de un valor del label
'''
import tkinter
class App:
    def __init__(self):
        self.valor = 1
        self.ventana = tkinter.Tk()
        self.ventana.title("Ejercicio 2")

        self.label = tkinter.Label( self.ventana, text=self.valor )
        self.label.grid( column=0, row=0 )

        self.boton1 = tkinter.Button( self.ventana, text="Incrementar", command=self.incrementar )
        self.boton1.grid(column=0 , row=1)

        self.boton2 = tkinter.Button( self.ventana, text="Decrementar", command=self.decrementar )
        self.boton2.grid( column=1 , row=1 )

        self.ventana.geometry('500x300')
        self.ventana.mainloop()

    def incrementar(self):
        self.valor = self.valor + 1
        self.label.config( text=self.valor )

    def decrementar(self):
        self.valor = self.valor - 1
        self.label.config( text=self.valor )

#***************MAIN*******************
app = App()
