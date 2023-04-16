# Ejercicio N°6

# Ingresar tres letras mayúsculas y mostrarlas ordenadas alfabéticamente.

# var letra1, letra2, letra3: integer;

A = str(input('Ingrese la primer letra: '))
B = str(input('Ingrese la segunda letra: '))
C = str(input('Ingrese la tercer letra: '))
if (A < B):
    if(B < C):
        print(A,B,C)
    else:
        if(A < C):
            print(A,C,B)
        else:
            print(C,A,B)
else:
    if(B < C):
        if(A < C):
            print(B,A,C)
        else:
            print(B,C,A)
    else:
        print(C,B,A)