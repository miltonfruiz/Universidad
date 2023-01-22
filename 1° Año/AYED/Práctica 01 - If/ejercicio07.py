# Ejercicio N°7

# Se desea controlar en una fábrica la calidad de dos tipos de piezas que
# denominaremos A y B.
# a. Se dan como datos el tipo de pieza y su medida en milímetros.
# b. Se debe indicar si cumple con las especificaciones sabiendo que 
# c. Las piezas de tipo A deben medir 165 mm y se admite un error de +/-2 mm.
# d. Las piezas de tipo B deben medir 180 mm y se admite un error de +/-3 mm.

# var pieza: string; medida: float;

pieza = str(input('Ingrese el tipo de pieza: A o B: '))
if (pieza == 'A') or (pieza == 'a'):
	medida = float(input('Ingrese la medida de la pieza: '))
	if (163 <= medida <= 167):
		print('La pieza "A" ingresada cumple con las especificaciones.')
	else:
		print('La pieza ingresada no cumple con las especificaciones.')
elif (pieza == 'B') or (pieza == 'b'):
	medida = float(input('Ingrese la medida de la pieza: '))
	if (177 <= medida <= 183):
		print('La pieza "B" ingresada cumple con las especificaciones.')
	else:
		print('La pieza "B" ingresada no cumple con las especificaciones.')
else:
	print('El tipo de pieza ingresado es inválido.')