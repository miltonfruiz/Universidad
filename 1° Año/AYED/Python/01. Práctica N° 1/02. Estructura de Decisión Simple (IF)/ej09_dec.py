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
if (cliente == 'l') or (cliente == 'p'):
	cantidad = int(input('Ingrese la cantidad de libros: '))
	importe = float(input('Ingrese el importe: '))
	if(cliente == 'l'):
		if (0 < cantidad <= 24):
			bonificacion = (importe * 0.2)
		else:
			bonificacion = (importe * 0.25)
	else:
		if(cantidad < 6):
			bonificacion = importe
		else:
			if(6 <= cantidad <= 18):
				bonificacion = importe * 0.05
			else:
				bonificacion = importe * 0.10
	importeBonificado = importe - bonificacion
	print('Debe abonar:',importeBonificado)
else:
	print('Tipo de cliente ingresado incorrecto')
