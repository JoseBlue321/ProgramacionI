'''
Un módulo es un archivo que contiene un conjunto de codigo o funciones
que se puede incluir a una aplicación.
'''
from operaciones import suma,resta,multiplicacion,division
from mayor import mayor

#Dado 2 numeros, sumar, restar, multiplicar y dividir los mismos
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("ingrse el segundo número: "))

print( "la suma de los dos numeros ingresados es: ", suma(num1,num2) )
print( "la resta de los dos numero ingresados es: ", resta(num1,num2) )
print( "la multiplicacion de los dos numero ingresados es: ", multiplicacion(num1,num2) )
print( "la division de los dos numero ingresados es: ", division(num1,num2) )

#Dado 2 numeros: mostrar el mayor
print( "el mayor es: ",mayor(num1,num2) )

