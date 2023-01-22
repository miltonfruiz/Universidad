# Ejercicio N°1

# Dados dos números distintos, mostrarlos ordenados en forma creciente.

# var nro1, nro2: integer;

nro1 = int(input('Ingrese el primer número: '))
nro2 = int(input('Ingrese el segundo número: '))
if (nro1 > nro2):
	print('Los valores ingresados en forma creciente son: ', nro2,',', nro1)
elif (nro1 < nro2):
	print('Los valores ingresados en forma creciente son: ', nro1,',', nro2)
else:
	print('Los valores ingresados son iguales.')