''' Ejercicio N°7

Calcular y exhibir la suma de los primeros 100 números naturales.

var: calculo, i: integer; '''

calculo = 0
for i in range(1, 101):
	calculo = calculo + i
print('La suma total es: ',calculo)