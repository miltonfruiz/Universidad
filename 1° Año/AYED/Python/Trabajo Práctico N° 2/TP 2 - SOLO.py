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

def buscoIndice(codigo):
	f = 0
	while((f != codigo) and (f != 50)):
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

def reset(X,f):
	X[f][0] = ''
	X[f][1] = ''
	X[f][2] = ''
	X[f][3] = ''

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

def ordenoLocales(X):
	for i in range(0,49):
		for j in range(i+1,50):
			if(X[i][0] > X[j][0]):
				for k in range(4):
					aux = X[i][k]
					X[i][k] = X[j][k]
					X[j][k] = aux

#-------------------------------------------------> Opciones de Gestión de Locales <-------------------------------------------------

def validoNombre(letra,opcion,cadena,minimo,X):
	global nombre, n
	salto()
	opcionGestion(letra,opcion)
	nombre = input('> Ingrese nombre: ').capitalize()
	while((len(nombre) > 50) or (len(nombre) < 2)):
		salto()
		print(ec+'x ',cadena,'debe contener mínimo',minimo,'caracteres!'+cierre)
		presione('reintentar')
		opcionGestion(letra,opcion)
		nombre = input('> Ingrese nombre nuevamente: ').capitalize()
	n = buscoNombre(X,nombre)

def validoUbicación(letra,opcion,cadena,minimo,X,fila):
	salto()
	opcionGestion(letra,opcion)
	X[fila][1] = input('> Ingrese ubicación: ')
	while((len(X[fila][1]) > 50) or (len(X[fila][1]) < 1)):
		salto()
		print(ec+'x ',cadena,'debe contener mínimo',minimo,'caracteres!'+cierre)
		presione('reintentar')
		opcionGestion(letra,opcion)
		X[fila][1] = input('> Ingrese ubicación nuevamente: ')

def validoRubro(letra,opcion,cadena,X,fila):
	salto()
	opcionGestion(letra,opcion)
	X[fila][2] = input('> Ingrese rubro: ').capitalize()
	while(X[fila][2] != 'Comida') and (X[fila][2] != 'Indumentaria') and (X[fila][2] != 'Perfumeria'):
		salto()
		print(ec+'x ',cadena,'ingresado debe ser comida, indumentria o perfumeria!'+cierre)
		presione('reintentar')
		opcionGestion(letra,opcion)
		X[fila][2] = input('> Ingrese rubro nuevamente: ').capitalize()

def validoCodigo(letra,opcion,cadena,minimo,X):
	global codigo, c
	salto()
	opcionGestion(letra,opcion)
	codigo = input('> Ingrese codigo: ')
	while(codigo == '-1'):
		salto()
		print(ec+'x ',cadena,'ingresado debe ser distinto de',minimo,+cierre)
		presione('reintentar')
		opcionGestion(letra,opcion)
		codigo = input('> Ingrese codigo nuevamente: ')
	c = buscoCodigo(X,codigo)

def validoIndice(letra,opcion,cadena,minimo):
	global codigoIndice, im
	salto()
	opcionGestion(letra,opcion)
	codigoIndice = int(input('> Ingrese codigo: '))
	while(codigoIndice < -1):
		salto()
		print(ec+'x ',cadena,'ingresado debe ser',minimo,+cierre)
		presione('reintentar')
		opcionGestion(letra,opcion)
		codigoIndice = int(input('> Ingrese codigo nuevamente: '))
	im = buscoIndice(codigoIndice)

def muestroDescendente(Y,W,letra,opcion):
	opcionGestion(letra,opcion)
	print('     TOTAL              RUBRO\n'' ------------------------------------')
	for i  in range(3):
		if(Y[i] != 0):
			print('       ',Y[i],'             ',W[i])

def sumoLocal(Y,W,tipo,letra,opcion):
	t = buscoRubro(W,tipo)
	match W[t]:
		case 'Comida':
			Y[t] = Y[t] + 1
		case 'Indumentaria':
			Y[t] = Y[t] + 1
		case 'Perfumeria':
			Y[t] = Y[t] + 1
	ordenoCantidad(Y,W)
	print(cvc+'¡Los datos se cargaron correctamente!'+cierre)
	presione('visualizar rubros cargados hastas el momento')
	muestroDescendente(Y,W,letra,opcion)

def restoLocal(Y,W,tipo):
	t = buscoRubro(W,tipo)
	match W[t]:
		case 'Comida':
			Y[t] = Y[t] - 1
		case 'Indumentaria':
			Y[t] = Y[t] - 1
		case 'Perfumeria':
			Y[t] = Y[t] - 1
	ordenoCantidad(Y,W)

def muestroLocales(X,letra,opcion):
	global decs,c
	ordenoLocales(X)
	opcionGestion(letra,opcion)
	decs = input('¿Desea ver locales cargados? S / N \n\n> ').upper()
	print()
	while (decs != 'N') and (decs != 'S'):
		caracterInvalido()
		opcionGestion(letra,opcion)
		decs = input('¿Desea ver locales cargados? S / N \n\n> ').upper()
	salto()
	if(decs == 'S') and (X[49][0] != ''):
		opcionGestion(letra,opcion)
		print('CODIGO       NOMBRE       UBICACIÓN       RUBRO       ESTADO')
		print('------------------------------------------------------------')
		for f in range(0,51):
			if(X[f][0] != ''):
				print(' ',f,'      ',X[f][0],'     ',X[f][1],'      ',X[f][2],'    ',X[f][3])
		presione('continuar')
	elif(decs == 'S') and (X[0][0] == ''):
			print(ec+'Por el momento no se han cargado locales.'+cierre)
			presione('continuar')
	salto()

def CREAR(X,Z,Y,W,tl):
	muestroLocales(X,'a)','CREAR')
	opcionGestion('a)','CREAR')
	desea('a','CREAR','crear')
	while(des !='N') and (tl != 50):
		validoNombre('a)','CREAR','!El nombre','3',X)
		while(X[n][0] == nombre):
			salto()
			print(ec+'¡Ese nombre ya existe!'+cierre)
			presione('reintentar')
			validoNombre('a)','CREAR','!El nombre','3',X)
		X[tl][0] = nombre
		validoUbicación('a)','CREAR','!La ubicación','2',X,tl)
		validoRubro('a)','CREAR','!El rubro',X,tl)
		validoCodigo('a)','CREAR','!El código','negativo',Z)
		while(Z[c][0] != codigo) and (Z[c][3] != 'dueñoLocal'):
			salto()
			print(ec+'Ese codigo no pertenece al dueño de un local!'+cierre)
			presione('reintentar')
			validoCodigo('a)','CREAR','!El código','0',Z)
		salto()
		X[tl][3] = 'A'
		sumoLocal(Y,W,X[tl][2],'a)','CREAR')
		presione('continuar')
		tl = tl + 1
		opcionGestion('a)','CREAR')
		desea('a','CREAR','crear')
		salto()
	salto()
	presione('volver al menú anterior')
	salto()

def MODIFICAR(X,Y,W):
	global im
	muestroLocales(X,'b)','MODIFICAR')
	if(X[49][0] != ''):
		opcionGestion('b)','MODIFICAR')
		desea('b','MODIFICAR','modificar algún')
		while(decs != 'N' and X[49][0] != '' and des != 'N'):
			validoIndice('b)','MODIFICAR','!El código','entre 0-49')
			while(im != codigoIndice):
				salto()
				print(ec+'Ese codigo no pertenece a un local!'+cierre)
				presione('reintentar')
				validoIndice('b)','MODIFICAR','!El código','entre 0-49')
			salto()
			opcionGestion('b)','MODIFICAR')
			desea('b','MODIFICAR','realmente modificar este')
			if(des == 'S'):
				validoNombre('b)','MODIFICAR','!El nombre','3',X)
				while(X[n][0] == nombre):
					salto()
					print(ec+'¡Ese nombre ya existe!'+cierre)
					presione('reintentar')
					validoNombre('b)','MODIFICAR','!El nombre','3',X)
				X[im][0] = nombre
				validoUbicación('b)','MODIFICAR','!La ubicación','2',X,im)
				restoLocal(Y,W,X[im][2])
				validoRubro('b)','MODIFICAR','!El rubro',X,im)
				salto()
				X[im][3] = 'A'
				sumoLocal(Y,W,X[im][2],'b)','MODIFICAR')
				presione('continuar')
			opcionGestion('b)','MODIFICAR')
			desea('b','MODIFICAR','modificar algún')
	salto()
	presione('volver al menú anterior')
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
				CREAR(L,D,TR,R,tl)
			case 'B':
				salto()
				MODIFICAR(L,TR,R)
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
		match D[f][3]:
			case 'administrador':
				print(cvc+'¡Verificación de Administrador exitosa!'+cierre)
				presione('acceder al menú')
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
		print(efc+'x !Ha alcanzado el límite de intentos!'+cierre+'\n''______________________________________''\n')
		presione('cerrar sesión')
		msvcrt.getch()

#-------------------------------------------------------> Programa Principal <-------------------------------------------------------

def PROGRAMA():
	global intentos, decision, tl
	tl = 0
	intentos = 3
	tituloBienvenida()
	decision = input('¿Desea iniciar sesion? S / N \n\n> ').upper()
	while (decision != 'N') and (decision != 'S'):
		caracterInvalido()
		tituloBienvenida()
		decision = input('¿Desea iniciar sesion? S / N \n\n> ').upper()
	salto()
	while(decision != 'N' and intentos != 0):
		ACCESO()
	salto()
	print('¡Gracias por su visita!')
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
