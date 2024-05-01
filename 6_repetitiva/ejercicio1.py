# leer 5 valores por teclado y mostrar la suma de los 5 valores
suma = 0
for i in range(5):
    valor = int(input("ingrese un numero: "))
    suma = suma + valor
print(suma)