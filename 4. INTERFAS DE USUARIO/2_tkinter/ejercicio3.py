'''
2. realizar una calculadora ingresando 2 numero
seleccionar:
- suma
- resta
- multiplicacion
- division
- potencia
'''
import tkinter

class App:
    def __init__(self):
        self.ventana = tkinter.Tk()
        self.ventana.title("Ejercicio 2")
        self.ventana.geometry('500x300')

        self.label1 = tkinter.Label( self.ventana, text="Ingrese el primer numero: " )
        self.label1.grid(column=0,row=0)
        
        self.num1 = tkinter.IntVar()
        self.entry1 = tkinter.Entry( self.ventana, width=10, textvariable=self.num1 )
        self.entry1.grid( column=1, row=0 )

        self.label2 = tkinter.Label( self.ventana, text="Ingrese el segundo numero: " )
        self.label2.grid( column=0, row=1 )

        self.num2 = tkinter.IntVar()
        self.entry2 = tkinter.Entry( self.ventana, width=10, textvariable=self.num2 )
        self.entry2.grid( column=1, row=1 )

        self.seleccionar = tkinter.IntVar()
        self.radiosuma = tkinter.Radiobutton( self.ventana, text="Sumar ", variable=self.seleccionar, value=1 )
        self.radiosuma.grid( column=0, row=2 )
        self.radioresta = tkinter.Radiobutton( self.ventana, text="Restar ", variable=self.seleccionar, value=2 )
        self.radioresta.grid( column=0, row=3 )
        self.radiomultiplicar = tkinter.Radiobutton( self.ventana, text="Multiplicar ", variable=self.seleccionar, value=3 )
        self.radiomultiplicar.grid( column=0, row=4 )
        self.radiodividir = tkinter.Radiobutton( self.ventana, text="Dividir ", variable=self.seleccionar, value=4 )
        self.radiodividir.grid( column=0, row=5 )
        self.radiopotencia = tkinter.Radiobutton( self.ventana, text="potencia ", variable=self.seleccionar, value=5 )
        self.radiopotencia.grid( column=0, row=6 )

        self.boton = tkinter.Button( self.ventana, text="Ejecutar Operacion", command=self.ejecutar )
        self.boton.grid(column=0 , row=7)

        self.resultado = tkinter.Label( self.ventana, text="ver resultado" )
        self.resultado.grid( column=0, row=8 )

        self.ver = tkinter.Label(self.ventana, text="")
        self.ver.grid( column=0, row=9 )

        self.ventana.mainloop()

    def ejecutar(self):
        n1 = self.num1.get()
        n2 = self.num2.get()
        valor_seleccion = self.seleccionar.get()

        if valor_seleccion == 1:
            suma = n1 + n2
            self.ver.config(text=suma)
        elif valor_seleccion == 2:
            resta = n1 - n2
            self.ver.config(text=resta)
        elif valor_seleccion == 3:
            multiplicacion = n1 * n2
            self.ver.config(text=multiplicacion)
        elif valor_seleccion == 4:
            division = n1 / n2
            self.ver.config(text=division)
        elif valor_seleccion == 5:
            potencia = n1 ** n2
            self.ver.config(text=potencia)





#***********************
app = App()