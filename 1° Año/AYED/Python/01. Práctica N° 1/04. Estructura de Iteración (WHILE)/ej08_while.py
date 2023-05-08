''' Ejercicio N° 8

Se desea saber el total de ventas de cada uno de los vendedores de una empresa. A tal 
fin se tienen como datos: el código de vendedor y el importe de cada una de las ventas; 
un vendedor puede haber realizado más de una venta. No se sabe la cantidad de 
vendedores que tiene la empresa ni la cantidad de ventas hechas por cada vendedor (un
código de vendedor igual a cero es fin de datos). ESTOS DATOS ESTAN ORDENADOS 
POR CODIGO DE VENDEDOR. Exhibir cada código de vendedor y su total 
correspondiente y al final, el código de vendedor con mayor importe vendido y dicho 
importe.

var: codigo, aux: integer; importe, mayor, tventa: float;'''

def CONTADOR():
	global tventas, mayor
	tventas = 0
	mayor = 0

def CALCULO():
	global aux, tventas, mayor, codigo
	aux = codigo
	while(aux == codigo):
		importe = int(input('Ingrese importe: '))
		tventas += + 1
		if(importe > mayor):
			mayor = importe
			mcodigo = codigo
		codigo = int(input('Ingrese codigo: '))

def MOSTRAR():
	global tventas
	print('Código: ',aux)
	print('Total ventas: ',tventas)

def MAYOR():
	global mcodigo, mayor
	print('Código vendedor con mayor importe: ',mcodigo)
	print('Importe: ',mayor)

CONTADOR()
codigo = int(input('Ingrese codigo: '))
while(codigo != 0):
	CALCULO()
	MOSTRAR()
MAYOR()