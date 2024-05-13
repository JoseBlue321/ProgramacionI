'''
PIP es un programa que viene con Python 
y nos permite instalar paquetes de terceros 
con el objetivo de valernos de librerías de 
código desarrolladas por la comunidad de Python
'''
#1. Instalamos el paquete wxPython es uno de los miles de paquetes
# pip install wxPython
#mostrar una ventana vacia ejecutar desde el powershell
import wx
app = wx.App()
ventana = wx.Frame(parent=None,title="Hello world")
ventana.Show()
app.MainLoop()