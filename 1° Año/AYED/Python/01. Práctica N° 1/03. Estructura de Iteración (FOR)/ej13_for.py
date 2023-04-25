''' Ejercicio N°13

Calcular y exhibir el factorial de un número cualquiera ingresado por teclado.

var: factor, numeri, i: integer; '''

factor = 1
numero = int(input('Ingrese un número: '))
for i in range(1, numero):
	factor = factor * i
print('El factorial es: ', factor)