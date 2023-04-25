''' Ejercicio N°12

Ingresado un número X, calcular X5.

var: potencia, x, i: integer; '''

potencia = 1
x = int(input('Ingrese un número: '))
for i in range(1,6):
	potencia = potencia * x
print(potencia)