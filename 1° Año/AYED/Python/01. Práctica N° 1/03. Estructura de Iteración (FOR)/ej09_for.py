''' Ejercicio N°9

Se dan como datos los importes de las 200 ventas de una librería. Se desea saber:
· Cuántas ventas tuvieron importes menores que $ 100.
· Cuál es el monto total de las ventas cuyo importe fue igual o mayor que $ 100.-

var: cont, monto, i: integer; ventas: float '''

menores = 0
monto = 0
for i in range(1, 201):
	ventas = float(input('Ingrese el valor de la venta: '))
	if ventas < 100:
		menores = menores + 1
	else:
		monto = monto + ventas
print('Total importes menores a $ 100: ',menores)
print('Monto total de las ventas mayor o igual $ 100: ',monto)