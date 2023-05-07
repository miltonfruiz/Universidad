''' Ejercicio N° 4 

Se cuenta con la información brindada por un conjunto de vendedores. Por cada uno de 
ellos se ingresa su código (un carácter distinto de *) y el importe total de sus ventas. 
Determinar el código del vendedor con mayor importe vendido y dicho importe.

var: codigo, importe, mcodigo, mimporte: integer; '''

def CONTADOR():
	global mcodigo, mimporte
	mcodigo = 0
	mimporte = 0

def CALCULO():
	global mimporte, mcodigo
	importe = int(input('Ingrese importe: '))
	if(importe > mimporte):
		mimporte = importe
		mcodigo = codigo

def MOSTRAR():
	global mimporte, mcodigo
	print('Código de vendedor con mayor importe: ',mcodigo)
	print('Importe: ',mimporte)

CONTADOR()
codigo = input('Ingrese codigo: ')
while (codigo != '*'):
	CALCULO()
	codigo = input('Ingrese codigo: ')
MOSTRAR()