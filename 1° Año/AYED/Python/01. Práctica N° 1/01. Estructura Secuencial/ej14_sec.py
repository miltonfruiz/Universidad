# Ejercicio N°14

# Calcular cuántos pesos tiene un banco en monedas si dispone de N1 monedas de 10
# pesos, N2 de la mitad de pesos de N1, N3 de un cuarto peso de N1, y N4 de 1 peso. (N1, 
# N2, N3 y N4 son cantidades)

# var n1: integer; n2, n3, n4, n5, pesos: float;

n1 = int(input('Ingrese monedas de 10 pesos: '))
n2 = float(input('Ingrese monedas de 5 pesos: '))
n3 = float(input('Ingrese monedas de 2,50 pesos: '))
n4 = float(input('Ingrese monedas de 1 peso: '))
pesos = n1 + (n2 * 0.50) + (n3 * 0.25) + (n4 * 0.10)
print('Cantidad de pesos en monedas',pesos)