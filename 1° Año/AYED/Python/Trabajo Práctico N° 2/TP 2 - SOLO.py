#------------------------------------------------------------> UTILIDAD <------------------------------------------------------------

import msvcrt
clearconsole = lambda: print('\n' * 100)

#------------------------------------------------------------> COLORES <--------------------------------------------------------------

negro = '\033[30m'
rojo = '\033[3;31m'
verde = '\033[32m'
amarillo = '\033[4;33m'
azul = '\033[4;34m'
purpura = '\033[35m'
cyan = '\033[36m'
blanco = '\033[4;37m'
reset = '\033[39m'
cierre = '\033[0;m'

#-------------------------------------------------------> PROGRAMA PRINCIPAL <-------------------------------------------------------

def program():
	users = 'admin@shopping.com'
	password = '12345'
	attempts = 3
	clearconsole()
	print(blanco+'>>> B I E N V E N I D O  <<<'+cierre)
	print()
	decision = input('¿Desea iniciar sesion? S / N \n\n> ').upper()
	print()
	while (decision != 'N') and (decision != 'S'):
		clearconsole()
		print(blanco+'>>> B I E N V E N I D O  <<<'+cierre)
		print()
		print(rojo+'x ¡Carácter ingresado inválido, ingrese S o N!'+cierre)
		print()
		decision = input('¿Desea iniciar sesion? S / N \n\n> ').upper()
	clearconsole()
	while(decision != 'N' and attempts != 0):
		print(blanco+'>>> INICIAR SESIÓN <<<'+cierre)
		print()
		userLogin = str(input('> Ingrese usuario: '))
		while((len(userLogin) > 100) or (len(userLogin) < 7)):
			clearconsole()
			print(blanco+'>>> INICIAR SESIÓN <<<'+cierre)
			print()
			print(rojo+'x ¡Usuario ingresado inválido. Mínimo 7 caracteres!'+cierre)
			print()
			userLogin = str(input('> Ingrese usuario: '))
		clearconsole()
		print(blanco+'>>> INICIAR SESIÓN <<<'+cierre)
		print()
		userPassword = str(input('> Ingrese contraseña: '))
		while((len(userPassword) > 8) or (len(userPassword) < 3)):
			clearconsole()
			print(blanco+'>>> INICIAR SESIÓN <<<'+cierre)
			print()
			print(rojo+'x ¡Contraseña ingresada inválida. Mínimo 4 dígitos!'+cierre)
			print()
			userPassword = str(input('> Ingrese contraseña: '))
		clearconsole()
		if(userLogin == users and userPassword == password):
			print()
			print('Los datos son correctos!')
			print()
			print("* Presione una tecla para continuar...")
			msvcrt.getch()
			clearconsole()
		else:
			if((userLogin == users) and (userPassword != password)):
				print()
				print(rojo+'x ¡Contraseña ingresada incorecta!'+cierre)
				print('- - - - - - - - - - - - - - - - - - - - - ')
				print()
				print(azul+'# Contraseña:'+cierre,userPassword)
				print()
			elif((userLogin != users) and (userPassword == password)):
				print()
				print(rojo+'x El usuario ingresado no está registrado!'+cierre)
				print('- - - - - - - - - - - - - - - - - - - - - ')
				print()
				print(azul+'# Usuario:'+cierre,userLogin)
				print()
			elif((userLogin != users) and (userPassword != password)):
				print()
				print(rojo+'x ¡Los datos ingresados son incorrectos!'+cierre)
				print('- - - - - - - - - - - - - - - - - - - - - ')
				print()
				print(azul+'# Usuario:'+cierre,userLogin)
				print(azul+'# Contraseña:'+cierre,userPassword)
				print()
			attempts = attempts - 1
			print('Le quedan',attempts,'intentos.')
			print()
			print("* Presione una tecla para continuar...")
			msvcrt.getch()
			clearconsole()
		if(attempts != 0):
			print(blanco+'>>> INICIAR SESIÓN <<<'+cierre)
			print()
			decision = input('¿Desea continuar en el programa? S / N \n\n> ').upper()
			print()
			clearconsole()
			while (decision != 'N') and (decision != 'S'):
				print()
				print(blanco+'>>> INICIAR SESIÓN <<<'+cierre)
				print()
				print(rojo+'x ¡Carácter ingresado inválido, ingrese S o N!'+cierre)
				print()
				decision = input('¿Desea continuar en el programa?: ').upper()
				clearconsole()
		else:
			print(rojo+'x !Ha alcanzado el límite de intentos!'+cierre)
			print()
			print("* Presione una tecla para cerrar sesion...")
			msvcrt.getch()
	clearconsole()
	print('¡Gracias por su visita!')
	msvcrt.getch()

#------------------------------------------------------------> EJECUCIÓN <-----------------------------------------------------------
program()