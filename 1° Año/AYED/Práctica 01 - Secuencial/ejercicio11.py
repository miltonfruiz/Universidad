# Ejercicio N°11

# Calcular el sueldo de un operario conociendo la cantidad de horas que trabajó en el
# mes y el jornal horario.

# var horas: integer; jornal, sueldo: float;

horas = int(input('Ingrese la cantidad de horas que trabajó: '))
jornal = float(input('Ingrese jornal horario: '))
sueldo = horas * jornal
print('El sueldo es: ',sueldo)