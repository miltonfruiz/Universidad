# Ejercicio N°14

# Se dan dos valores cualesquiera enteros. Si el primero es mayor que el segundo, 
# restarle al primero un 20%, pero si el segundo es el mayor restarle al segundo un 15%. 
# Con estos nuevos valores, si el primero quedo mayor a 100 y el segundo mayor a 150, 
# se lo consideran valores correctos, de lo contrario es un intervalo de riesgo.

# var valor1, valor2: integer;

valor1 = int(input('Ingrese el primer valor: '))
valor2 = int(input('Ingrese el segundo valor: '))
if (valor1 > valor2):
	valor1 = valor1 - (valor1 * 0.2)
else:
	valor2 = valor2 - (valor2 * 0.15)

if (valor1 > 100) and (valor2 > 150):
	print('Los valores son correctos.')
else:
	print('Es un intervalo de riesgo.')