# Ejercicio N°9-10

# Una distribuidora de libros vende a librerías y a particulares. Aplica bonificaciones por
# cantidad según el siguiente criterio:
# Librerías: hasta 24 unidades, el 20%; más de 24 unidades, el 25%.
# Particulares: menos de 6 unidades, nada; desde 6 hasta 18 unidades, el 5%; 
# y más de 18 unidades, el 10%.
# El tipo de cliente está codificado: 'L' para librerías, 'P' para particular.
# Dado el importe bruto total de una compra de libros, el tipo de cliente y la cantidad
# total pedida por el mismo, determinar el importe bruto bonificado.

# var cliente: string; cantidad: integer; precio: float;

cliente = str(input('Ingrese el tipo de cliente: "L" o "P" : '))
if (cliente == "L"):
	cantidad = int(input('Ingrese la cantidad de libros: '))
	precio = float(input('Ingrese el precio: '))
	if (cantidad <= 24):
		importe = (cantidad * precio * 0.8)
	else:
		importe = (cantidad * precio * 0.75)
	print('Importe bruto bonificado: ', importe)
elif (cliente == "P"):
	cantidad = int(input('Ingrese la cantidad de libros: '))
	precio = float(input('Ingrese el precio: '))
	if (cantidad < 6):
		importe = (cantidad * precio)
	elif (6 < cantidad < 18):
		importe = (cantidad * precio * 95)
	else:
		importe = (cantidad * precio * 0.9)
	print('Importe bruto bonificado: ', importe)
else:
	print('El cliente ingresado es inválido.')