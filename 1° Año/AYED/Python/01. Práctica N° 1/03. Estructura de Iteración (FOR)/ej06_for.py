''' Ejercicio N°6

Sabiendo que una carrera universitaria cuenta con X cantidad de materias, ingresar las 
notas con que un alumno aprobó cada una de las materias durante su carrera
universitaria y finalmente mostrar la nota promedio de dicho alumno.

var: promedio, notas: float; x, i: integer; '''

promedio = 0
x = int(input('Ingrese total materias: '))
for i in range(1, x+1):
	notas = float(input('Ingrese las notas: '))
	promedio = (promedio + notas) / x
print('La nota promedio es: ',promedio)