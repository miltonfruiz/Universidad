''' Ejercicio N°23

Una empresa está dividida en 10 secciones. Para cada una de ellas se tienen como datos: 
Nro. de sección
Cantidad de empleados que trabajan en ella para cada empleado se tiene como dato:
· Cantidad de horas trabajadas
· Turno de trabajo (‘M’: mañana; ‘T’: tarde)
Se desea saber:
· El promedio de horas trabajadas en cada sección
· La cantidad total de horas trabajadas en cada turno en la empresa

var: turnom, turnot, i, seccion, empleados, horas: integer; promedio: float; turno: string; '''

turnom = 0
turnot = 0
for i in range(1, 11):
	seccion = int(input('Ingrese numero de seccion: '))
	empleados = int(input('Ingrese total empleados: '))
	promedio = 0
	for j in range(1, empleados+1):
		horas = int(input('Ingrese total horas trabajadas: '))
		turno = str(input('Ingrese el turno: '))
		promedio = promedio + horas
		if turno == 'M' or turno == 'm':
			turnom += horas
		elif turno == 'T' or turno == 't':
			turnot += horas
		else:
			print('Turno inválido.')
	print('Promedio de horas trabajadas en la seccion',i,',',promedio/empleados,'hs.')
print('Cantidad total de horas trabajadas en turno mañana',turnom,'hs. y en turno tarde',turnot,'hs.')