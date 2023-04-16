# Ejercicio N°15

# .Ingresar 3 valores en 3 variables X,Y y Z. Se desea obtener una rotación de sus
# valores, es decir que el contenido de Z pase a X, el contenido de X pase a Y, y el
# contenido de Y pase a Z. Se debe mostrar las variables X, Y y Z con sus valores
# originales y mostrar X, Y y Z con los valores luego de la rotación.

# var x, y, z, aux: integer;

x = int(input('Ingrese el valor de X: '))
y = int(input('Ingrese el valor de Y: '))
z = int(input('Ingrese el valor de Z: '))
print('El valor de X es',x,', de Y es',y,'y de Z es',z)
aux = x
x = z
y = aux
z = y
print('El valor rotado de X es',x,', el de Y es',y,'y el de Z es',z)