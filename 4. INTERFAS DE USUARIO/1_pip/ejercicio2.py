#1. Mostrar una ventana con un botón en su interior. 
#Al ser presionado mostrar un mensaje.
import wx

class Ventana(wx.Frame):

    def __init__(self, *args, **kw):
        super(Ventana, self).__init__(*args, **kw)        
        self.boton1 =wx.Button(self, label="Presionar")
        self.Bind(wx.EVT_BUTTON, self.presion_boton,self.boton1)
    
    def presion_boton(self,evento):
        wx.MessageBox("Hola mundo")

aplicacion = wx.App()
frm = Ventana(None, title='Prueba')
frm.Show()
aplicacion.MainLoop()