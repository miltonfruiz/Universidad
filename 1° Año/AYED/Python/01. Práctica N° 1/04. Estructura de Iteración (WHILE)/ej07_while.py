''' Ejercicio N° 7

Al finalizar cada día, los vendedores de un comercio rinden al dueño sus ventas para 
calcular la comisión que cobrarán. Los vendedores son 8, codificados de la ‘A’ a la ‘H’, y 
no se sabe cuántas ventas realizó cada uno.
Los datos vienen ordenados y agrupados por vendedor. Por cada vendedor se ingresan 
cada uno de los importes de sus ventas. Para indicar el fin de cada uno de ellos se 
ingresa un valor de venta igual a 0. Se solicita mostrar para cada uno de los vendedores: 
su código y la comisión que cobrará, que es el 2,5 % de la suma de sus ventas.

var: i, codigo: char; venta, tventas: float;'''

def CONTADOR():
	global tventas
	tventas = 0

def CALCULO():
	global tventas
	venta = int(input('Ingrese importe de venta: '))
	while(venta != 0):
		tventas += venta
		venta = int(input('Ingrese importe de venta: '))

def MOSTRAR():
	global tventas
	print('Código vendedor: ',codigo)
	print('Comisión: ',tventas*0.025)

for i in range(1, 9):
	CONTADOR()
	codigo = int(input('Ingrese codigo: '))
	CALCULO()
	MOSTRAR()