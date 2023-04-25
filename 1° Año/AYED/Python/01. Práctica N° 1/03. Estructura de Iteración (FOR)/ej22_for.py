''' Ejercicio N°22

Se cuenta con un texto de 190 caracteres. Determinar cuantas veces aparece la sílaba 
“pa”.
 
var: contador: integer; caracter1, caracter2: string; '''

contador = 0
texto = str(input('Ingrese texto: '))
for i in range(0,len(texto)-1):
	if (texto[i] == 'p' and texto[i+1] == 'a'):
		contador = contador + 1
print('Aparece ',contador,'veces.')