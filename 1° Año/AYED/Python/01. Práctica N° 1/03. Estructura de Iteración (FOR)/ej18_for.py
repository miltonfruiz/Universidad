''' Ejercicio N°18

Una escuela realiza un control sobre el estado físico de sus 304 alumnos. Dispone de
los números de legajos y estatura (en cms.) de cada uno de ellos. 
Se requiere saber el promedio de estatura, así como los números de legajos de los
alumnos de estatura inferior a 165 cms.

var: promedio, i, legajo: integer;  estatura: float; '''

promedio = 0
for i in range(1,304+1):
	legajo = int(input('Ingrese numero de legajo: '))
	estatura = float(input('Ingrese estatura en centímetros: '))
	promedio = promedio + estatura
	if estatura < 165:
		print('El legajo ',legajo,'es inferior a 165')
print('El promedio de estatura es: ', promedio/304)