# Ejercicio N°13

# Se dan dos valores cualesquiera enteros. Si el primero es mayor que el segundo, 
# restarle al primero un 20%, pero si el segundo es el mayor restarle al segundo un 15%. 
# Con estos nuevos valores, si el primero quedo mayor a 100 y el segundo mayor a 150, 
# se lo consideran valores correctos, de lo contrario es un intervalo de riesgo.

# var valor1, valor2: integer;

valor1 = int(input('Ingrese el primer valor: '))
valor2 = int(input('Ingrese el segundo valor: '))
if (valor1 > valor2):
	valor1 = valor1 - (valor1 * 0.2)
	if(valor1 > 100) and (valor2 > 150):
		print('Valores correctos')
	else:
		print('Intervalo de riesgo')
else:
	valor2 = valor2 - (valor2 * 0.15)
	if(valor2 > 150) and (valor1 > 100):
		print('Valores correctos')
	else:
		print('Intervalo de riesgo')