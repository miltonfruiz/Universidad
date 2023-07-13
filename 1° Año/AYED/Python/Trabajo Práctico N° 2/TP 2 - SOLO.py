#------------------------------------------------------------> Utilidad <-------------------------------------------------------------

import msvcrt
salto = lambda: print('\n' * 150)

#------------------------------------------------------------> Colores <--------------------------------------------------------------

negro = '\033[30m'
efc = '\033[3;37;41m'
esc = '\033[3;4;31m'
ec = '\033[3;31m'
verde = '\033[32m'
amarillo = '\033[4;33m'
azul = '\033[3;4;34m'
purpura = '\033[35m'
pcyan = '\033[1;36m'
blanco = '\033[4;37m'
reset = '\033[39m'
cierre = '\033[0;m'

#-------------------------------------------------------> Programa Principal <-------------------------------------------------------

def PROGRAMA():
	users = 'admin@shopping.com'
	password = '12345'
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
		print(blanco+'>>> INICIAR SESIÓN <<<'+cierre)
		print()
		userLogin = str(input('> Ingrese usuario: '))
		while((len(userLogin) > 100) or (len(userLogin) < 7)):
			salto()
			print(blanco+'>>> INICIAR SESIÓN <<<'+cierre)
			print()
			print(efc+'x ¡Usuario ingresado inválido. Mínimo 7 caracteres!'+cierre)
			print()
			userLogin = str(input('> Ingrese usuario: '))
		salto()
		print(blanco+'>>> INICIAR SESIÓN <<<'+cierre)
		print()
		userPassword = str(input('> Ingrese contraseña: '))
		while((len(userPassword) > 8) or (len(userPassword) < 3)):
			salto()
			print(blanco+'>>> INICIAR SESIÓN <<<'+cierre)
			print()
			print(efc+'x ¡Contraseña ingresada inválida. Mínimo 4 dígitos!'+cierre)
			print()
			userPassword = str(input('> Ingrese contraseña: '))
		salto()
		if(userLogin == users and userPassword == password):
			print()
			print('Los datos son correctos!')
			print()
			print(pcyan+'* Presione una tecla para continuar...'+cierre)
			msvcrt.getch()
			salto()
		else:
			if((userLogin == users) and (userPassword != password)):
				print()
				print(efc+'x ¡Contraseña ingresada incorecta!'+cierre)
				print('__________________________________')
				print()
				print(esc+'x Contraseña:'+cierre,ec+userPassword+cierre)
				print()
			elif((userLogin != users) and (userPassword == password)):
				print()
				print(efc+'x ¡El usuario ingresado no está registrado!'+cierre)
				print('___________________________________________')
				print()
				print(esc+'x Usuario:'+cierre,ec+userLogin+cierre)
				print()
			elif((userLogin != users) and (userPassword != password)):
				print()
				print(efc+'x ¡Los datos ingresados son incorrectos!'+cierre)
				print('________________________________________')
				print()
				print(esc+'x Usuario:'+cierre,ec+userLogin+cierre)
				print(esc+'x Contraseña:'+cierre,ec+userPassword+cierre)
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
	salto()
	print('¡Gracias por su visita!')
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
		['2','','',''],
		['3','','',''],
		['4','localA@shopping.com','AAAA1111','dueñoLocal'],
		['5','','',''],
		['6','localB@shopping.com','BBBB2222','dueñoLocal'],
		['7','','',''],
		['8','','',''],
		['9','unCliente@shopping.com','33xx33','cliente'],
		['10','','',''],
	  ]
	D = ['']*10
	for i in range(10):
		D[i] = datos[i]

def INICIO():
	cargoUsuarios()

#------------------------------------------------------------> Ejecución <-----------------------------------------------------------

INICIO()
PROGRAMA()