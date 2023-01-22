# Ejercicio N°6

# Ingresar tres letras mayúsculas y mostrarlas ordenadas alfabéticamente.

# var letra1, letra2, letra3: integer;

letra1 = str(input('Ingrese la primer letra: '))
letra2 = str(input('Ingrese la segunda letra: '))
letra3 = str(input('Ingrese la tercer letra: '))
if (letra1 < letra2 < letra3):
	print('Ordenadas alfabeticamente: ', letra1, ',', letra2,',', letra3)
elif (letra1 < letra3 < letra2):
	print('Ordenadas alfabeticamente: ', letra1, ',', letra3,',', letra2)
elif (letra2 < letra3 < letra1):
	print('Ordenadas alfabeticamente: ', letra2, ',', letra3,',', letra1)
elif (letra2 < letra1 < letra3):
	print('Ordenadas alfabeticamente: ', letra2, ',', letra1,',', letra3)
elif (letra3 < letra1 < letra2):
	print('Ordenadas alfabeticamente: ', letra3, ',', letra1,',', letra2)
elif (letra3 < letra2 < letra1):
	print('Ordenadas alfabeticamente: ', letra3, ',', letra2,',', letra1)
else:
	print('Hay valores repetidos.')