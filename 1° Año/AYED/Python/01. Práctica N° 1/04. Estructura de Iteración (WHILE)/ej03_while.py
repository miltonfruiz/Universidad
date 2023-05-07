''' Ejercicio N° 2 

Se van ingresando números distintos de cero, salvo el último valor. Determinar su suma.

var: sumo, numero: integer; '''

sumo = 0
numero = int(input('Ingrese numero: '))
while (numero != 0):
	sumo += numero
	numero = int(input('Ingrese numero: '))
print('La suma total es: ',sumo)