''' Ejercicio N°20

Una comisión tiene 55 alumnos, de cada uno de los cuales se tienen las notas de los 6 
parciales que han rendido. Obtener el promedio de las notas de cada uno de los
alumnos. 

var: i, j: integer; promedio: float; '''

for i in range(1,56):
	promedio = 0
	for j in range(1,7):
		nota = int(input('Ingrese nota:'))
		promedio = promedio + nota
	print('El promedio es: ',promedio/6)