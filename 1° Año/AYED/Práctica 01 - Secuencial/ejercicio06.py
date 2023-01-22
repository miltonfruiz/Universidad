# Ejercicio N°6

# Dadas las medidas de dos ángulos de un triángulo determinar la medida del tercero e
# informar el resultado.

# var ang1, ang2, triangulo: integer;

ang1 = int(input('Ingrese el primer ángulo: '))
ang2 = int(input('Ingrese el segundo ángulo: '))
triangulo = 180 - (ang1 + ang2)
print('El valor del tercer ángulo es: ',triangulo)