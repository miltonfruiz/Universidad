''' Ejercicio N°16

Dada una lista de 93 números, determinar e informar el valor máximo y el orden en el 
que fue ingresado.

var: vmax, i, numero, posM: integer; '''



vmax = 0
posM = 1
for i in range(2, 94):
	numero = int(input('Ingrese un numero: '))
	if numero > vmax:
		vmax = numero
		posM = i
print('El valor máximo es ',vmax,'y está en la posición ',posM)