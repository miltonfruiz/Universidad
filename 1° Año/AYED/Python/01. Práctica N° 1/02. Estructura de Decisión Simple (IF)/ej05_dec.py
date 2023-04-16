# Ejercicio N°5

# Determinar si el primero de un conjunto de tres números dados, es menor que los otros 
# dos.

# var nro1, nro2, nro3: integer;

nro1 = int(input('Ingresar el primer número: '))
nro2 = int(input('Ingresar el segundo número: '))
nro3 = int(input('Ingresar el tercer número: '))
if (nro1 < nro2) and (nro1 < nro3):
	print('El primer número ingresado es menor que los otros dos.')
else:
	print('El primer número ingresado no es menor que los otros dos.')