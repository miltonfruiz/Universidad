''' Ejercicio N°3

Ingresando una sucesión de 300 números enteros, determinar la cantidad de números. 
positivos que hay en ella.

var: cant, i, sucesion: integer; '''

cant = 0
for i in range(1,301):
	sucesion = int(input('Ingrese el número: '))
	if sucesion > 0:
		cant = cant + 1
print('Cantidad de números positivos: ', cant)