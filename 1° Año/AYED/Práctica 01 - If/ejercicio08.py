# Ejercicio N°8

# Se leen tres números positivos. Determinar si son las longitudes de los lados de un
# triángulo: Recordar que en todo triangulo cada lado es menor o igual que la suma de
# los otros dos y menor que su diferencia (basta mostrarlo para un lado). En caso
# afirmativo, informar si el mismo es equilátero (3 lados iguales), isósceles (2 lados
# iguales) o escaleno (3 lados distintos).

# var nro1, nro2, nro3: float;

nro1 = int(input('Ingrese el primer valor de longitud: '))
nro2 = int(input('Ingrese el segundo valor de longitud: '))
nro3 = int(input('Ingrese el tercer valor de longitud: '))
if (nro1 + nro2 + nro3 == 180) and (nro1 > 0 and nro2 > 0 and nro3 > 0):
	if (nro1 == nro2 == nro3):
		print('Los valores ingresados corresponden a un triángulo equilátero.')
	elif (nro1 == nro2 != nro3) or (nro1 == nro3 != nro2):
		print('Los valores ingresados corresponden a un triángulo isósceles.')
	elif (nro1 != nro2 != nro3):
		print('Los valores ingresados corresponden a un triángulo escaleno.')
else:
	print('Los valores ingresados no corresponden a un triángulo.')