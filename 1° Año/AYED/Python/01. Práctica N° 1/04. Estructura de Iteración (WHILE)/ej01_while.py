''' Ejercicio N° 1 

Dado un conjunto de números enteros, determinar cuántos de ellos son mayores o
iguales que 100. Un número igual a cero indica fin de datos.

var: contador, numero: integer; '''

contador = 0
numero = int(input('Ingrese numero: '))
while (numero != 0):
	if(numero >= 0):
		contador += 1
	numero = int(input('Ingrese numero: '))
print('Total números mayores a 100: ',contador)