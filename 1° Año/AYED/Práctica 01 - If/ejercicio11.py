# Ejercicio N°11

# Dado como dato la cantidad de kilowatios consumidos por un usuario en un mes,
# calcular el importe a pagar por el mismo teniendo en cuenta que:
# Si la cantidad de kilowatios consumidos es menor ó igual a 200, el precio del kilowatio 
# es de 0.05 pesos.
# Si la cantidad de kilowatios consumidos es mayor que 200 y menor que 1000, el precio 
# del kilowatio es de 0.1 pesos.
# Si la cantidad de kilowatios consumidos es mayor ó igual que 1000, el precio del 
# kilowatio es de 0.15 pesos.

# var kilowatio: integer; precio: float;

kilowatio = int(input('Ingrese la cantidad de kilowatios consumidos: '))
if (kilowatio <= 200):
	precio = kilowatio * 0.05
	print('Total a pagar: ', precio,'$')
elif (200 < kilowatio <1000):
	precio = kilowatio * 0.01
	print('Total a pagar: ', precio,'$')
else:
	precio = kilowatio * 0.15
	print('Total a pagar: ',precio,'$')