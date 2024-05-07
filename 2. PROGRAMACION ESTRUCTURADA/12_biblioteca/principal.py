'''
Python tiene una biblioteca de funciones, variables, clases, etc...
que nos facilitaran la resolucion de problemas en una gran diversidad de areas 
como ser: matemática, estadistica, comprension de datos, internet, interfaces entre otros
'''
from random import random,randint
from math import sqrt, pow, factorial, pi, floor, ceil, log10
from statistics import *
from string import *


print( random() ) #mostrar numeros entre 0-1
print( randint(10,35) ) #mostrar un numero aleatorio entre el 1 y 10

print( sqrt(85) ) #nos retorna la raiz cuadrada de un numero
print( pow(2,4) ) #nos retorna la potencia de un numero
print( factorial(10) ) #nos retorna el factorial de un numero
print( pi ) #nos retorna el numero PI
print( ceil(10.5) ) #redondea al mas alto
print( floor(10.5) ) #redondea al mas bajo
print( log10(50) ) #retorna el logaritmo en base 10 de un numero

print( mean([2,3,6,8,5,3]) ) #nos retorna la media de una lista de datos
print( median([3,5,4,2,7,3]) ) #nos retorna la mediana de una lista de datos
print( mode([4,7,2,5,8,2]) ) #nos retorna la moda de una lista de datos

print( ascii_letters ) #nos retorna los caracteres de texto
print( digits ) #nos retorna todos los caracteres numericos
print( punctuation ) #nos retorna todos los caracteres simbolos


