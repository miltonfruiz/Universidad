# Ejercicio N°4

# Ingresar tres números enteros distintos. Determinar y mostrar si ingresaron en orden
# creciente.

# var nro1, nro2, nro3: integer;

nro1 = int(input('Ingresar el primer número: '))
nro2 = int(input('Ingresar el segundo número: '))
nro3 = int(input('Ingresar el tercer número: '))
if (nro1 < nro2 < nro3):
	print('Se ingresaron en forma creciente los siguientes valores: ',nro1,',', nro2,',', nro3)
else:
	print('Los valores ingresados no están en orden creciente.')