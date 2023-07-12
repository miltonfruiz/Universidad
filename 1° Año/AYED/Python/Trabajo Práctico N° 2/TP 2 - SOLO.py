#------------------------------------------------------------> UTILIDAD <------------------------------------------------------------

import msvcrt
clearconsole = lambda: print('\n' * 150)

#------------------------------------------------------------> COLORES <--------------------------------------------------------------

negro = '\033[30m'
efc = '\033[1;37;41m'
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

#-------------------------------------------------------> PROGRAMA PRINCIPAL <-------------------------------------------------------

def program():
	users = 'admin@shopping.com'
	password = '12345'
	intentos = 3
	clearconsole()
	print(blanco+'>>> B I E N V E N I D O  <<<'+cierre)
	print()
	decision = input('¿Desea iniciar sesion? S / N \n\n> ').upper()
	print()
	while (decision != 'N') and (decision != 'S'):
		clearconsole()
		print(blanco+'>>> B I E N V E N I D O  <<<'+cierre)
		print()
		print(efc+'x ¡Carácter ingresado inválido, ingrese S o N!'+cierre)
		print()
		decision = input('¿Desea iniciar sesion? S / N \n\n> ').upper()
	clearconsole()
	while(decision != 'N' and intentos != 0):
		print(blanco+'>>> INICIAR SESIÓN <<<'+cierre)
		print()
		userLogin = str(input('> Ingrese usuario: '))
		while((len(userLogin) > 100) or (len(userLogin) < 7)):
			clearconsole()
			print(blanco+'>>> INICIAR SESIÓN <<<'+cierre)
			print()
			print(efc+'x ¡Usuario ingresado inválido. Mínimo 7 caracteres!'+cierre)
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
			print(efc+'x ¡Contraseña ingresada inválida. Mínimo 4 dígitos!'+cierre)
			print()
			userPassword = str(input('> Ingrese contraseña: '))
		clearconsole()
		if(userLogin == users and userPassword == password):
			print()
			print('Los datos son correctos!')
			print()
			print(pcyan+'* Presione una tecla para continuar...'+cierre)
			msvcrt.getch()
			clearconsole()
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
			clearconsole()
		if(intentos != 0):
			print(blanco+'>>> INICIAR SESIÓN <<<'+cierre)
			print()
			decision = input('¿Desea continuar en el programa? S / N \n\n> ').upper()
			print()
			clearconsole()
			while (decision != 'N') and (decision != 'S'):
				print()
				print(blanco+'>>> INICIAR SESIÓN <<<'+cierre)
				print()
				print(efc+'x ¡Carácter ingresado inválido, ingrese S o N!'+cierre)
				print()
				decision = input('¿Desea continuar en el programa?: ').upper()
				clearconsole()
		else:
			print(efc+'x !Ha alcanzado el límite de intentos!'+cierre)
			print('______________________________________')
			print()
			print(pcyan+'* Presione una tecla para cerrar sesion... '+cierre)
			msvcrt.getch()
	clearconsole()
	print('¡Gracias por su visita!')
	msvcrt.getch()

#------------------------------------------------------------> EJECUCIÓN <-----------------------------------------------------------
program()