# Ejercicio N°14

# Calcular cuántos pesos tiene un banco en monedas si dispone de N1 monedas de 1
# peso, N2 de medio peso, N3 de un cuarto de peso, N4 de 10 centavos de peso y N5 de 
# 5 centavos de peso. (N1, N2, N3, N4 y N5 son cantidades)

# var n1: integer; n2, n3, n4, n5, pesos: float;

n1 = int(input('Ingrese monedas de 1 peso: '))
n2 = float(input('Ingrese monedas de medio peso: '))
n3 = float(input('Ingrese monedas de un cuarto de peso: '))
n4 = float(input('Ingrese monedas de 10 centavos: '))
n5 = float(input('Ingrese monedas de 5 centavos: '))
pesos = n1 + (n2 * 0.50) + (n3 * 0.25) + (n4 * 0.10) + (n5 * 0.05)
print('Cantidad de pesos en monedas',pesos)