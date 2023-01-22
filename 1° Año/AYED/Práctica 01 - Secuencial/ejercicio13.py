# Ejercicio N°13

# Dado el importe bruto de una factura calcular el resultado de bonificarlo (descuento)
# con un 4%. Al monto obtenido calcularle el IVA (21%). Finalmente informar: el importe
# bruto, el valor de la bonificación, el importe bruto bonificado, el monto correspondiente
# al IVA y el importe neto resultante.

# var importe, descuento, iva: float;

importe = float(input('Ingrese el importe bruto: '))
descuento = importe * 0.04
iva = descuento * 0.21
print('El importe bruto es',importe,', la bonificacion',descuento,', bruto bonificado',importe+descuento,', el IVA',iva,'y el neto',importe-descuento)