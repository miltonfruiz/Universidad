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
cvc = '\033[3;32m'
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

#funcion para opciones y titulos
def opcionGestion(opc,x):
	print(blanco+'>>>',opc,x,'LOCAL'+cierre+'\n')

def desea(opcion,titulo,pregunta):
	global des
	print('¿Desea',pregunta,'local? S / N\n')
	des = input('> ').upper()
	while (des != 'N') and (des != 'S'):
		caracterInvalido()
		opcionGestion(opcion,titulo)
		print('¿Desea',pregunta,'local? S / N\n')
		des = input('> ').upper()

#-----------------------------------------------------------> Búsquedas <------------------------------------------------------------

def buscoUsuario(Usuario,Contraseña,X):
	f = 0
	while((X[f][1] != Usuario) and (X[f][2] != Contraseña) and (f != 3)):
		f = f + 1
	return f

def buscoNombre(X,nombre):
	f = 0
	while((X[f][0] != nombre) and (f != 3)):
		f = f + 1
	return f

def buscoCodigo(X,codigo):
	f = 0
	while((X[f][0] != codigo) and (f != 3)):
		f = f + 1
	return f

def buscoRubro(X,rubro):
	f = 0
	while((X[f] != rubro) and (f != 2)):
		f = f + 1
	return f

#------------------------------------------------------------> Títulos <-------------------------------------------------------------

def tituloIniciar():
	print(blanco+'>>> INICIAR SESIÓN <<<'+cierre+'\n')

def tituloBienvenida():
	salto()
	print(blanco+'>>> B I E N V E N I D O  <<<'+cierre+'\n')

#-------------------------------------------------------> Opciones Inválidos <-------------------------------------------------------

def presione(accion):
	print()
	print(pcyan+'* Presione una tecla para',accion,'...'+cierre)
	msvcrt.getch()
	salto()

def usuarioInvalido():
	salto()
	tituloIniciar()
	print(ec+'x !Debe contener mínimo 7 caracteres!'+cierre+'\n')

def contraseñaInvalida():
	salto()
	tituloIniciar()
	print(ec+'x !Debe contener mínimo 4 caracteres!'+cierre+'\n')

def admInvalida():
	salto()
	print(ec+'x Opción ingresada inválida!'+cierre)
	presione('reintentar')

def caracterInvalido():
	salto()
	print(ec+'x ¡Carácter ingresado inválido, ingrese S o N!'+cierre)
	presione('reintentar')

#---------------------------------------------------------> Ordenamientos <----------------------------------------------------------

def ordenoCantidad(Y,W):
	for i in range(0,2):
		for j in range(i+1,3):
			if(Y[i] < Y[j]):
				aux1 = Y[i]
				Y[i] = Y[j]
				Y[j] = aux1
				aux2 = W[i]
				W[i] = W[j]
				W[j] = aux2

#-------------------------------------------------> Opciones de Gestión de Locales <-------------------------------------------------

def validoNombre(letra,opcion,cadena,minimo,X):
	global nombre, n
	salto()
	opcionGestion(letra,opcion)
	nombre = input('> Ingrese nombre: ')
	while((len(nombre) > 50) or (len(nombre) < 2)):
		salto()
		print(ec+'x ',cadena,'debe contener mínimo',minimo,'caracteres!'+cierre)
		presione('reintentar')
		opcionGestion(letra,opcion)
		nombre = input('> Ingrese nombre nuevamente: ')
	n = buscoNombre(X,nombre)

def validoUbicación(letra,opcion,cadena,minimo,X):
	salto()
	opcionGestion(letra,opcion)
	X[tl][1] = input('> Ingrese ubicación: ')
	while((len(X[tl][1]) > 50) or (len(X[tl][1]) < 1)):
		salto()
		print(ec+'x ',cadena,'debe contener mínimo',minimo,'caracteres!'+cierre)
		presione('reintentar')
		opcionGestion(letra,opcion)
		X[tl][1] = input('> Ingrese ubicación nuevamente: ')

def validoRubro(letra,opcion,cadena,X):
	salto()
	opcionGestion(letra,opcion)
	X[tl][2] = input('> Ingrese rubro: ').capitalize()
	while(X[tl][2] != 'Comida') and (X[tl][2] != 'Indumentaria') and (X[tl][2] != 'Perfumeria'):
		salto()
		print(ec+'x ',cadena,'ingresado debe ser comida, indumentria o perfumeria!'+cierre)
		presione('reintentar')
		opcionGestion(letra,opcion)
		X[tl][2] = input('> Ingrese rubro nuevamente: ').capitalize()

def validoCodigo(letra,opcion,cadena,minimo,X):
	global codigo, c
	salto()
	opcionGestion(letra,opcion)
	codigo = input('> Ingrese codigo: ')
	while(codigo == '0'):
		salto()
		print(ec+'x ',cadena,'ingresado debe ser distinto de',minimo,+cierre)
		presione('reintentar')
		opcionGestion(letra,opcion)
		codigo = input('> Ingrese codigo nuevamente: ')
	c = buscoCodigo(X,codigo)

def muestroDescendente(Y,W):
	opcionGestion('a)','CREAR')
	print('     CANTIDAD              RUBRO\n'' ------------------------------------')
	for i  in range(3):
		if(Y[i] != 0):
			print('       ',Y[i],'             ',W[i])

def sumoLocal(Y,W,tipo):
	t = buscoRubro(W,tipo)
	match W[t]:
		case 'Comida':
			Y[t] = Y[t] + 1
		case 'Indumentaria':
			Y[t] = Y[t] + 1
		case 'Perfumeria':
			Y[t] = Y[t] + 1
	ordenoCantidad(Y,W)
	muestroDescendente(Y,W)

def muestroLocales():
	global decs,c
	opcionGestion('a)','CREAR')
	decs = input('¿Desea ver locales cargados? S / N \n\n> ').upper()
	print()
	while (decs != 'N') and (decs != 'S'):
		caracterInvalido()
		opcionGestion('a)','CREAR')
		decs = input('¿Desea ver locales cargados? S / N \n\n> ').upper()
	salto()
	if(decs == 'S') and (L[0][0] != ''):
		opcionGestion('a)','CREAR')
		print('NOMBRE       UBICACIÓN       RUBRO       ESTADO')
		print('-----------------------------------------------')
		for f in range(50):
			if(L[f][0] != ''):
				print(L[f][0],'     ',L[f][1],'      ',L[f][2],'    ',L[f][3])
		presione('continuar')
	elif(decs == 'S') and (L[0][0] == ''):
			print(ec+'Por el momento no se han cargado locales.'+cierre)
			presione('continuar')
	salto()

def CREAR(X,Z,Y,W):
	global tl
	muestroLocales()
	opcionGestion('a)','CREAR')
	desea('a','CREAR','crear')
	while(des !='N') and (tl != 50):
		validoNombre('a','CREAR','!El nombre','3',X)
		if(X[n][0] != nombre):
			X[tl][0] = nombre
			validoUbicación('a','CREAR','!La ubicación','2',X)
			validoRubro('a','CREAR','!El rubro',X)
			validoCodigo('a','CREAR','!El código','0',Z)
			if(Z[c][0] == codigo) and (Z[c][3] == 'dueñoLocal'):
				salto()
				X[tl][3] = 'A'
				sumoLocal(Y,W,X[tl][2])
				print('\n'+cvc+'¡Los datos se cargaron correctamente!'+cierre)
				presione('continuar')
				tl = tl + 1
			else:
				salto()
				print('Ese codigo no pertenece al dueño de un local!')
				presione('continuar')
		else:
			print()
			print(ec+'¡Ese nombre ya existe!'+cierre)
			presione('continuar')
		opcionGestion('a)','CREAR')
		desea('a','CREAR','crear')
		salto()
	salto()

#----------------------------------------------------> Opciones de Administrador <---------------------------------------------------

def admOpcion():
	print(blanco+'>>> MENÚ ADMINISTRADOR <<<\n'+cierre)
	print('1. Gestión de Locales\n''2. Crear cuentas de dueños de locales\n''3. Aprobar / Denegar solicitud de descuento\n''4. Gestión de Novedades\n''5. Reporte de utilización de descuentos\n''0. Salir\n')

def admCartel():
	print(cursiva+'En construcción...'+cierre+'\n'+fan+'\n/ / / / / / / / / / / / / / / / / / / / /'+cierre+'\n'+pcyan+'\n* Presione una tecla para volver al menú administrador...'+cierre)
	msvcrt.getch()
	salto()

def localOpcion():
	print(blanco+'>>> 1. GESTIÓN DE LOCALES\n'+cierre+'\n''       a) Crear local\n''       b) Modificar local\n''       c) Eliminar local\n''       d) Mapa local\n''       e) Volver\n')

def admLocales():
	localOpcion()
	opcl = input('> Ingrese una opción: ').upper()
	while(opcl != 'E'):
		match opcl:
			case 'A':
				salto()
				CREAR(L,D,TR,R)
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
				print(cvc+'¡Verificación de Administrador exitosa!'+cierre)
				presione('continuar')
				ADMINISTRADOR()
			case 'dueñoLocal':
				print('DUEÑO LOCAL')
			case 'cliente':
				print('CLIENTE')
		print()
		salto()
	else:
		if((usuario == D[f][1]) and (contraseña != D[f][2])):
			print(efc+'\nx ¡Contraseña ingresada incorecta!'+cierre+'\n''__________________________________''\n'+esc+'\nx Contraseña:'+cierre,ec+contraseña+cierre+'\n')
		elif((usuario != D[f][1]) and (contraseña == D[f][2])):
			print(efc+'\nx ¡El usuario ingresado no está registrado!'+cierre+'\n''___________________________________________''\n'+esc+'\nx Usuario:'+cierre,ec+usuario+cierre+'\n')
		elif((usuario != D[f][1]) and (contraseña != D[f][2])):
			print(efc+'\nx ¡Los datos ingresados son incorrectos!'+cierre+'\n''________________________________________''\n'+esc+'\nx Usuario:'+cierre,ec+usuario+cierre+esc+'\nx Contraseña:'+cierre,ec+contraseña+cierre+'\n')
		intentos = intentos - 1
		print(ec+'Le quedan',intentos,'intentos.'+cierre+'\n')
		presione('reintentar')
		salto()
	if(intentos != 0):
		tituloIniciar()
		decision = input('¿Desea continuar en el programa? S / N \n\n> ').upper()
		salto()
		while (decision != 'N') and (decision != 'S'):
			caracterInvalido()
			tituloIniciar()
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
	global intentos, decision, tl
	tl = 0
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
        clocal: array[1..50] of integer;
        trubros: array[0..2] of integer;
        rubros: array[0..2] of string;
	var D: datos;
		L: locales;
		m: mapa;
		TR: trubros;
		R: rubros;
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
	L = ['']*51
	for f in range(51):
		L[f] = ['']*4

def cargoTotalRubros():
	global TR
	TR = [0]*3

def cargoRubros():
	global R
	R = ['Comida','Indumentaria','Perfumeria']

def INICIO():
	cargoUsuarios()
	cargoLocales()
	cargoTotalRubros()
	cargoRubros()

#------------------------------------------------------------> Ejecución <-----------------------------------------------------------

INICIO()
PROGRAMA()
