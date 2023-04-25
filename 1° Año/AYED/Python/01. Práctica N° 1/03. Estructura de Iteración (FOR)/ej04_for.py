''' Ejercicio N°4

Dados como datos 200 números enteros, obtener y mostrar su suma.

var: suma, i, numeros: integer; '''

suma = 0
for i in range(1,201):
	numeros = int(input('Ingrese el número: '))
	suma = suma + numeros
print('La suma es: ', suma)