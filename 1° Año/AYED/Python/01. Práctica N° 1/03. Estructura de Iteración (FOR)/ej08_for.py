''' Ejercicio N°8

Ingresar dos números naturales.
Verificar si el primero es menor que el segundo.
En caso afirmativo mostrar todos los números comprendidos entre ellos en secuencia
ascendente, incluyendo los extremos.

var: nro1, nro2, i: integer; '''

nro1 = int(input('Ingrese el primer numero: '))
nro2 = int(input('Ingrese el segundo numero: '))
if nro1 < nro2:
	for i in range(nro1, nro2+1):
		print(i)