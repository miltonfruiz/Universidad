''' Ejercicio N° 6

Una empresa tiene 50 viajantes que trabajan en ella. A fin de mes cada uno de los 
viajantes informa su número y los importes de cada una de las ventas realizadas. No se 
sabe la cantidad de ventas que realizó cada uno de ellos por lo que un valor de venta 
igual a cero indica que no hay más ventas de ese vendedor.
Se pide exhibir, para cada uno de los viajantes, el Nro. del viajante y el importe de la 
mayor venta realizada por el mismo.

var: importe: float; mventa, numero: integer; '''

def CONTADOR():
	global mventa
	mventa = 0

def CALCULO():
	global mventa
	if(importe > mventa):
		mventa = importe

CONTADOR()
for i in range(1, 51):
	numero = int(input('Ingrese numero: '))
	importe = int(input('Ingrese importe: '))
	while (importe != 0):
		CALCULO()
		importe = int(input('Ingrese importe: '))
	print('Número de viajante: ',numero,'con mayor venta',mventa)
print('Porcentaje importes con descuento: ',(cimportes/timportes)*100)