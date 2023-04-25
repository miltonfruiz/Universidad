''' Ejercicio N°19

Dada una sucesión de N números enteros ordenados en forma creciente, no
consecutivos, hallar la máxima diferencia entre dos números sucesivos

var: mdif, N, numero, i, siguiente, dif: integer; '''

anterior = 0
diferencia = 0
N = int(input("Ingrese cantidad de números de la secuencia: "))
for i in range(1, N+1):
	numero = int(input("Ingrese el siguiente número: "))
	if diferencia < (numero - anterior):
		diferencia = numero - anterior
	anterior = numero
print("La máxima diferencia entre dos números es:", diferencia)