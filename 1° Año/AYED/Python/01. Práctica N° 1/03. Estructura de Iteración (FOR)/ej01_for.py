''' Ejercicio N°1

Calcular el sueldo de cada uno de los 50 operarios de una fábrica dados como datos la 
remuneración por hora (es la misma para todos los operarios) y la cantidad de horas
que trabajó en el mes cada operario. 

var: rem, sueldo: float; hs: integer; '''

rem = float(input('Ingrese remuneración por hora: '))
for i in range(1,51):
	hs = int(input('Ingrese horas trabajadas: '))
	sueldo = rem * hs
	print('El sueldo es de: ',sueldo)