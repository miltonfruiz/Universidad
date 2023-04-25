''' Ejercicio N°21

Se tienen los siguientes datos de los N socios de un club:
Número de socio
Edad
Sexo (F ó M)
Importe de la cuota
AyED – Práctica Nº 1
Página 7 de 12
Se quiere saber:
a) Cantidad de mujeres y cantidad de hombres
b) Promedio de edad de todos socios
c) Total recaudado por el club en concepto de cuotas
 
var: cmujer, chombre, total, socios, i, numero, edad: integer; promedio, importe: float; sexo: string; '''

cmujer = 0
chombre = 0
promedio = 0
total = 0
socios = int(input('Ingrese cantidad de socios: '))
for i in range(1, socios+1):
	numero = int(input('Ingrese numero de socio: '))
	edad = int(input('Ingrese edad: '))
	promedio = promedio + edad
	sexo = str(input('Ingrese sexo, F o M: '))
	if sexo == 'F'or sexo == 'f':
		cmujer = cmujer + 1
	elif sexo == 'M' or sexo == 'm':
		chombre = chombre + 1
	else:
		print('No corresponde a un género.')
	importe = float(input('Ingrese importe de la cuota: '))
	total = total + importe
print('Cantidad de mujeres',cmujer,', cantidad de hombres',chombre)
print('Promedio de edad de los socios',promedio/socios)
print('Total recaudado', total)