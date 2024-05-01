#Desarrollar un programa que permita leer el lado de un cuadrado 
#preguntar si quiere calcular su perimetro o su superficie
def superficie(lado):
    superficie = lado * lado
    print("la superficie es: ",superficie)

def perimetro(lado):
    perimetro = lado * 4
    print("el perimetro es: ",perimetro)

def leer():
    lado = int(input("ingresar el lado de un cuadrado: "))
    print("quieres calcular su perimetro o su superficie: ingrese (p) para su perimetro, ingrese (s) para su superficie")
    respuesta = input("respuesta: ") #p/s
    if respuesta == "p":
        #calcular su perimetro
        perimetro(lado)
    if respuesta == "s":
        #calcular su superficie
        superficie(lado)



#*******************************
leer()

