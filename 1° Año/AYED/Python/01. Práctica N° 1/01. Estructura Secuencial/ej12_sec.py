# Ejercicio N°12

# Determinar el número de horas, minutos y segundos que hay en 6250 segundos. 

# var hs, mins, seg: integer;

hs = 6250 // 3600
mins = (6250 % 3600) // 60
seg = (6250 % 3600) - (mins*60)
print('En 6250 segundos hay:',hs,'Horas,',mins,'minutos y',seg,'segundos')