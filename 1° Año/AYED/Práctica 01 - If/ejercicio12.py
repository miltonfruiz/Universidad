# Ejercicio N°12

# Se ingresan seis números positivos diferentes. Al final mostrar un cartel que diga: “El
# mayor número ingresado fue el xxx” 

# var nro1, nro2, nro3, nro4, nro5, nro6: integer;

nro1 = int(input('Ingrese el primer número: '))
nro2 = int(input('Ingrese el segundo número: '))
nro3 = int(input('Ingrese el tercer número: '))
nro4 = int(input('Ingrese el cuarto número: '))
nro5 = int(input('Ingrese el quinto número: '))
nro6 = int(input('Ingrese el sexto número: '))
mayor = 0
if (nro1 > 0 , nro2 > 0 , nro3 > 0 , nro4 > 0 , nro5 > 0 , nro6 > 0 ) and (mayor >= 0):
	if (nro1 != nro2 and nro2 != nro3 and nro3 != nro4 and nro4 != nro5 and nro5 != nro6):
		if (nro1 < nro2):
			mayor = nro2
		if (mayor < nro3):
			mayor = nro3
		if (mayor < nro4):
			mayor = nro4
		if (mayor < nro5):
			mayor = nro5
		if (mayor < nro6):
			mayor = nro6
		print('El mayor valor ingresado es: ', mayor)
	else:
		print('Valor ingresado repetido.')
else:
	print('¡¡Los valores ingresados deben ser positivos!!')