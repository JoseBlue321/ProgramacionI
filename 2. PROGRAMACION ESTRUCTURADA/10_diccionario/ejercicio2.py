'''
Diccionario de clave entera y valor entero, cadena
'''

diccionario = {
    1: 10,
    2: 45,
    3: 39
}
print( type(diccionario) )

print ("Diccionario de clave entero y valor cadena")
diccionario2 = {1: 'uno', 2: 'dos', 3: 'tres'}
print(diccionario2)
print(type(diccionario2))

print ("Diccionario de clave cadena y valor entero")
diccionario3 = {'uno': 1, 'dos': 2, 'tres': 3}
print(diccionario3)
print(type(diccionario3))

print ("Diccionario de clave cadena y valor cadena")
diccionario4 = {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
print(diccionario4)
print(type(diccionario4))

print ("Diccionario mixto")
diccionario5 = {1:"ID-XXXXX", "edad": 3, 'animal': '🐶' , ("John","Doe"): 6917222722, "salvaje": False}
print(diccionario5)
print(type(diccionario5))

print ("Diccionario vacío")
diccionario6 = {}
print(diccionario6)
print(type(diccionario6))
diccionario7 = dict()
print(diccionario7)
print(type(diccionario7))