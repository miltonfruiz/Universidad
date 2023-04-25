''' Ejercicio N°11

Generar e informar los primeros N múltiplos de un número M entero cualquiera.
N y M son dos números que se ingresan como dato.

var: genera, N, M,i: integer; '''

genera = 0
N = int(input('Ingrese los multiplos: '))
M = int(input('Ingrese un número cualquiera: '))
for i in range(1, N+1):
	genera = M * i
	print('Los primeros son: ',genera)