''' Ejercicio N°10

Obtener la suma de los N números naturales posteriores al número 300 inclusive.

var: suma,N,i: integer; '''

suma = 0
N = int(input('Ingrese números a sumar: '))
for i in range(300, 300+N):
	suma = suma + i
print('El total de la suma es: ',suma)