#------------------------------------------------------------> UTILIDAD <------------------------------------------------------------

import msvcrt
clearconsole = lambda: print('\n' * 150)

#-------------------------------------------------------> PROGRAMA PRINCIPAL <-------------------------------------------------------

def program():
	users = 'admin@shopping.com'
	password = '12345'
	attempts = 3
	clearconsole()
	print('>>> B I E N V E N I D O  <<<')
	print()
	decision = input('¿Desea iniciar sesion? S / N: ').upper()
	print()
	while (decision != 'N') and (decision != 'S'):
		clearconsole()
		print('>>> B I E N V E N I D O  <<<')
		print()
		print('# Carácter inválido, ingrese S o N')
		print()
		decision = input('¿Desea iniciar sesion?: ').upper()
	clearconsole()
	while(decision != 'N' and attempts != 0):
		print('>>> INICIAR SESIÓN <<<')
		print()
		userLogin = str(input('> Ingrese usuario: '))
		while((len(userLogin) >= 100) or (len(userLogin) <= 7)):
			clearconsole()
			print('>>> INICIAR SESIÓN <<<')
			print()
			print('# Usuario ingresado inválido. Mínimo 7 caracteres')
			print()
			userLogin = str(input('> Ingrese usuario: '))
		clearconsole()
		print('>>> INICIAR SESIÓN <<<')
		print()
		userPassword = str(input('> Ingrese contraseña: '))
		while((len(userPassword) >= 8) or (len(userPassword) <= 3)):
			clearconsole()
			print('>>> INICIAR SESIÓN <<<')
			print()
			print('# Contraseña ingresada inválida. Mínimo 4 dígitos')
			print()
			userPassword = str(input('> Ingrese contraseña: '))
		clearconsole()
		if(userLogin == users and userPassword == password):
			print()
			print('Los datos son correctos!')
			print()
			print("Presione una tecla para continuar...")
			msvcrt.getch()
			clearconsole()
		else:
			if((userLogin == users) and (userPassword != password)):
				print()
				print('¡Contraseña ingresada incorecta!')
				print()
				print('# Contraseña: ',userPassword)
				print()
			elif((userLogin != users) and (userPassword == password)):
				print()
				print('El usuario ingresado no está registrado!')
				print()
				print('# Usuario: ',userLogin)
				print()
			elif((userLogin != users) and (userPassword != password)):
				print()
				print('¡Los datos ingresados son incorrectos!')
				print()
				print('# Usuario: ',userLogin)
				print('# Contraseña: ',userPassword)
				print()
			attempts = attempts - 1
			print('Le quedan',attempts,'intentos.')
			print()
			print("Presione una tecla para continuar...")
			msvcrt.getch()
			clearconsole()
		if(attempts != 0):
			print('>>> INICIAR SESIÓN <<<')
			print()
			decision = input('¿Desea continuar en el programa? S / N: ').upper()
			print()
			clearconsole()
			while (decision != 'N') and (decision != 'S'):
				print()
				print('>>> INICIAR SESIÓN <<<')
				print()
				print('# Carácter inválido, ingrese S o N')
				print()
				decision = input('¿Desea continuar en el programa?: ').upper()
				clearconsole()
		else:
			print('!Ha alcanzado el límite de intentos!')
			print()
			print("Presione una tecla para cerrar sesion...")
			msvcrt.getch()
	clearconsole()
	print('Gracias por su visita!!!')
	msvcrt.getch()

#------------------------------------------------------------> EJECUCIÓN <-----------------------------------------------------------
program()