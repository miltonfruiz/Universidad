''' Ejercicio N° 10  

De cada uno de los alumnos de primer año de la facultad se tienen los siguientes datos:
Nº de comisión - Nota del parcial
No se sabe la cantidad de comisiones ni la cantidad de alumnos por comisión. Los 
datos están ordenados por comisión.
Determinar, para cada una de las comisiones, el número de comisión y el promedio de 
las notas de dicho parcial.

var: comision, aux, nota, talumnos, tnotas: integer; '''

def CONTADOR():
	global aux, tnotas, talumnos
	aux = 0
	tnotas = 0
	talumnos = 0

def CALCULO():
	global aux, comision, tnotas, talumnos, nota
	aux = comision
	while(aux == comision):
		nota = int(input('Ingrese nota: '))
		tnotas += nota
		talumnos += 1
		comision = int(input('Ingrese comision: '))
	MOSTRAR()

def MOSTRAR():
	global aux, tnotas, talumnos
	print('Número de comisión: ',aux)
	print('Promedio de notas: ',tnotas/talumnos)

comision = int(input('Ingrese comision: '))
while(comision != 0):
	CONTADOR()
	CALCULO()