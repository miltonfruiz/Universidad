''' Ejercicio N° 9 

Ingresar una secuencia ordenada alfabéticamente de letras con repeticiones. Informar 
cada carácter y la cantidad de veces que aparece en la lista. La secuencia finaliza con 
un ‘*’

var: aux, letra: char;'''

def CONTADOR():
	global aux, tletra
	aux = ''
	tletra = 0

def CALCULO():
	global aux, letra, tletra
	aux = letra
	while(aux == letra):
		tletra += 1
		letra = input('Ingrese letra: ')

def MOSTRAR():
	global tletra, aux
	print('La letra: ',aux)
	print('Aparece: ',tletra)

letra = input('Ingrese letra: ')
while(letra != '*'):
	CONTADOR()
	CALCULO()
	MOSTRAR()