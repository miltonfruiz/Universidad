''' Ejercicio N°2

Dados como datos 100 números enteros, mostrar cada uno de ellos indicando si es
‘POSITIVO’ ó ‘NEGATIVO’, según corresponda. 

var: i: integer; numero: flota; '''

for i in range(1,101):
	numero = int(input('Ingrese el número: '))
	if numero > 0:
		print('Es positivo.')
	else:
		print('Es negativo.')