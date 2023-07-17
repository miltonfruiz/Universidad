#------------------------------------------------------------> Utilidad <-------------------------------------------------------------

import msvcrt
salto = lambda: print('\n' * 150)

#------------------------------------------------------------> Colores <--------------------------------------------------------------

negro = '\033[30m'
efc = '\033[3;37;41m'
esc = '\033[3;4;31m'
ec = '\033[3;31m'
fan = '\033[2;7;30;43m'
cursiva = '\033[3m'
verde = '\033[32m'
amarillo = '\033[4;33m'
azul = '\033[3;4;34m'
purpura = '\033[35m'
pcyan = '\033[1;36m'
blanco = '\033[4;37m'
reset = '\033[39m'
cierre = '\033[0;m'

#-------------------------------------------------------> Usurios de prueba <--------------------------------------------------------

''' 1 admin@shopping.com       12345      administrador
    4 localA@shopping.com      AAAA1111   dueñoLocal
	6 localB@shopping.com      BBBB2222   dueñoLocal
	9 unCliente@shopping.com   33xx33     cliente     '''


#-----------------------------------------------------------> Búsquedas <------------------------------------------------------------

def buscoUsuario(Usuario,Contraseña,X):
	f = 0
	while((X[f][1] != Usuario) and (X[f][2] != Contraseña) and (f != 3)):
		f = f + 1
	return f

#-----------------------------------------------> Módulos de Opciones de Administrador <---------------------------------------------

def admOpcion():
	print(blanco+'>>> MENÚ ADMINISTRADOR <<<\n'+cierre)
	print('1. Gestión de Locales')
	print('2. Crear cuentas de dueños de locales')
	print('3. Aprobar / Denegar solicitud de descuento')
	print('4. Gestión de Novedades')
	print('5. Reporte de utilización de descuentos')
	print('0. Salir\n')

def admCartel():
	print(cursiva+'En construcción...'+cierre)
	print()
	print(fan+'/ / / / / / / / / / / / / / / / / / / / /'+cierre)
	print()
	print(pcyan+'* Presione una tecla para volver al menú administrador...'+cierre)
	msvcrt.getch()
	salto()

def admInvalida():
	salto()
	print(efc+'x Opción ingresada inválida!'+cierre)
	print()
	print(pcyan+'* Presione una tecla para reintentar...'+cierre)
	msvcrt.getch()
	salto()

#------------------------------------------------------> Módulo Administrador <------------------------------------------------------

def ADMINISTRADOR():
	admOpcion()
	opc = input('> Ingrese una opción: ')
	while(opc != '0'):
		match opc:
			case '1':
				salto()
				print(blanco+'>>> 1. Gestión de Locales\n'+cierre)
			case '2':
				salto()
				print(blanco+'>>> 2. Crear cuentas de dueños de locales\n'+cierre)
				admCartel()
			case '3':
				salto()
				print(blanco+'>>> 3. Aprobar / Denegar solicitud de descuento\n'+cierre)
				admCartel()
			case '4':
				salto()
				print(blanco+'>>> 4. Gestión de Novedades\n'+cierre)
			case '5':
				salto()
				print(blanco+'>>> 5. Reporte de utilización de descuentos\n'+cierre)
				admCartel()
			case '0':
				opc = '0'
			case opc:
				print()
				admInvalida()
		admOpcion()
		opc = input('> Ingrese una opción nuevamente: ')

#---------------------------------------------------------> Módulo Acceso <----------------------------------------------------------

def ACCESO():
	global usuario, contraseña, f, intentos, decision
	print(blanco+'>>> INICIAR SESIÓN <<<'+cierre)
	print()
	usuario = str(input('> Ingrese usuario: '))
	while((len(usuario) > 100) or (len(usuario) < 7)):
		salto()
		print(blanco+'>>> INICIAR SESIÓN <<<'+cierre)
		print()
		print(efc+'x ¡Usuario ingresado inválido. Mínimo 7 caracteres!'+cierre)
		print()
		usuario = str(input('> Ingrese usuario: '))
	salto()
	print(blanco+'>>> INICIAR SESIÓN <<<'+cierre)
	print()
	contraseña = str(input('> Ingrese contraseña: '))
	while((len(contraseña) > 8) or (len(contraseña) < 3)):
		salto()
		print(blanco+'>>> INICIAR SESIÓN <<<'+cierre)
		print()
		print(efc+'x ¡Contraseña ingresada inválida. Mínimo 4 dígitos!'+cierre)
		print()
		contraseña = str(input('> Ingrese contraseña: '))
	salto()
	f = buscoUsuario(usuario,contraseña,D)
	if (D[f][1] == usuario and D[f][2] == contraseña):
		print()
		match D[f][3]:
			case 'administrador':
				ADMINISTRADOR()
			case 'dueñoLocal':
				print('DUEÑO LOCAL')
			case 'cliente':
				print('CLIENTE')
		print()
		salto()
	else:
		if((usuario == D[f][1]) and (contraseña != D[f][2])):
			print()
			print(efc+'x ¡Contraseña ingresada incorecta!'+cierre)
			print('__________________________________')
			print()
			print(esc+'x Contraseña:'+cierre,ec+contraseña+cierre)
			print()
		elif((usuario != D[f][1]) and (contraseña == D[f][2])):
			print()
			print(efc+'x ¡El usuario ingresado no está registrado!'+cierre)
			print('___________________________________________')
			print()
			print(esc+'x Usuario:'+cierre,ec+usuario+cierre)
			print()
		elif((usuario != D[f][1]) and (contraseña != D[f][2])):
			print()
			print(efc+'x ¡Los datos ingresados son incorrectos!'+cierre)
			print('________________________________________')
			print()
			print(esc+'x Usuario:'+cierre,ec+usuario+cierre)
			print(esc+'x Contraseña:'+cierre,ec+contraseña+cierre)
			print()
		intentos = intentos - 1
		print(ec+'Le quedan',intentos,'intentos.'+cierre)
		print()
		print(pcyan+'* Presione una tecla para continuar...'+cierre)
		msvcrt.getch()
		salto()
	if(intentos != 0):
		print(blanco+'>>> INICIAR SESIÓN <<<'+cierre)
		print()
		decision = input('¿Desea continuar en el programa? S / N \n\n> ').upper()
		print()
		salto()
		while (decision != 'N') and (decision != 'S'):
			print()
			print(blanco+'>>> INICIAR SESIÓN <<<'+cierre)
			print()
			print(efc+'x ¡Carácter ingresado inválido, ingrese S o N!'+cierre)
			print()
			decision = input('¿Desea continuar en el programa? S / N \n\n> ').upper()
			salto()
	else:
		print(efc+'x !Ha alcanzado el límite de intentos!'+cierre)
		print('______________________________________')
		print()
		print(pcyan+'* Presione una tecla para cerrar sesion... '+cierre)
		msvcrt.getch()


#-------------------------------------------------------> Programa Principal <-------------------------------------------------------

def PROGRAMA():
	global intentos, decision
	intentos = 3
	salto()
	print(blanco+'>>> B I E N V E N I D O  <<<'+cierre)
	print()
	decision = input('¿Desea iniciar sesion? S / N \n\n> ').upper()
	print()
	while (decision != 'N') and (decision != 'S'):
		salto()
		print(blanco+'>>> B I E N V E N I D O  <<<'+cierre)
		print()
		print(efc+'x ¡Carácter ingresado inválido, ingrese S o N!'+cierre)
		print()
		decision = input('¿Desea iniciar sesion? S / N \n\n> ').upper()
	salto()
	while(decision != 'N' and intentos != 0):
		ACCESO()
	salto()
	print('¡Gracias por su visita!\n')
	msvcrt.getch()

#------------------------------------------------------->  Carga de Arreglos <-------------------------------------------------------

'''type datos: array[0..99,0..3] of string;
        locales: array[0..49,0..3] of string;
        mapa: array[1..10,1..5] of integer;
        cusuario: array[1..100] of integer;
        clocal: array[1..50] of integer;
        cantidad: array[1..3] of integer;
        rubro: array[1..3] of string;
	var D: datos;
		l: locales;
		m: mapa;
		c: cantidad;
		r: rubro;
		cus: cusuario;
    	clo: clocal;
    	dec: char;
    	int: integer;'''

def cargoUsuarios():
	global D
	datos = [
		['1','admin@shopping.com','12345','administrador'],
		['4','localA@shopping.com','AAAA1111','dueñoLocal'],
		['6','localB@shopping.com','BBBB2222','dueñoLocal'],
		['9','unCliente@shopping.com','33xx33','cliente'],
	  ]
	D = ['']*4
	for i in range(4):
		D[i] = datos[i]

def INICIO():
	cargoUsuarios()

#------------------------------------------------------------> Ejecución <-----------------------------------------------------------

INICIO()
PROGRAMA()