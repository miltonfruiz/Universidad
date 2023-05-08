''' Ejercicio N° 11 

Del reloj de marcación del personal de una empresa se tienen los siguientes datos: 
día, DNI y cantidad de horas trabajadas
Se desea conocer:
Por día, quien trabajó la mayor cantidad de horas y el promedio de horas trabajas 
La cantidad total de horas trabajas.
Los datos vienen ordenados por día y la carga de datos termina al ingresar el día en 0.

var: dia, aux, mdni: string; horas, mayor, thoras, personal: integer; '''

def CONTADOR():
	global aux, mayor, thoras, personal
	aux = ''
	mayor = 0
	thoras = 0
	personal = 0

def CALCULO():
	global aux, dia, mdni, thoras, personal
	aux = dia
	while(aux == dia):
		dni = input('Ingrese dni: ')
		horas = int(input('Ingrese horas: '))
		if(horas > mayor):
			mdni = dni
		thoras += horas
		personal += 1
		dia = input('Ingrese dia: ')
	MOSTRAR()

def MOSTRAR():
	print('Persona con mayor horas trabajadas: ',mdni)
	print('Promedio de horas trabajadas: ',thoras/personal)
	print('Total horas trabajadas: ',thoras)

dia = input('Ingrese dia: ')
while(dia != '0'):
	CONTADOR()
	CALCULO()