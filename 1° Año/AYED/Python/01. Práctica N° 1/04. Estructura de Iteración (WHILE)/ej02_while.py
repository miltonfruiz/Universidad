''' Ejercicio N° 2

Se tienen como dato los importes de todas las facturas correspondientes al mes que
acaba de finalizar de un comercio (no se sabe cuántas son). Se desea conocer:
	• cuántas ventas se realizaron
	• importe promedio de las mismas
	• cuántos son los importes que superan los 300 pesos

var: cventas, cimportes, promedio: integer; '''

def CONTADOR():
	global cventas, cimportes, promedio
	cventas = 0
	cimportes = 0
	promedio = 0

def CALCULO():
	global cventas, cimportes, promedio
	cventas += 1
	promedio += importe
	if(importe > 300):
		cimportes += 1

def MOSTRAR():
	print('Total ventas: ',cventas)
	print('Importe promedio: ',promedio/cventas)
	print('Importe que superan los $300: ',cimportes)

CONTADOR()
importe = int(input('Ingrese importe: '))
while (importe != 0):
	CALCULO()
	importe = int(input('Ingrese importe: '))
MOSTRAR()