# Ejercicio N°7

# Dado el valor del lado de un cuadrado calcular su perímetro y su superficie, e informar
# los mismos con carteles aclaratorios.

# var lado, perimetro, superficie: integer;

lado = int(input('Ingrese valor del lado de cuadrado: '))
perimetro = lado * 4
superficie = lado * lado
print('El perimetro es ',perimetro,'y su superficie es ',superficie)