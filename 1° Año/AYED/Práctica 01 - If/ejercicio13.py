# Ejercicio N°13

# El mismo que el anterior, pero indicar la posición en que entró el mayor. (Ej. “El mayor 
# fue xx y fue ingresado quinto”

# var nro1, nro2, nro3, nro4, nro5, nro6: integer; posicion: string;

nro1 = int(input('Ingrese el primer número: '))
nro2 = int(input('Ingrese el segundo número: '))
nro3 = int(input('Ingrese el tercer número: '))
nro4 = int(input('Ingrese el cuarto número: '))
nro5 = int(input('Ingrese el quinto número: '))
nro6 = int(input('Ingrese el sexto número: '))
if (nro1 > 0 and nro2 > 0 and nro3 > 0 and nro4 > 0 and nro5 > 0 and nro6 > 0 ):
	if (nro1 != nro2 and nro2 != nro3 and nro3 != nro4 and nro4 != nro5 and nro5 != nro6):
		mayor = 0
		if (mayor < nro1):
			mayor = nro1
			posicion = "primer"
		if (nro1 < nro2):
			mayor = nro2
			posicion = "segunda"
		if (mayor < nro3):
			mayor = nro3
			posicion = "tercera"
		if (mayor < nro4):
			mayor = nro4
			posicion = "cuarta"
		if (mayor < nro5):
			mayor = nro5
			posicion = "quinta"
		if (mayor < nro6):
			mayor = nro6
			posicion = "Sexta"
		print('El mayor valor ingresado es ', mayor,'y esta en', posicion, 'posicion.')
	else:
		print('Valor ingresado repetido.')
else:
	print('¡¡Los valores ingresados deben ser positivos!!')