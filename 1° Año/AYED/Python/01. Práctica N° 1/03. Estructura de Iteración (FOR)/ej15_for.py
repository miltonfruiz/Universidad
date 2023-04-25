''' Ejercicio N°15

Generar e informar los primeros 23 términos de la sucesión de Fibonacci. Tener en
cuenta que los dos primeros términos son iguales a uno y que los restantes se
obtienen como la suma de los dos anteriores.

var: termino1, termino2, i, prox: integer; '''

termino1 = 1
termino2 = 1
print(termino1)
print(termino2)
for i in range(1,21):
	prox = termino1 + termino2
	termino1 = termino2
	termino2 = prox
	print(prox)