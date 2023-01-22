# Ejercicio N°3

# Dada la medida de cada uno de los tres ángulos de un triángulo determinar e informar 
# mediante un mensaje si pertenecen o no a un triángulo rectángulo.

# var ang1, ang2, ang3: float;

ang1 = float(input('Ingrese el valor del primer ángulo: '))
ang2 = float(input('Ingrese el valor del segundo ángulo: '))
ang3 = float(input('Ingrese el valor del tercer ángulo: '))
if (ang1 + ang2 + ang3 == 180):
	if (ang1 == 90 or ang2 == 90 or ang3 == 90) and (ang1 > 0 and ang2 > 0 and ang3 > 0):
		print('Los valores ingresados pertenecen a un triángulo rectángulo.')
	else:
		print('Los valores ingresados no pertenecen un triángulo rectángulo.')
else:
	print('Los valores ingresados no pertenecen a un triángulo.')