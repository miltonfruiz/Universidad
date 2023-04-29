#Importamos librerias
from getpass import getpass

#Definimos constantes y variables
def inicio():
    global attempts, in_menu, admin_user, admin_password
    attempts = 0
    in_menu = '5'
    admin_user = "admin@shopping.com"
    admin_password = "12345"

#Contadores para los rubros
conIndumentaria = 0
conComida = 0
conPerfumeria = 0

#=====================================================================================#
#                                FUNCIONES PARA EL LOGIN                              #
#=====================================================================================#

#Entrada de datos
def loginInput():
    global nombreUsuario, claveUsuario
    nombreUsuario = input("Ingrese su nombre de usuario: ")
    while((len(nombreUsuario) > 100) or (len(nombreUsuario) < 7)):
            print("==============================")
            print("Nombre de usuario no válido. Debe contener entre 8 y 100 caracteres")
            nombreUsuario = input("Ingrese un nombre de usuario: ")
    claveUsuario = getpass("Ingrese su contraseña: ")
    while((len(claveUsuario) > 8) or (len(claveUsuario) < 3)):
            print("==============================")
            print("Contraseña no válida. Debe contener entre 3 y 8 caracteres")
            claveUsuario = getpass("Ingrese su contraseña: ")

#Validación de datos
def loginVal():
    global attempts, in_menu

    if nombreUsuario == admin_user and claveUsuario == admin_password:
        print("==============================")
        print("Bienvenido Administrador!")
        attempts = attempts + 3

    else:
        attempts = attempts + 1
        if attempts != 3:
            print("Credenciales incorrectas. Has realizado", attempts, "de 3 intentos")

        else:
            print("Credenciales incorrectas. No tienes más intentos")
            in_menu = 0

#=====================================================================================#
#                                      MENU's                                         #
#=====================================================================================#

#Print del menú principal
def menuPrincipal():
    global accion, in_locales, in_novedad
    in_locales = 'e'
    in_novedad = 'f'
    print("==============================")
    print("1. Gestión de locales")
    print("2. Crear cuentas de dueños locales")
    print("3. Aprobar/Denegar solicitud de descuento")
    print("4. Gestión de novedades")
    print("0. Salir")
    accion = input("Seleccione una acción: ")
    menuPrincVal()

#Menu Gestión de Locales
def menuLocales():
    global in_locales
    while (in_locales != 'd'):
        is_creating = 'c'
        menuLocPrint()

        match localAcc:
            case "a":

                while (is_creating != 'b'):
                    ingresoLocal()
                    contarLocal()
                    otroLocal()

                    match opcLocal:
                        case "a":
                            is_creating = "a"
                        case "b":
                            mayorRubro()
                            menorRubro()
                            is_creating = 'b'

            case "b":
                soon()

            case "c":
                soon()

            case "d":
                in_locales = 'd'

#Menú Gestión de Novedades
def menuNovedades():
    global in_novedad
    while (in_novedad != 'e'):
        menuNovPrint()

        match novedadAcc:
            case "a":
                soon()

            case "b":
                soon()

            case "c":
                soon()

            case "d":
                soon()

            case "e":
                in_novedad = 'e'


#Print del menú Gestión de locales
def menuLocPrint():
    global localAcc
    print("==============================")
    print("a) Crear locales")
    print("b) Modificar local")
    print("c) Eliminar local")
    print("d) Volver")
    localAcc = input("Seleccione una acción: ")
    menuLocVal()

#Print del menú gestión de novedades
def menuNovPrint():
    global novedadAcc
    print("==============================")
    print("a) Crear novedades")
    print("b) Modificar novedad")
    print("c) Eliminar novedad")
    print("d) Ver reporte de novedades")
    print("e) Volver")
    novedadAcc = input("Seleccione una opción: ")
    menuNovVal()

#Print ¿seguir creando más locales?
def otroLocal():
    global opcLocal
    print("==============================")
    print("¿Qué desea hacer a continuación?")
    print("a) Crear otro local")
    print("b) Salir")
    opcLocal = input("Seleccione una opción: ")
    otroLocalVal()


#=====================================================================================#
#                             FUNCIONES PARA EL MENU                                  #
#=====================================================================================#

#Ingreso de un nuevo local
def ingresoLocal():
    global rubroLocal
    print("==============================")
    nombreLocal = input("Ingrese el nombre del local: ")

    while((len(nombreLocal) > 100) or (len(nombreLocal) < 1)):
        print("==============================")
        print("Nombre de local no válido. Debe contener entre 1 y 100 caracteres")
        nombreLocal = input("Ingrese el nombre del local: ")
    ubicacionLocal = input("Ingrese la ubicación del local: ")

    while((len(ubicacionLocal) > 50) or (len(ubicacionLocal) < 1)):
        print("==============================")
        print("Ubicación de local no válida. Debe contener entre 1 y 50 caracteres")
        ubicacionLocal = input("Ingrese la ubicación del local: ")
    rubroLocal = input("Ingrese el rubro del local: ")
    
    rubroVal()

#Sumar a los contadores de los rubros
def contarLocal():
    global conIndumentaria, conComida, conPerfumeria

    match rubroLocal:
        case "indumentaria":
            conIndumentaria = conIndumentaria + 1
        
        case "perfumeria":
            conPerfumeria = conPerfumeria + 1

        case "comida":
            conComida = conComida + 1

#Determinar el mayor rubro
def mayorRubro():
    print("==============================")
    if conPerfumeria == conIndumentaria and conComida == conIndumentaria:
        print("Todos los rubros tienen la misma cantidad de locales, que son", conIndumentaria)

    else: 
        if conIndumentaria > conComida and conIndumentaria > conPerfumeria:
            print("El rubro con más locales es indumentaria con", conIndumentaria, "local/es.")

        elif conComida > conIndumentaria and conComida > conPerfumeria:
            print("El rubro con más locales es comida con", conComida, "local/es.")
    
        elif (conIndumentaria == conComida) and (conIndumentaria == conComida) > conPerfumeria:
           print("Los rubros con más locales son indumentaria y comida, con", conIndumentaria, "local/es")
    
        elif (conIndumentaria == conPerfumeria) and (conIndumentaria == conPerfumeria) > conComida:
            print("Los rubros con más locales son indumentaria y perfumeria, con", conIndumentaria, "local/es")

        elif (conComida == conPerfumeria) and (conComida == conPerfumeria) > conIndumentaria:
            print("Los rubros con más locales son comida y perfumeria, con", conComida, "local/es")

        else:
            print("El rubro con más locales es perfumeria con", conPerfumeria, "local/es.")

#Determinar el menor rubro
def menorRubro():
    if conPerfumeria != conIndumentaria or conComida != conIndumentaria:
        if (conIndumentaria == conPerfumeria) and (conIndumentaria < conComida):
            print("Los rubros con menos locales son indumentaria y perfumeria, con", conIndumentaria, "local/es")

        elif (conIndumentaria == conComida) and (conIndumentaria < conPerfumeria):
            print("Los rubros con menos locales son indumentaria y comida, con", conIndumentaria, "local/es")

        elif (conComida == conPerfumeria) and (conComida < conIndumentaria):
            print("Los rubros con menos locales son perfumeria y comida, con", conComida, "local/es")

        elif conIndumentaria < conComida and conIndumentaria < conPerfumeria:
            print("El rubro con menos locales es indumentaria con", conIndumentaria, "local/es.")

        elif conComida < conIndumentaria and conComida < conPerfumeria:
            print("El rubro con menos locales es comida con", conComida, "local/es.")

        elif conPerfumeria < conIndumentaria and conPerfumeria < conComida:
            print("El rubro con menos locales es perfumeria con", conPerfumeria, "local/es.")



#=====================================================================================#
#                                   VALIDADORES                                       #
#=====================================================================================#

#Otherwise del Menu Principal
def menuPrincVal():
    global accion
    while accion != "1" and accion != "2" and accion != "3" and accion != "4" and accion != "0":
        print("==============================")
        print("La acción", accion, "no se encuentra registrada en el sistema. Pruebe otra vez")
        menuPrincipal()

#Otherwise del Menu Gestión Locales
def menuLocVal():
    global localAcc
    while localAcc != "a" and localAcc != "b" and localAcc != "c" and localAcc != "d":
        print("==============================")
        print("La acción", localAcc, "no se encuentra registrada en el sistema. Pruebe otra vez")
        menuLocPrint()

#Otherwise del Menu Gestión de Novedades
def menuNovVal():
    global novedadAcc
    while novedadAcc != "a" and novedadAcc != "b" and novedadAcc != "c" and novedadAcc != "d" and novedadAcc != "e":
        print("==============================")
        print("La acción", novedadAcc, "no se encuentra registrada en el sistema. Pruebe otra vez")
        menuNovPrint()

#Otherwise de la creación de locales
def rubroVal():
    global rubroLocal
    while rubroLocal != "perfumeria" and rubroLocal != "indumentaria" and rubroLocal != "comida":
        print("==============================")
        print("El rubro", rubroLocal,  "no se encuentra registrado en el sistema. Pruebe otra vez")
        rubroLocal = input("Ingrese el rubro del local: ")
        

#Validador para "otroLocal", si seguir creando o no
def otroLocalVal():
    global opcLocal
    while opcLocal != "a" and opcLocal != "b":
        print("==============================")
        print("La acción", opcLocal, "no se encuentra registrada en el sistema. Pruebe otra vez")
        otroLocal()

#=====================================================================================#
#                                 OTRAS FUNCIONES                                     #
#=====================================================================================#

#En construcción
def soon():
    print("==============================")
    print("En construcción...")

def despedida():
    global in_menu
    print("==============================")
    print("==  Se cerrará el programa  ==")
    print("==============================")
    in_menu = 0
    
#=====================================================================================#
#                                PROGRAMA PRINCIPAL                                   #
#=====================================================================================#

inicio()
while attempts < 3:
    loginInput()
    loginVal()

while (in_menu != 0):
    
    menuPrincipal()

    match accion:
        case "1":
            menuLocales()

        case "2":
            soon()

        case "3":
            soon()

        case "4":
            menuNovedades()

        case "0":
            despedida()