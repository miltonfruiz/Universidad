#------------------------------------------------------------> Utilidad <-------------------------------------------------------------
import os
import msvcrt
salto = lambda: os.system('cls')

#------------------------------------------------------------> Colores <--------------------------------------------------------------

negro = '\033[30m'
efc = '\033[2;37;41m'
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

#-------------------------------------------------------> Usurios de prueba <-----------------------------------------------------

''' 1 admin@shopping.com       12345      administrador
    4 localA@shopping.com      AAAA1111   dueñoLocal
	6 localB@shopping.com      BBBB2222   dueñoLocal
	9 unCliente@shopping.com   33xx33     cliente     '''

#-----------------------------------------------------------> Extras <------------------------------------------------------------

#funcion para opcines y titulos parametrizados
def opcionGestion(opc,x):
	print(blanco+'>>>',opc,')',x,'LOCAL'+cierre)
	print()

def desea(opcion,titulo,pregunta):
	global des
	print('¿Desea',pregunta,'local? S / N')
	print()
	des = input('>').upper()
	print()
	while (des != 'N') and (des != 'S'):
		caracterInvalido()
		opcionGestion(opcion,titulo)
		print('¿Desea',pregunta,'local? S / N')
		print()
		des = input('>').upper()
		print()

#-----------------------------------------------------------> Búsquedas <------------------------------------------------------------

def buscoUsuario(Usuario,Contraseña,X):
	f = 0
	while((X[f][1] != Usuario) and (X[f][2] != Contraseña) and (f != 3)):
		f = f + 1
	return f

#------------------------------------------------------------> Títulos <-------------------------------------------------------------

def tituloIniciar():
	print(blanco+'>>> INICIAR SESIÓN <<<'+cierre)
	print()

def tituloBienvenida():
	salto()
	print(blanco+'>>> B I E N V E N I D O  <<<'+cierre)
	print()

#-------------------------------------------------------> Opciones Inválidos <-------------------------------------------------------

def continuar():
	print()
	print(pcyan+'* Presione una tecla para continuar...'+cierre)
	msvcrt.getch()
	salto()

def reintentar():
	print()
	print(pcyan+'* Presione una tecla para reintentar...'+cierre)
	msvcrt.getch()
	salto()

def usuarioInvalido():
	salto()
	tituloIniciar()
	print(ec+'x !Debe contener mínimo 7 caracteres!'+cierre)
	print()

def contraseñaInvalida():
	salto()
	tituloIniciar()
	print(ec+'x !Debe contener mínimo 4 caracteres!'+cierre)
	print()

def admInvalida():
	salto()
	print(ec+'x Opción ingresada inválida!'+cierre)
	reintentar()

def caracterInvalido():
	salto()
	print(ec+'x ¡Carácter ingresado inválido, ingrese S o N!'+cierre)
	reintentar()

#-------------------------------------------------> Opciones de Gestión de Locales <-------------------------------------------------

def muestroLocales():
	global decs,c
	opcionGestion('a','CREAR')
	decs = input('¿Desea ver locales cargados? S / N \n\n> ').upper()
	print()
	while (decs != 'N') and (decs != 'S'):
		caracterInvalido()
		opcionGestion('a','CREAR')
		decs = input('¿Desea ver locales cargados? S / N \n\n> ').upper()
	salto()
	if(decs == 'S') and (L[0][0] != ''):
		opcionGestion('a','CREAR')
		print('NOMBRE       UBICACIÓN       RUBRO       ESTADO')
		print('-----------------------------------------------')
		for f in range(4):
			print(L[f][0],'     ',L[f][1],'      ',L[f][2],'    ',L[f][3])
		continuar()
	else:
		print(ec+'Por el momento no se han cargado locales.'+cierre)
		continuar()
	salto()


def CREAR():
	global tlocales
	tlocales = 0
	muestroLocales()
	opcionGestion('a','CREAR')
	desea('a','CREAR','crear')
	while(des !='N') and (tlocales != 50):
		salto()
		opcionGestion('a','CREAR')
		L[f][0] = input('> Ingrese nombre: ')
		while((len(L[f][0]) > 100) or (len(L[f][0]) < 2)):
			salto()
			print(ec+'x !El nombre debe contener mínimo 3 caracteres!'+cierre)
			reintentar()
			opcionGestion('a','CREAR')
			L[f][0]= input('> Ingrese nombre nuevamente: ')
		L[f][1] = input('> Ingrese ubicación: ')
		L[f][2] = input('> Ingrese rubro: ')
		L[f][3] = input('> Ingrese estado: ')
		salto()
		desea('a','CREAR','crear')
		salto()
	salto()



#----------------------------------------------------> Opciones de Administrador <---------------------------------------------------

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

def localOpcion():
	print(blanco+'>>> 1. GESTIÓN DE LOCALES\n'+cierre)
	print('        a) Crear local')
	print('        b) Modificar local')
	print('        c) Eliminar local')
	print('        d) Mapa local')
	print('        e) Volver\n')

def admLocales():
	localOpcion()
	opcl = input('> Ingrese una opción: ').upper()
	while(opcl != 'E'):
		match opcl:
			case 'A':
				salto()
				CREAR()
			case 'B':
				salto()
				print('Modificar localesssssssssss')
			case 'C':
				salto()
				print('Eliminar localessssssssssssssssss')
			case 'D':
				salto()
				print('Mapa de localllllllllllllll')
			case 'E':
				salto()
				opcl = 'E'
			case opcl:
				print()
				admInvalida()
		localOpcion()
		opcl = input('> Ingrese una opción: ').upper()

#------------------------------------------------------> Módulo Administrador <------------------------------------------------------

def ADMINISTRADOR():
	admOpcion()
	opc = input('> Ingrese una opción: ')
	while(opc != '0'):
		match opc:
			case '1':
				salto()
				admLocales()
				salto()
			case '2':
				salto()
				print(blanco+'>>> 2. CREAR CUENTAS DE DUEÑOS DE LOCALES\n'+cierre)
				admCartel()
			case '3':
				salto()
				print(blanco+'>>> 3. APROBAR / DENEGAR SOLICITUD DE DESCUENTO\n'+cierre)
				admCartel()
			case '4':
				salto()
				print(blanco+'>>> 4. GESTIÓN DE NOVEDADES\n'+cierre)
			case '5':
				salto()
				print(blanco+'>>> 5. REPORTE DE UTILIZACIÓN DE DESCUENTOS\n'+cierre)
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
	tituloIniciar()
	usuario = str(input('> Ingrese usuario: '))
	while((len(usuario) > 100) or (len(usuario) < 7)):
		usuarioInvalido()
		usuario = str(input('> Ingrese usuario nuevamente: '))
	salto()
	tituloIniciar()
	contraseña = str(input('> Ingrese contraseña: '))
	while((len(contraseña) > 8) or (len(contraseña) < 4)):
		contraseñaInvalida()
		contraseña = str(input('> Ingrese contraseña nuevamente: '))
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
		tituloIniciar()
		decision = input('¿Desea continuar en el programa? S / N \n\n> ').upper()
		print()
		salto()
		while (decision != 'N') and (decision != 'S'):
			print()
			tituloIniciar()
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
	tituloBienvenida()
	decision = input('¿Desea iniciar sesion? S / N \n\n> ').upper()
	print()
	while (decision != 'N') and (decision != 'S'):
		caracterInvalido()
		tituloBienvenida()
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
        cusuario: array[0..49] of integer;
        clocal: array[1..50] of integer;
        cantidad: array[1..3] of integer;
        rubro: array[1..3] of string;
	var D: datos;
		L: locales;
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

def cargoLocales():
	global L
	L = ['']*4
	for f in range(4):
		L[f] = ['']*4

def INICIO():
	cargoUsuarios()
	cargoLocales()

#------------------------------------------------------------> Ejecución <-----------------------------------------------------------

INICIO()
PROGRAMA()