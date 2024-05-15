'''
Python por defecto instala el módulo 'tkinter' 
para la implementación de interfaces visuales.
'''
#1. Mostrar una ventana y que en su título aparezca el mensaje con tu nombre
import tkinter

class Aplicacion:
    def __init__(self):
        self.ventana = tkinter.Tk()
        self.ventana.title("jose apaza saavedra")
        self.ventana.mainloop()

#********MAIN**********
app = Aplicacion()