''' Ejercicio N° 5

Se dispone de una serie de importes y para cada uno es necesario saber si se aplica o 
no un descuento. En caso afirmativo, calcular el importe del mismo. El criterio es el 
siguiente: para importes menores o iguales que 85, no se hace descuento y para 
importes mayores, se hace el 5 % de descuento. Informar cada importe (nunca cero) con 
su correspondiente descuento y, al final, el porcentaje que representa la cantidad de 
importes que tuvieron descuento, con respecto a la cantidad total de importes.

var: importe, descuento: float; timportes, tdescuento: integer; '''

def CONTADORES():
	global descuento, timportes, tdescuento
	descuento = 0
	timportes = 0
	tdescuento = 0

def CALCULO():
	global descuento, tdescuento, timportes
	if(importe > 85):
		descuento = importe * 0.05
		tdescuento += 1
		print('Aplica descuento')
		print('Total a pagar con descuento: ',importe-descuento)
	else:
		print('No aplica')
		print('Debe abonar: ',importe)
	timportes += timportes + 1

def PORCENTAJE():
	global tdescuento, timportes
	print('Código de vendedor con mayor importe: ',tdescuento/timportes)

CONTADORES()
importe = int(input('Ingrese importe: '))
while (importe != 0):
	CALCULO()
	importe = int(input('Ingrese importe: '))
PORCENTAJE()