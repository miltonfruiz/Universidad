#----------------------------------------------------------------------------------------------------------------------
from operator import rshift
import os
from datetime import date, datetime
import pickle
import os.path
from turtle import pos
def pausa():
    os.system("pause")
clearconsole= lambda: os.system('cls')

black= '\033[30m'
red= '\033[31m'
green= '\033[32m'
yellow= '\033[33m'
blue= '\033[34m'
purple= '\033[35m'
Cyan= '\033[36m'
white= '\033[37m'
reset = '\033[39m'

fechahoy=datetime.now().strftime("%d/%m/%y")
#global afoperaciones, aloperaciones, afproductos, alproductos, afrubros, alrubros, afrubrosp, alrubrosp, afsilos, alsilos, alrechazados, afrechazados

#-----------------------------------------------> CLASES <--------------------------------------------------------

class operaciones():
    def __init__(self):
        self.patente = ""
        self.codproducto = 0
        self.fechacupo = ""
        self.estado = ""
        self.bruto = 0
        self.tara = 0

class productos():
    def __init__(self):
        self.codprod = 0
        self.nombreprod = ""
        self.estado = ""

class rubros():
    def __init__(self):
        self.codrubros = 0
        self.nombrerubro = ""

class rubrosXproductos():
    def __init__(self):
        self.codrubros = 0
        self.codprod = 0
        self.minimo = 0 #no menor a 0 (real)
        self.maximo = 0 #no puede ser mayor a 100 (real)

class silos():
    def __init__(self):
        self.codsilos = 0
        self.nombre = ""
        self.codprod = 0
        self.stock = 0

class rechazados():
    def __init__(self):
        self.fecha = ""
        self.patente = ""
        self.estado = ""

class totales():
    def __init__(self):
        self.cupos = 0
        self.camionesrecib = 0

class camionesxproductos():
    def __init__(self):
        self.nombreprod = ""
        self.prodcod = 0
        self.cantprod = 0
        self.netototal = 0
        self.promedio = 0
        self.menorpat = ""
        self.menorpeso = 0

#---------------------------------------------- --> APERTURA <-------------------------------------------------------

def APERTURA():
    global afoperaciones, aloperaciones, afproductos, alproductos, afrubros, alrubros, afrubrosp, alrubrosp, afsilos, alsilos, alrechazados, afrechazados, aftotales, altotales
    afoperaciones="C:\\AyEd\\OPERACIONES.dat"
    if os.path.exists(afoperaciones):
        aloperaciones=open(afoperaciones,"r+b")
    else:
        aloperaciones=open(afoperaciones,"w+b")

    afproductos="C:\\AyEd\\PRODUCTOS.dat"
    if os.path.exists(afproductos):
        alproductos=open(afproductos,"r+b")
    else:
        alproductos=open(afproductos,"w+b")

    afrubros="C:\\AyEd\\RUBROS.dat"
    if os.path.exists(afrubros):
        alrubros=open(afrubros,"r+b")
    else:
        alrubros=open(afrubros,"w+b")

    afrubrosp="C:\\AyEd\\RUBROSXPRODUCTO.dat"
    if os.path.exists(afrubrosp):
        alrubrosp=open(afrubrosp,"r+b")
    else:
        alrubrosp=open(afrubrosp,"w+b")

    afsilos="C:\\AyEd\\SILOS.dat"
    if os.path.exists(afsilos):
        alsilos=open(afsilos,"r+b")
    else:
        alsilos=open(afsilos,"w+b")

    afrechazados="C:\\AyEd\\RECHAZADOS.dat"
    if os.path.exists(afrechazados):
        alrechazados=open(afrechazados,"r+b")
    else:
        alrechazados=open(afrechazados,"w+b")

    aftotales="C:\\AyEd\\RECHAZADOS.dat"
    if os.path.exists(aftotales):
        altotales=open(aftotales,"r+b")
    else:
        altotales=open(aftotales,"w+b")

#-------------------------------------------> PROGRAMA PRINCIPAL <---------------------------------------------------

def PROGRAMA():
    APERTURA()
    global salir,cont
    salir=0
    cont=0
    clearconsole()
    print(">>> BIENVENIDO AL PROGRAMA PRINCIPAL <<<")
    print()
    print("1 - ADMINISTRACIONES")
    print("2 - ENTREGAS DE CUPOS")
    print("3 - RECEPCION")
    print("4 - REGISTRAR CALIDAD")
    print("5 - REGISTRAR PESO BRUTO")
    print("6 - REGISTRAR DESCARGA")
    print("7 - REGISTRAR TARA")
    print("8 - REPORTES")
    print("9 - LISTADO DE SILOS Y RECHAZOS")
    print("0 - FIN DEL PROGRAMA")
    print()
    op3=input("INGRESE UNA OPCIÓN: ").upper()
    clearconsole()
    while (op3 != "0"):
        if (op3 == "1"):
            clearconsole()
            ADMINISTRACIONES()
        elif (op3 == "2"):
            clearconsole()
            ENTREGADECUPOS()
        elif(op3 == "3"):
            clearconsole()
            RECEPCION()
        elif(op3 == "4"):
            clearconsole()
            CALIDAD()
        elif(op3 == "5"):
            clearconsole()
            PESO()
        elif(op3 == "6"):
            clearconsole()
            print()
            print('>>> BIENVENIDO A REGISTRAR DESCARGA <<<')
            print()
            print('>>> ESTA FUNCIONALIDAD ESTÁ EN CONSTRUCCIÓN')
            print()
            pulse = input('* Pulse ENTER para volver a opciones de rubros...')
            clearconsole()
        elif(op3 == "7"):
            clearconsole()
            TARA()
        elif(op3 == "8"):
            clearconsole()
            REPORTES()
        elif(op3 == "9"):
            clearconsole()
            LISTADO()
        else:
            clearconsole()
            print('x ¡OPCIÓN INVÁLIDA! x')
            print()
            pulse = input('* Pulse ENTER para reintentar...')
            clearconsole()
        print(">>> BIENVENIDO AL PROGRAMA PRINCIPAL <<<")
        print()
        print("1 - ADMINISTRACIONES")
        print("2 - ENTREGAS DE CUPOS")
        print("3 - RECEPCIÓN")
        print("4 - REGISTRAR CALIDAD")
        print("5 - REGISTRAR PESO BRUTO")
        print("6 - REGISTRAR DESCARGA")
        print("7 - REGISTRAR TARA")
        print("8 - REPORTES")
        print("9 - LISTADO DE SILOS Y RECHAZOS")
        print("0 - FIN DEL PROGRAMA")
        print()
        op3=input("INGRESE UNA OPCIÓN: ")
        clearconsole()
    print()
    print("¡Gracias por su visita, hasta pronto!")
    print()
    clearconsole()

#-----------------------------------------------> FORMATEAR <--------------------------------------------------------

def formatearProducto(rlproductos):
    rlproductos.nombreprod= rlproductos.nombreprod.ljust(10, ' ')
    rlproductos.codprod = str(rlproductos.codprod)
    rlproductos.codprod = rlproductos.codprod.ljust(5,' ')

def formatearRubro(rlrubros):
    rlrubros.nombrerubro = str(rlrubros.nombrerubro)
    rlrubros.nombrerubro = rlrubros.nombrerubro.ljust(5,' ')
    rlrubros.codrubros = str(rlrubros.codrubros)
    rlrubros.codrubros = rlrubros.codrubros.ljust(5,' ')

def FormatearRXP(rlrxp):
    rlrxp.codrubros = str(rlrxp.codrubros)
    rlrxp.codrubros = rlrxp.codrubros.ljust(5,' ')
    rlrxp.codprod = str(rlrxp.codprod)
    rlrxp.codprod = rlrxp.codprod.ljust(5,' ')
    rlrxp.minimo = str(rlrxp.minimo)
    rlrxp.minimo = rlrxp.minimo.ljust(5,' ')
    rlrxp.maximo = str(rlrxp.maximo)
    rlrxp.maximo = rlrxp.maximo.ljust(5,' ')

def FormatearOperaciones(rlop):
    rlop.patente = str(rlop.patente)
    rlop.patente = rlop.patente.ljust(7,' ')
    rlop.codproducto = str(rlop.codproducto)
    rlop.codproducto = rlop.codproducto.ljust(5,' ')
    rlop.bruto = str(rlop.bruto)
    rlop.bruto = rlop.bruto.ljust(5, ' ')
    rlop.tara = str(rlop.tara)
    rlop.tara = rlop.tara.ljust(5,' ')

def FormatearRechazados(rlrechazados):
    rlrechazados.patente = str(rlrechazados.patente)
    rlrechazados.patente = rlrechazados.patente.ljust(7,' ')

def FormatearSilos(rlsilos):
    rlsilos.codsilos = str(rlsilos.codsilos)
    rlsilos.codsilos = rlsilos.codsilos.ljust(5,' ')
    rlsilos.nombre = str(rlsilos.nombre)
    rlsilos.nombre = rlsilos.nombre.ljust(10,' ')
    rlsilos.codprod = str(rlsilos.codprod)
    rlsilos.codprod = rlsilos.codprod.ljust(5,' ')
    rlsilos.stock = str(rlsilos.stock)
    rlsilos.stock = rlsilos.stock.ljust(10,' ') #PASAR A INT PARA ACUMULAR!

def FormatearTotales(rltotales):
    rltotales.cupos = str(rltotales.cupos)
    rltotales.cupos = rltotales.cupos.ljust(5," ")
    rltotales.camionesrecib = str(rltotales.camionesrecib)
    rltotales.camionesrecib = rltotales.camionesrecib.ljust(5," ")

def FormatearCamionesxProducto(rlcxp):
    rlcxp.nombreprod = rlcxp.nombreprod.ljust(10," ")
    rlcxp.prodcod = str(rlcxp.prodcod)
    rlcxp.prodcod = rlcxp.prodcod.ljust(5," ")
    rlcxp.cantprod = str(rlcxp.cantprod)
    rlcxp.cantprod = rlcxp.cantprod.ljust(10," ")
    rlcxp.netototal= str(rlcxp.netototal).ljust(10, " ")
    rlcxp.promedio = str(rlcxp.promedio).ljust(10, " ")
    rlcxp.menorpat = (rlcxp.menorpat).ljust(10, " ")
    rlcxp.menorpeso = str(rlcxp.menorpeso).ljust(10, " ")

#----------------------------------------> ORDENAMINETO Y DICOTOMICA <----------------------------------------------------------

def ORDENAMIENTO():
    alrubros.seek (0, 0)
    aux = pickle.load(alrubros)
    tamaño = alrubros.tell() 
    tamArch = os.path.getsize(afrubros)
    cantReg = int(tamArch / tamaño)  
    for i in range(0, cantReg-1):
        for j in range (i+1, cantReg):
            alrubros.seek (i*tamaño, 0)
            auxi = pickle.load(alrubros)
            alrubros.seek (j*tamaño, 0)
            auxj = pickle.load(alrubros)
            auxi.codrubros = int(auxi.codrubros)
            auxj.codrubros = int(auxj.codrubros)
            if (auxi.codrubros > auxj.codrubros):
                alrubros.seek (i*tamaño, 0)
                formatearRubro(auxj)
                pickle.dump(auxj, alrubros)
                alrubros.seek (j*tamaño, 0)
                formatearRubro(auxi)
                pickle.dump(auxi,alrubros)
                alrubros.flush()

def DICOTOMICARUBROS(a):
    alrubros.seek (0, 0)
    aux = pickle.load(alrubros)
    tamaño = alrubros.tell() 
    cantReg = int(os.path.getsize(afrubros) / tamaño)
    desde = 0
    hasta = cantReg-1
    medio = (desde + hasta) // 2 					
    alrubros.seek(medio*tamaño, 0)
    reg= pickle.load(alrubros) 					
    while int(reg.codrubros) != a and desde < hasta:
        if a < int(reg.codrubros):			
            hasta = medio - 1
        else:
            desde = medio + 1
        medio = (desde + hasta) // 2 
        alrubros.seek(medio*tamaño, 0)
        reg= pickle.load(alrubros)
    if int(reg.codrubros) == a:
        return medio*tamaño
    else:
        return -1	
#----------------------------------------> BUSQUEDAS (Validaciones) <----------------------------------------------

def BuscoRepCodProd(codprodu):
    tam = os.path.getsize(afproductos)
    alproductos.seek(0,0)
    pos = 0
    encontrado = False
    if tam > 0:
        while alproductos.tell() < tam and not encontrado:
            pos = alproductos.tell()
            reg = pickle.load(alproductos)
            reg.codprod = int(reg.codprod)
            if reg.codprod == codprodu:
                encontrado = True
    if encontrado:
        return pos
    else:
        return -1

def BuscoEstadoCodProd(codprodu):
    rlprod = productos()
    codprodu = str(codprodu)
    codprodu = codprodu.ljust(5,' ')
    tam = os.path.getsize(afproductos)
    alproductos.seek(0,0)
    reg = productos()
    if tam > 0:
        while alproductos.tell() < tam and reg.codprod != codprodu:
            pos = alproductos.tell()
            reg = pickle.load(alproductos)
        if reg.codprod == codprodu:
            est = rlprod.estado
            return est
        else:
            return -1
    else:
        return -1

def BuscoRepNomProd(produ):
    tam = os.path.getsize(afproductos)
    alproductos.seek(0,0)
    reg = productos()
    encontrado = False
    if tam > 0:
        while alproductos.tell() < tam and not encontrado:
            pos = alproductos.tell()
            reg = pickle.load(alproductos)
            reg.nombreprod = (reg.nombreprod).strip(" ")
            if reg.nombreprod == produ:
                encontrado = True
    if encontrado:
        return pos
    else:
        return False

def BuscoRepCodRu(codru):
    tam = os.path.getsize(afrubros)
    alrubros.seek(0,0)
    reg = rubros()
    encontrado = False
    if tam > 0:
        while alrubros.tell() < tam and not encontrado:
            reg = pickle.load(alrubros)
            reg.codrubros = int(reg.codrubros)
            if reg.codrubros == codru:
                encontrado = True
    if encontrado:
        return True
    else:
        return False

def BuscoRepNomRu(nomru):
    tam = os.path.getsize(afrubros)
    alrubros.seek(0,0)
    reg = rubros()
    encontrado = False
    if tam > 0:
        while alrubros.tell() < tam and not encontrado:
            reg = pickle.load(alrubros)
            reg.nombrerubro = (reg.nombrerubro).strip()
            if reg.nombrerubro == nomru:
                encontrado = True
    if encontrado:
        return True
    else:
        return False

def BuscoSilo(codsilo):
    tam = os.path.getsize(afsilos)
    alsilos.seek(0,0)
    reg = silos()
    encontrado = False
    if tam > 0:
        while alsilos.tell() < tam and not encontrado:
            pos = alsilos.tell()
            reg = pickle.load(alsilos)
            reg.codsilos = int(reg.codsilos)
            if reg.codsilos == codsilo:
                encontrado = True
    if encontrado:
        return pos
    else:
        return False

def BuscoSilo2(codproducto):
    tam = os.path.getsize(afsilos)
    alsilos.seek(0,0)
    reg = silos()
    encontrado = False
    if tam > 0:
        while alsilos.tell() < tam and not encontrado:
            pos = alsilos.tell()
            reg = pickle.load(alsilos)
            reg.codprod = int(reg.codsilos)
            if reg.codprod == codproducto:
                encontrado = True
    if encontrado:
        return pos
    else:
        return False

def BuscoNombre(nombresilo):
    tam = os.path.getsize(afsilos)
    alsilos.seek(0,0)
    reg = silos()
    encontrado = False
    if tam > 0:
        while alsilos.tell() < tam and not encontrado:
            reg = pickle.load(alsilos)
            reg.nombre = (reg.nombre).strip(" ")
            if reg.nombre == nombresilo:
                encontrado = True
    if encontrado:
        return True
    else:
        return False

def PatXFecha(patente, fecha):
    patente = patente.ljust(7, ' ')
    if BuscoPatente(patente) != -1:
        pospat = BuscoPatente(patente)
        aloperaciones.seek(pospat)
        rl = pickle.load(aloperaciones)
        if rl.patente == patente and rl.fechacupo == fecha:
            return True
        else:
            return False
        
    else:
        return False

def BuscoPatente(npat):
    npat = npat.ljust(7, ' ')
    tam = os.path.getsize(afoperaciones)
    aloperaciones.seek(0,0)
    while aloperaciones.tell() < tam:
        pospat = aloperaciones.tell()
        vrtemp = pickle.load(aloperaciones)
        if vrtemp.patente == npat:
            return pospat
    return -1

def BuscoPatente2(npat):
    rloperaciones = operaciones()
    npat = npat.ljust(7, ' ')
    tam = os.path.getsize(afoperaciones)
    aloperaciones.seek(0)
    while aloperaciones.tell() < tam:
        vrtemp = pickle.load(aloperaciones)
        if vrtemp.patente == npat:
            return rloperaciones.codproducto
    return -1

def BuscoFecha(fecha,patente):
    tamaño = os.path.getsize(afoperaciones)
    pos = 0
    aloperaciones.seek(0,0)
    if (tamaño > 0):
        while (aloperaciones.tell() < tamaño):
            pos = aloperaciones.tell()
            rloperaciones = pickle.load(aloperaciones)
            rloperaciones.patente = rloperaciones.patente.strip(" ")
            if rloperaciones.patente == patente:
                if (rloperaciones.fechacupo == fecha):
                    return pos
        return -1
    else:
        print('!EL ARCHIVO NO CONTIENE DATOS!')
        return -1

def BuscoEstado(patente):
    tamaño = os.path.getsize(afoperaciones)
    aloperaciones.seek(0,0)
    encontrado = False
    while (aloperaciones.tell() < tamaño):
        pos = aloperaciones.tell()
        rloperaciones = pickle.load(aloperaciones)
        rloperaciones.patente = rloperaciones.patente.strip(" ")
        if (rloperaciones.patente == patente):
            encontrado = True
    if encontrado:
        return pos
    else:
        return -1

def BuscoBruto(patente):
    tamaño = os.path.getsize(afoperaciones)
    aloperaciones.seek(0,0)
    if (tamaño > 0):
        rloperaciones = pickle.load(aloperaciones)
        while (aloperaciones.tell() < tamaño) and (aloperaciones.patente != patente):
            pos = aloperaciones.tell()
            rloperaciones = pickle.load(aloperaciones)
            if (rloperaciones.patente == patente) and (rloperaciones.estado == 'B'):
                return pos
            else:
                return -1
    else:
        print('!EL ARCHIVO NO CONTIENE VALORES!')
        return -1

def BuscoValor(valor):
        tamaño = os.path.getsize(afrubrosp)
        alrubrosp.seek(0,0)
        if (tamaño > 0):
            rlrxp = pickle.load(alrubrosp)
            while (alrubrosp.tell() < tamaño):
                pos = alrubrosp.tell()
                rlrxp = pickle.load(alrubrosp)
                if (rlrxp.minimo <= valor) and (rlrxp.maximo >= valor):
                    return pos
                else:
                    return -1
        else:
            return -1

def BuscoTara(patente):
    tamaño = os.path.getsize(afoperaciones)
    aloperaciones.seek(0,0)
    if (tamaño > 0):
        rloperaciones = pickle.load(aloperaciones)
        while (aloperaciones.tell() < tamaño) and (aloperaciones.patente != patente):
            pos = aloperaciones.tell()
            rloperaciones = pickle.load(aloperaciones)
            if (rloperaciones.patente == patente) and (rloperaciones.estado != 'B'):
                return pos
            else:
                return -1
    else:
        print('!EL ARCHIVO NO CONTIENE VALORES!')
        return -1

def BuscoTara2(patente):
    tamaño = os.path.getsize(afoperaciones)
    aloperaciones.seek(0,0)
    if (tamaño > 0):
        rloperaciones = pickle.load(aloperaciones)
        while (aloperaciones.tell() < tamaño) and (aloperaciones.patente != patente):
            pos = aloperaciones.tell()
            rloperaciones = pickle.load(aloperaciones)
            if (rloperaciones.patente == patente) and (rloperaciones.estado != 'B'):
                return pos
            else:
                return 1
    else:
        print('!EL ARCHIVO NO CONTIENE VALORES!')
        return -1

def CuentoCupos():
    cuentocupos = 0
    tam = os.path.getsize(afoperaciones)
    aloperaciones.seek(0,0)
    while aloperaciones > tam:
        cuentocupos += 1
        pickle.load(aloperaciones)
    return cuentocupos

def validarFormatoFecha():
    booleano = True
    while booleano:
        try:
            fecha = input("Ingresa una fecha en el formato DD/MM/AA: ")
            datetime.strptime(fecha, '%d/%m/%y')
            clearconsole()
            print("Fecha correcta")
            booleano = False
        except ValueError:
            clearconsole()
            print("Fecha incorrecta")
    return fecha

def ValidarFecha2(p):
    tam = os.path.getsize(afrechazados)
    alrechazados.seek(0)
    temp = operaciones()
    encontrado = False
    while alrechazados.tell() < tam and not encontrado:
        pos=alrechazados.tell()
        temp = pickle.load(alrechazados)
        if temp.Fecha == p:
            encontrado = True
    if encontrado:
        return pos
    else:
        return -1

#------------------------------------------------> ALTAS <--------------------------------------------------------

#Alta Productos
def AltaProd():
    rlcxp = camionesxproductos()
    print('>>> A. ALTA \n')
    op = input('¿Desea dar de alta productos? S/N: ').upper()
    print()
    while (op != 'N') and (op != 'S'):
        op = input('INGRESE S o N PARA DAR DE ALTA: ').upper()
    if (op != 'N'):
        produ = str(input("Ingrese el nombre del producto: ")).upper()
        busca = BuscoRepNomProd(produ)
        while(len(produ)> 20 or busca != False):
            produ = str(input("Nombre demasiado largo o repetido, ingrese otro: "))
        codprodu = str(input("Ingrese el codigo del producto (5 caracteres) a registrar: "))
        busca = BuscoRepCodProd(codprodu)
        while(len(codprodu) != 5 or busca != -1):
            codprodu= str(input("Codigo repetido o muy corto, ingrese uno valido (5 caracteres): "))
            busca = BuscoRepCodProd(codprodu)
        rlproductos = productos()
        rlproductos.nombreprod=produ
        rlproductos.codprod=codprodu
        rlproductos.estado = "A"
        formatearProducto(rlproductos)
        alproductos.seek(0,2)
        pickle.dump(rlproductos,alproductos)
        alproductos.flush()
        alcamxprod.seek(0,2)
        rlcxp.prodcod = codprodu
        rlcxp.cantprod = 0
        rlcxp.netototal = 0
        rlcxp.promedio = 0
        rlcxp.nombreprod = produ
        rlcxp.menorpat = ""
        rlcxp.menorpeso = 0
        FormatearCamionesxProducto(rlcxp)
        pickle.dump(rlcxp,alcamxprod)
        alcamxprod.flush()
        print("Producto dado de alta con exito.")
        pausa()
        clearconsole()

#Alta rubros
def Altac():
    print('>>> A. ALTA \n')
    dec=input("¿Desea ingresar un rubro? S/N: ").upper()
    while dec!= "S" and dec!= "N":
        dec=input("Opcion invalida, por favor indique S/N!: ").upper()
    if (dec != "N"):
        codru = int(input("Ingrese el codigo de Rubro: "))
        buscac = BuscoRepCodRu(codru)
        while buscac != False:
            codru = int(input("Codigo repetido, ingrese uno valido (númerico): "))
            buscac = BuscoRepCodRu(codru)
        nomru = input("Ingrese el nombre del Rubro: ")
        busca = BuscoRepNomRu(nomru)
        while len(nomru)>10 or busca == True:
            nomru = input("Nombre demasiado largo o repetido, ingrese otro: ")
            busca = BuscoRepNomRu(nomru)
        rlrubros = rubros()
        rlrubros.codrubros = codru
        rlrubros.nombrerubro = nomru
        formatearRubro(rlrubros)
        alrubros.seek(0,2)
        pickle.dump(rlrubros,alrubros)
        alrubros.flush()
        print(green+"El rubro ha sido dado de alta exitosamente.\n"+reset)
        ORDENAMIENTO()
        pausa()
        clearconsole()
    else:
        print('Los datos no fueron dados de alta...\n')
        pausa()
    clearconsole()
    pausa()
    clearconsole()

#Alta RubrosXProductos
def Altad():
    print('>>> A. ALTA \n')
    dec=input("¿Desea realizar una carga? S/N: ").upper()
    while dec != "N" and dec != "S":
        dec=input("Opcion invalida, ingrese S/N: ").upper()
    if dec == "S":
        codproducto = str(input("Ingrese un codigo de Producto valido: "))
        busca = BuscoRepCodProd(codproducto)
        while busca == -1 :
            busca = codproducto = str(input("Ingrese un codigo de Producto valido: "))
        codrubro = int(input("Ingrese un codigo de rubro valido: "))
        busca = DICOTOMICARUBROS(codrubro)
        while(busca == -1):
            codrubro = int(input("Codigo no existente, ingrese otro: "))
            busca = DICOTOMICARUBROS(codrubro)
        menor = float(input("Ingrese el valor minimo admitido: "))
        while menor < 0:
            menor = float(input("El minimo no puede ser menor a 0, ingrese un número valido: "))
        mayor = float(input("Ingrese el valor maximo admitido: "))
        while mayor > 100:
            mayor = float(input("El maximo no puede ser mayor a 100, ingrese un número valido: "))
        rlrxp = rubrosXproductos()
        rlrxp.codprod = codproducto
        rlrxp.codrubros = codrubro
        rlrxp.minimo = menor
        rlrxp.maximo = mayor
        FormatearRXP(rlrxp)
        alrubrosp.seek(0,2)
        pickle.dump(rlrxp,alrubrosp)
        alrubrosp.flush()
        print(green+"El producto ha sido dado de alta exitosamente.\n"+reset)
        pausa()
        clearconsole()
    clearconsole()
    pausa()
    clearconsole()

#Alta silos
def Altae():
    print('>>> A. ALTA \n')
    print()
    dec = input("¿Desea iniciar la carga? S/N: ").upper()
    while (dec != "S") and (dec != "N"):
        dec = input("Opcion invalida, seleccione otra: ")
    if (dec == 'S'):
        codproducto = int(input("Ingrese el codigo del producto: "))
        buscorep = BuscoRepCodProd(codproducto)
        if (buscorep != -1):
            alproductos.seek(buscorep,0)
            rlproductos = pickle.load(alproductos)
            if rlproductos.estado != "F":
                clearconsole()
                codsilo = input("Ingrese el codigo del silo: ")
                BuscoSilo(codsilo)
                while (len(codsilo) != 5) or (BuscoSilo == pos):
                    codsilo = input("Codigo invalido, ingrese otro: ")
                nombresilo = input("Ingrese el nombre del silo: ")
                BuscoNombre(nombresilo)
                while len(nombresilo) > 10 or BuscoNombre == True:
                    nombresilo=input("Nombre ya existente, ingrese otro: ")
                silo = silos()
                silo.codsilos = codsilo
                silo.nombre = nombresilo
                silo.codprod = codproducto
                silo.stock = 0
                pickle.dump(silo,alsilos)
                alsilos.flush()
            else:
                print(red+"El producto referente esta dado de baja."+reset)
                pausa()
        else:
            print(red+"El producto referente no existe."+reset)
            pausa()
    clearconsole()
    print(green+"¡Hasta la proxima!"+reset)
    print()
    pausa()
    clearconsole()

#-------------------------------------------> BAJA PRODUCTOS <----------------------------------------------------

def BajaProductos():
    rlproductos=productos()
    print('>>> B. BAJA ')
    print()
    op = input('¿Desea dar de baja productos? S/N: ').upper()
    print()
    while (op != 'N') and (op != 'S'):
        op = input('INGRESE S o N PARA DAR DE BAJA: ').upper()
    if (op != 'N'):
        codprodu = input("Ingrese el codigo del producto que desea dar de baja: ")
        busco = BuscoRepCodProd(codprodu)
        if busco != -1:
            alproductos.seek(busco,0)
            rlproductos=pickle.load(alproductos)
            if rlproductos.estado != "B":
                op=input("¿Desea dar de baja el producto?: ").upper()
                while op != "S" and op != "N":
                    op=input("Opcion invalida, seleccione una valida S/N: ").upper()
                if op != "N":
                    alproductos.seek(busco,0)
                    rlproductos.estado = "B"
                    formatearProducto(rlproductos)
                    pickle.dump(rlproductos,alproductos)
                    alproductos.flush()
                    clearconsole()
                    print(green+"El producto ha sido dado de baja exitosamente.\n"+reset)
                    pausa()
                    clearconsole()
            else:
                clearconsole()
                print(red+"El producto ya esta dado de baja."+reset)
                pausa()
        else:
            clearconsole()
            print(red+"El producto no existe."+reset)
            pausa()
    else:
        clearconsole()
        pausa()
        clearconsole()

#---------------------------------------> MODIFICACION PRODUCTOS <----------------------------------------------------

def ModProductos():
    rlproductos = productos()
    print('>>> M. MODIFICACIÓN ')
    print()
    op = input('¿Desea modificar productos? S/N: ').upper()
    print()
    while (op != 'N') and (op != 'S'):
        op = input('INGRESE S o N PARA MODIFICAR PRODUCTOS: ').upper()
    if (op != 'N'):
        codprodu = input("Ingrese el codigo del producto que desea modificar: ")
        busco = BuscoRepCodProd(codprodu)
        buscoestado = BuscoEstadoCodProd(codprodu)
        if busco != -1:
            alproductos.seek(busco,0)
            rlproductos = pickle.load(alproductos)
            if rlproductos.estado != "B":
                op=input("¿Desea modificar el producto? S/N: ").upper()
                while op != "S" and "N":
                    op=input("Opcion invalida, seleccione una valida S/N: ").upper()
                if op == "S":
                    rlproductos.nombreprod = input("Ingrese el nuevo nombre del producto: ").upper()
                    rlproductos.nombreprod = rlproductos.nombreprod.ljust(10,' ')
                    busco2 = BuscoRepNomProd(rlproductos.nombreprod)
                    if busco2 == False:
                        confirma = input("¿Desea confirmar los cambios? S/N: ").upper()
                        while (confirma != "S") and (confirma != "N"):
                            confirma = input("Opcion invalida, Confirma? S/N: ").upper()
                        alproductos.seek(busco,0)
                        formatearProducto(rlproductos)
                        pickle.dump(rlproductos,alproductos)
                        alproductos.flush()
                        clearconsole()
                        print(green+"El producto ha sido modificado exitosamente."+reset)
                        pausa()
                    else:
                        clearconsole()
                        print(red+"El producto ya existe."+reset)
                        pausa()
            else:
                clearconsole()
                print(red+"El producto esta dado de baja."+reset)
                pausa()
        else:
            clearconsole()
            print(red+"El producto que desea modificar no existe."+reset)
            pausa()
        op = input('¿Desea ingresar nuevos datos? S / N: ').upper()
        while (op != 'S') and (op != 'N'):
            op = input('INGRESE S o N PARA MODIFICAR PRODUCTOS: ').upper()
    else:
        clearconsole()
        pausa()
        clearconsole()

#-----------------------------------------> CONSULTA PRODUCTOS <-------------------------------------------------------

def ConsultaProductos():
    rlproducto = productos()
    print('>>> C. CONSULTA\n')
    op = input('¿Desea consultar productos? S/N: ').upper()
    while (op != 'N') and (op != 'S'):
        op = input('INGRESE S o N PARA CONSULTAR PRODUCTOS: ').upper()
    print()
    if (op != 'N'):
        print(">>>> LISTA DE PRODUCTOS <<<<")
        alproductos.seek(0,0)
        tam = os.path.getsize(afproductos)
        while alproductos.tell() < tam:
            rlproducto = pickle.load(alproductos)
            print(f"NOMBRE: {rlproducto.nombreprod} CÓDIGO: {rlproducto.codprod} ESTADO: {rlproducto.estado}")
    pausa()
    clearconsole()

#----------------------------------------------> OPCIONES <-------------------------------------------------------

def OpcionesProducto():
    print('>>> B. PRODUCTOS <<<\n')
    print('A. ALTA')
    print('B. BAJA')
    print('C. CONSULTA')
    print('M. MODIFICACIÓN')
    print('V. VOLVER AL MENÚ ANTERIOR\n')
    op2 = input('INGRESE UNA OPCIÓN: ').upper()
    clearconsole()
    while (op2 <= 'A') and (op2 >= 'N'):
        op2 = input('!OPCIÓN INVÁLIDA!').upper()
    while(op2 != 'V'):
        if (op2 == 'A'):
            clearconsole()
            print('>>> B. PRODUCTOS <<<')
            print()
            AltaProd()
        elif (op2 == 'B'):
            clearconsole()
            print('>>> B. PRODUCTOS <<<')
            print()
            BajaProductos()
        elif (op2 == 'C'):
            clearconsole()
            print('>>> B. PRODUCTOS <<<')
            print()
            ConsultaProductos()
        elif (op2 == 'M'):
            clearconsole()
            print('>>> B. PRODUCTOS <<<')
            print()
            ModProductos()
        else:
            clearconsole()
            print('x ¡OPCIÓN INVÁLIDA! x\n')
            pausa()
            clearconsole()
        clearconsole()
        print('>>> B. PRODUCTOS <<<')
        print()
        print('A. ALTA')
        print('B. BAJA')
        print('C. CONSULTA')
        print('M. MODIFICACIÓN')
        print('V. VOLVER AL MENÚ ANTERIOR')
        print()
        op2 = input('INGRESE UNA OPCIÓN: ').upper()
        clearconsole()

def OpcionesRubros():
    print('>>> C. RUBROS <<<')
    print()
    print('A. ALTA')
    print('B. BAJA')
    print('C. CONSULTA')
    print('M. MODIFICACIÓN')
    print('V. VOLVER AL MENÚ ANTERIOR')
    print()
    op2 = input('INGRESE UNA OPCIÓN: ').upper()
    while (op2 <= 'A') and (op2 >= 'N'):
        op2 = input('!OPCIÓN INVÁLIDA!').upper()
    while(op2 != 'V'):
        if (op2 == 'A'):
            clearconsole()
            print('>>> C. RUBROS <<<')
            print()
            Altac()
        elif (op2 == 'B'):
            clearconsole()
            print('>>> C. RUBROS <<<')
            print()
            print('>>> B. BAJA')
            print()
            print('>>> ESTA FUNCIONALIDAD ESTÁ EN CONSTRUCCIÓN <<<')
            print()
            pulse = input('* Pulse ENTER para volver a opciones de rubros...')
            clearconsole()
        elif (op2 == 'C'):
            clearconsole()
            print('>>> C. RUBROS <<<')
            print()
            print('>>> C. CONSULTA')
            print()
            print('>>> ESTA FUNCIONALIDAD ESTÁ EN CONSTRUCCIÓN <<<')
            print()
            pulse = input('* Pulse ENTER para volver a opciones de rubros...')
            clearconsole()
        elif (op2 == 'M'):
            clearconsole()
            print('>>> C. RUBROS <<<')
            print()
            print('>>> M. MODIFICACIÓN')
            print()
            print('>>> ESTA FUNCIONALIDAD ESTÁ EN CONSTRUCCIÓN <<<')
            print()
            pulse = input('* Pulse ENTER para volver a opciones de rubros...')
            clearconsole()
        else:
            clearconsole()
            print('x ¡OPCIÓN INVÁLIDA! x')
            print()
            pausa()
            clearconsole()
        print('>>> C. RUBROS <<<')
        print()
        print('A. ALTA')
        print('B. BAJA')
        print('C. CONSULTA')
        print('M. MODIFICACIÓN')
        print('V. VOLVER AL MENÚ ANTERIOR')
        print()
        op2 = input('INGRESE UNA OPCIÓN: ').upper()
        clearconsole()

def OpcionesRXP():
    print('>>> D. RUBROS x PRODUCTO <<<')
    print()
    print('A. ALTA')
    print('B. BAJA')
    print('C. CONSULTA')
    print('M. MODIFICACIÓN')
    print('V. VOLVER AL MENÚ ANTERIOR')
    print()
    op2 = input('INGRESE UNA OPCIÓN: ').upper()
    while (op2 <= 'A') and (op2 >= 'N'):
        op2 = input('!OPCIÓN INVÁLIDA!').upper()
    while(op2 != 'V'):
        if (op2 == 'A'):
            clearconsole()
            print('>>> D. RUBROS x PRODUCTO <<<')
            print()
            Altad()
        elif (op2 == 'B'):
            clearconsole()
            print('>>> D. RUBROS x PRODUCTO <<<')
            print()
            print('>>> B. BAJA')
            print()
            print('>>> ESTA FUNCIONALIDAD ESTÁ EN CONSTRUCCIÓN <<<')
            print()
            pulse = input('* Pulse ENTER para volver a opciones de rubros x producto...')
            clearconsole()
        elif (op2 == 'C'):
            clearconsole()
            print('>>> D. RUBROS x PRODUCTO <<<')
            print()
            print('>>> C. CONSULTA')
            print()
            print('>>> ESTA FUNCIONALIDAD ESTÁ EN CONSTRUCCIÓN <<<')
            print()
            pulse = input('* Pulse ENTER para volver a opciones de rubros x producto...')
            clearconsole()
        elif (op2 == 'M'):
            clearconsole()
            print('>>> D. RUBROS x PRODUCTO <<<')
            print()
            print('>>> M. MODIFICACIÓN')
            print()
            print('>>> ESTA FUNCIONALIDAD ESTÁ EN CONSTRUCCIÓN <<<')
            print()
            pulse = input('* Pulse ENTER para volver a opciones de rubros x producto...')
            clearconsole()
        else:
            clearconsole()
            print('x ¡OPCIÓN INVÁLIDA! x')
            print()
            pausa()
            clearconsole()
        print('>>> D. RUBROS x PRODUCTO <<<')
        print()
        print('A. ALTA')
        print('B. BAJA')
        print('C. CONSULTA')
        print('M. MODIFICACIÓN')
        print('V. VOLVER AL MENÚ ANTERIOR')
        print()
        op2 = input('INGRESE UNA OPCIÓN: ').upper()
        clearconsole()

def OpcionesSilos():
    print('>>> E. SILOS <<<')
    print()
    print('A. ALTA')
    print('B. BAJA')
    print('C. CONSULTA')
    print('M. MODIFICACIÓN')
    print('V. VOLVER AL MENÚ ANTERIOR')
    print()
    op2 = input('INGRESE UNA OPCIÓN: ').upper()
    while (op2 <= 'A') and (op2 >= 'N'):
        op2 = input('!OPCIÓN INVÁLIDA!').upper()
    while(op2 != 'V'):
        if (op2 == 'A'):
            clearconsole()
            print('>>> E. SILOS <<<')
            Altae()
        elif (op2 == 'B'):
            clearconsole()
            print('>>> E. SILOS <<<')
            print()
            print('>>> B. BAJA')
            print()
            print('>>> ESTA FUNCIONALIDAD ESTÁ EN CONSTRUCCIÓN <<<')
            print()
            pulse = input('* Pulse ENTER para volver a opciones de silos...')
            clearconsole()
        elif (op2 == 'C'):
            clearconsole()
            print('>>> E. SILOS <<<')
            print()
            print('>>> C. CONSULTA')
            print()
            print('>>> ESTA FUNCIONALIDAD ESTÁ EN CONSTRUCCIÓN <<<')
            print()
            pulse = input('* Pulse ENTER para volver a opciones de silos...')
            clearconsole()
        elif (op2 == 'M'):
            clearconsole()
            print('>>> E. SILOS <<<')
            print()
            print('>>> M. MODIFICACIÓN')
            print()
            print('>>> ESTA FUNCIONALIDAD ESTÁ EN CONSTRUCCIÓN <<<')
            print()
            pulse = input('* Pulse ENTER para volver a opciones de silos...')
            clearconsole()
        else:
            clearconsole()
            print('x ¡OPCIÓN INVÁLIDA! x')
            print()
            pausa()
            clearconsole()
        print('>>> E. SILOS <<<')
        print()
        print('A. ALTA')
        print('B. BAJA')
        print('C. CONSULTA')
        print('M. MODIFICACIÓN')
        print('V. VOLVER AL MENÚ ANTERIOR')
        print()
        op2 = input('INGRESE UNA OPCIÓN: ').upper()
        clearconsole()

#---------------------------------------------> ACUMULADORES <----------------------------------------------------

#En este módulo se suman cupos, camiones recibidos y cantidad de productos
def ACUMULOCUPOS():
    tam = os.path.getsize(aftotales)
    if tam > 0:
        altotales.seek(0,0)
        rltotales = totales()
        rltotales = pickle.load(altotales)
        rltotales.cupos = int(rltotales.cupos)
        rltotales.cupos += 1

    else:
        rltotales = totales()
        rltotales.cupos = 1
        rltotales.camionesrecib = 0
    FormatearTotales(rltotales)
    pickle.dump(rltotales,altotales)
    altotales.flush()
#Acumulo camiones recibidos

#Acumulo neto
def ACUMULONETO(posc,neto):
    alcamxprod.seek(posc,0)
    rlcampxprod = pickle.load(alcamxprod)
    alcamxprod.seek(posc,0)
    rlcampxprod.netototal = int(rlcampxprod.netototal)
    rlcampxprod.netototal += neto
    pickle.dump(rlcampxprod,alcamxprod)
    alcamxprod.flush()

#Busco peso y patente menor
def MENOR(posc,neto, patente):
    alcamxprod.seek(posc,0)
    rlcampxprod = pickle.load(alcamxprod)
    alcamxprod.seek(posc,0)
    rlcampxprod.menorpeso = int(rlcampxprod.menorpeso)
    if (rlcampxprod.menorpeso < neto):
        rlcampxprod.menorpeso = neto
        rlcampxprod.menorpat = patente
    elif (rlcampxprod.menorpeso == 0):
        rlcampxprod.menorpeso = neto
        rlcampxprod.menorpat = patente
    pickle.dump(rlcampxprod,alcamxprod)
    alcamxprod.flush()

#-------------------------------------------> 1. ADMINISTRACIONES <-----------------------------------------------

def ADMINISTRACIONES():
    clearconsole()
    print('>>> BIENVENIDO AL MENU DE ADMINISTRACIONES <<<')
    print()
    print('A - TITULARES') #construccion
    print('B - PRODUCTOS')
    print('C - RUBROS')
    print('D - RUBROS x PRODUCTO')
    print('E - SILOS')
    print('F - SUCURSALES') #construccion
    print('G - PRODUCTOS POR TITULAR') #construccion
    print('V - VOLVER AL MENÚ PRINCIPAL')
    print()
    op = input('INGRESE UNA OPCIÓN: ').upper()
    clearconsole()
    while (op !='V'):
        if(op == 'A'):
            clearconsole()
            print('>>> A - TITULARES <<<')
            print()
            print('>>> ESTA FUNCIONALIDAD ESTÁ EN CONSTRUCCIÓN')
            print()
            pulse = input('* Pulse ENTER para volver al MENÚ ADMINISTRACIONES...')
            clearconsole()
        elif(op == 'B'):
            clearconsole()
            OpcionesProducto()
        elif(op == 'C'):
            clearconsole()
            OpcionesRubros()
        elif(op =='D'):
            clearconsole()
            OpcionesRXP()
        elif(op == 'E'):
            clearconsole()
            OpcionesSilos()
        elif(op == 'F'):
            clearconsole()
            print('>>> F - SUCURSALES <<<')
            print()
            print('>>> ESTA FUNCIONALIDAD ESTÁ EN CONSTRUCCIÓN ')
            print()
            pulse = input('* Pulse ENTER para volver al MENÚ ADMINISTRACIONES...')
            clearconsole()
        elif(op == 'G'):
            clearconsole()
            print('>>> G - PRODUCTOS POR TITULAR <<<')
            print()
            print('>>> ESTA FUNCIONALIDAD ESTÁ EN CONSTRUCCIÓN')
            print()
            pulse = input('* Pulse ENTER para volver al MENÚ ADMINISTRACIONES...')
            clearconsole()
        else:
            clearconsole()
            print('x ¡OPCIÓN INVÁLIDA! x')
            print()
            pulse = input('* Pulse ENTER para reintentar...')
            clearconsole()
        print('>>> BIENVENIDO AL MENU DE ADMINISTRACIONES <<<')
        print()
        print('A - TITULARES')
        print('B - PRODUCTOS')
        print('C - RUBROS')
        print('D - RUBROS x PRODUCTO')
        print('E - SILOS')
        print('F - SUCURSALES')
        print('G - PRODUCTOS POR TITULAR')
        print('V - VOLVER AL MENÚ PRINCIPAL')
        print()
        op = input('INGRESE UNA OPCIÓN NUEVAMENTE: ').upper()
        clearconsole()

#-------------------------------------------> 2. ENTREGA DE CUPOS <-----------------------------------------------

def ENTREGADECUPOS():
    print('>>> BIENVENIDO A ENTREGA DE CUPOS <<<')
    print()
    opcion = input('¿Desea pedir un cupos? S/N: ').upper()
    print()
    while (opcion != 'N') and (opcion != 'S'):
        opcion = input('Ingrese S o N para pedir cupo: ').upper()
    if opcion != "N":
        clearconsole()
        print('>>> 2. ENTREGA DE CUPOS <<<')
        print()
        Patente_Camion = str(input("Ingrese un número de patente: "))
        while(len(Patente_Camion) < 6 or len(Patente_Camion) > 7):
            Patente_Camion = str(input("Ingrese una patente VÁLIDA: "))
        rloperaciones = operaciones()
        print('>>> 2. ENTREGA DE CUPOS <<<')
        print()
        fecharep = validarFormatoFecha()
        while PatXFecha(Patente_Camion,fecharep) == True:
            print(f"Cupo ya otorgado a la patente {Patente_Camion} en esta fecha, por favor ingrese otra fecha: ")
            fecharep = validarFormatoFecha()
        codigo = int(input("Ingrese el codigo del producto: "))
        teencontre = BuscoRepCodProd(codigo)
        while (teencontre == -1):
            codigo = int(input("Codigo no encontrado o dado de baja, ingrese un codigo valido: "))
            teencontre = BuscoRepCodProd(codigo)
        rloperaciones.patente = Patente_Camion
        rloperaciones.fechacupo = fecharep
        rloperaciones.codproducto = codigo
        rloperaciones.estado = "P"
        FormatearOperaciones(rloperaciones)
        pickle.dump(rloperaciones,aloperaciones)
        aloperaciones.flush()
        print(">>> Ingreso exitoso <<<")
        ACUMULOCUPOS()
    clearconsole()
    pausa()
    clearconsole()

#----------------------------------------------> 3. RECEPCIÓN <---------------------------------------------------

# variables: patente,fecha: string; opcion: char;
def RECEPCION():
    print('>>> BIENVENIDO A RECEPCIÓN <<<\n')
    rltot = totales()
    opcion = input('¿Desea realizar una recepción? S/N: ').upper()
    while (opcion != 'N') and (opcion != 'S'):
        opcion = input('Ingrese S o N para realizar una recepción: ').upper()
    while (opcion != 'N'):
        clearconsole()
        print('>>> 3. RECEPCION <<<')
        print()
        patente = input('Ingrese número de patente: ').upper()
        while (len(patente) <= 6) and (len(patente) >= 7):
            patente = input('La patente debe tener entre 6 y 7 caracteres: ').upper()
        posp = BuscoPatente(patente)
        if (posp != -1):
            posf = BuscoFecha(fechahoy,patente)
            print(posf)
            if (posf != -1):
                aloperaciones.seek(posf,0)
                rloperaciones = pickle.load(aloperaciones)
                aloperaciones.seek(posf,0) 
                if (rloperaciones.estado == 'P'):
                    rloperaciones.estado = 'A'
                    FormatearOperaciones(rloperaciones)
                    pickle.dump(rloperaciones, aloperaciones)
                    aloperaciones.flush()
                    altotales.seek(0,0)
                    rltot = pickle.load(altotales)
                    altotales.seek(0,0)
                    rltot.camionesrecib = int(rltot.camionesrecib)
                    rltot.camionesrecib += 1
                    FormatearTotales(rltot)
                    pickle.dump(rltot, altotales)
                    altotales.flush()
                    print('¡Recepción exitosa!')
                    print()
                else:
                    print('\n¡LOS DATOS NO COINCIDEN!\n')
                    pausa()
                    clearconsole()
            else:
                print('\n¡LOS DATOS NO COINCIDEN!\n')
                pausa()
                clearconsole()
        else:
            print('\n¡LA PATENTE NO EXISTE!\n')
            pausa()
            clearconsole()
        clearconsole()
        print('>>> 3. RECEPCIÓN <<<')
        print()
        opcion = input('¿Desea verificar otra recepción? S/N: ').upper()
        while (opcion != 'S') and (opcion != 'N'):
            opcion = input('Ingrese S o N para realizar recepción: ').upper()
    clearconsole()
    pausa()
    clearconsole()

#-------------------------------------------> 4. REGISTRAR CALIDAD <----------------------------------------------
        # self.codrubros = 0
        # self.codprod = 0
        # self.minimo = 0 
        # self.maximo = 0
def validarValor(prod):
    total=0
    t = os.path.getsize(afrubrosp)
    alrubrosp.seek(0, 0)
    b = rubrosXproductos()
    encontrado = False
    while alrubrosp.tell()<t:
        b = pickle.load(alrubrosp)
        b.codrubros=int(b.codrubros)
        b.codprod=int(b.codprod)
        b.maximo=float(b.maximo)
        b.minimo=float(b.minimo)
        if b.codprod == int(prod):
            total+=1
            pos=DICOTOMICARUBROS(b.codrubros)
            alrubros.seek(pos,0)
            rubros=pickle.load(alrubros)
            rubros.nombrerubro=rubros.nombrerubro.strip(" ")
            valor=float(input((f"Ingrese el valor del camión para el rubro {rubros.nombrerubro}: ")))
            if valor > b.maximo or valor < b.minimo:
                if total==2:
                    print("No cumplio con mas de 1 rubro")
                    return False
            else:
                encontrado = True
    if valor > b.maximo or valor < b.minimo and total == 1:
        return False
    if encontrado:
        return encontrado
    else:
        return -1

def CALIDAD():
    if os.path.getsize(afrubros) != 0:
        ORDENAMIENTO()
        Operacion=operaciones()
        rec=rechazados()
        patente = input('Ingrese número de patente: ').upper()
        while (len(patente) <= 6) and (len(patente) >= 7):
            patente = input('La patente debe tener entre 6 y 7 caracteres: ').upper()
        buscapat=BuscoPatente(patente)
        if buscapat!=-1:
            valida=BuscoFecha(fechahoy,patente)
            if valida != -1:
                aloperaciones.seek(valida,0)
                rlop = pickle.load(aloperaciones)
                aloperaciones.seek(valida,0)
                if rlop.estado == "A":
                    Operacion=pickle.load(aloperaciones)
                    v = validarValor(Operacion.codproducto)
                    if v !=-1:
                        if v == False:
                            clearconsole()
                            print(red+"El producto no cuenta con la calidad deseada."+reset)
                            pausa()
                            aloperaciones.seek(valida,0)
                            Operacion=pickle.load(aloperaciones)
                            Operacion.estado = "R"
                            aloperaciones.seek(valida,0)
                            rec.patente=Operacion.patente
                            rec.fechacupo=Operacion.fechacupo
                            pickle.dump(rec,alrechazados)
                            alrechazados.flush()
                            pickle.dump(Operacion,aloperaciones)
                            aloperaciones.flush()
                        else:
                            clearconsole()
                            print(green+"El producto cumple con los estandares de calidad."+reset)
                            pausa()
                            aloperaciones.seek(valida,0)
                            Operacion=pickle.load(aloperaciones)
                            Operacion.estado = "C"
                            aloperaciones.seek(valida,0)
                            pickle.dump(Operacion,aloperaciones)
                            aloperaciones.flush()
                    else:
                        clearconsole()
                        print(red+"No se encontró ese rubro para el producto."+reset)
                        pausa()
                else:
                    clearconsole()
                    print(red+"La patente no se encuentra en estado correspondiente."+reset)
                    pausa()
            else:
                clearconsole()
                print(red+"No arribó ese camión hoy."+reset)
                pausa()
        else:
            clearconsole()
            print(red+"No se encontro la patente."+reset)
            pausa()
    else:
        clearconsole()
        print(red+"No hay rubros cargados."+reset)
        pausa()

#------------------------------------------> 5. REGISTRAR PESO BRUTO <--------------------------------------------

def PESO():
    print('>>> BIENVENIDO A PESO BRUTO <<<\n')
    opcion = input('¿Desea registrar peso bruto? S/N: ').upper()
    while (opcion != 'N') and (opcion != 'S'):
        opcion = input('Ingrese S o N para registrar peso bruto: ').upper()
    while (opcion != 'N'):
        clearconsole()
        print('>>> 5. REGISTRAR PESO BRUTO <<<')
        print()
        patente = input('Ingrese patente: ').upper()
        while (len(patente) <= 6) and (len(patente) >= 7):
            patente = input('La patente debe tener entre 6 y 7 caracteres: ').upper()
        posc = BuscoEstado(patente)
        print(posc)
        if (posc != -1):
            aloperaciones.seek(posc,0)
            rlop = pickle.load(aloperaciones)
            aloperaciones.seek(posc,0)
            rlop.bruto = int(input('Ingrese peso: '))
            while (rlop.bruto < 0):
                rlop.bruto = int(input('Peso ingresado incorrecto (debe ser mayor a 0)'))
            rlop.estado = 'B'
            FormatearOperaciones(rlop)
            pickle.dump(rlop, aloperaciones)
            aloperaciones.flush()
            print('¡El peso se ha ingresado correactamente!')
        else:
            print('\n¡ESA PATENTE NO EXISTE!\n')
            reintentar = input('* Pulse ENTER para reintentar...')
            clearconsole()
        clearconsole()
        print('>>> 5. REGISTRAR PESO BRUTO <<<')
        print()
        opcion = input('¿Desea ingresar otro peso bruto? S/N: ').upper()
        while (opcion != 'S') and (opcion != 'N'):
            opcion = input('Ingrese S o N para registrar peso bruto: ').upper()
    clearconsole()
    pulse = input('Pulse ENTER para volver al MENÚ PRINCIPAL...')
    clearconsole()

#---------------------------------------------> 7. REGISTRAR TARA <-----------------------------------------------

def TARA():
    rloperaciones = operaciones()
    rlsilos = silos()
    print('>>> BIENVENIDO A REGISTRAR TARA <<<\n')
    dec = input("¿Desea registrar una Tara? S/N: ").upper()
    while dec != "S" and dec != "N":
        dec = input("Opcion invalida, por favor seleccione S/N: ").upper()
    while dec != "N":
        clearconsole()
        print('>>> 7. REGISTRAR TARA')
        print()
        patente = input("Ingrese el número de patente: ").upper()
        while (len(patente) <= 6) and (len(patente) >= 7):
            patente = input('La patente debe tener entre 6 y 7 caracteres: ').upper()
        posc = BuscoEstado(patente)
        if posc != -1:
            aloperaciones.seek(posc,0)
            rlop = pickle.load(aloperaciones)
            rlop.tara = int(input('Ingrese peso: '))
            rlop.bruto = int(rlop.bruto)
            while (rlop.bruto < rlop.tara):
                rlop.tara = int(input('La tara no puede ser mayor al peso bruto, ingrese otra: '))
            neto = (rlop.bruto - rlop.tara)
            rlop.neto = neto
            ProdPat = BuscoPatente2(patente)
            pos = BuscoSilo2(ProdPat)
            alsilos.seek(pos,0)
            pickle.load(alsilos)
            alsilos.seek(pos,0)
            rlsilos.stock = int(rlsilos.stock)
            rlsilos.stock = (rlsilos.stock + neto)
            pickle.dump(rlsilos,alsilos)
            alsilos.flush()
            rlop.estado = "F"
            ACUMULONETO(posc,0)
            MENOR(posc,neto, patente)
            FormatearOperaciones(rlop)
            FormatearSilos(rlsilos)
            pickle.dump(rlop, aloperaciones)
            pickle.dump(rlsilos,alsilos)
            aloperaciones.flush()
            alsilos.flush()
            print('¡La tara se ha ingresado correactamente!')
        else:
            print('\n¡ESA PATENTE NO EXISTE!\n')
            reintentar = input('* Pulse ENTER para reintentar...')
            clearconsole()
        clearconsole()
        print('>>> 7. REGISTRAR TARA')
        print()
        dec = input('¿Desea ingresar otra tara? S/N: ').upper()
        while (dec != 'S') and (dec != 'N'):
            dec = input('Ingrese S o N para realizar registro de tara: ').upper()
    clearconsole()
    pausa()
    clearconsole()

#-----------------------------------------------> 8. REPORTES <---------------------------------------------------

def REPORTES():
    rltotales = totales()
    print('>>> BIENVENIDO A REPORTES <<<\n')
    dec=input("¿Desea iniciar un reporte? S/N: ").upper()
    while dec != "S" and dec != "N":
        dec=input("Opcion incorrecta, ¿S/N?: ").upper()
    if dec == 'S':
        clearconsole()
        print()
        print('>>> 8. REPORTES')
        print()
        #Cantidad de cupos
        cantcupos = CuentoCupos()
        print(f"Se han emitido {cantcupos} cupos")
        #Cantidad de camiones recibidos
        altotales.seek(0,0)
        print(f"Fueron recibidos {rltotales.camionesrecib} camiones.")
        #cant. camiones x producto
        tam = os.path.getsize(afcamxprod)
        alcamxprod.seek(0)
        while alcamxprod.tell() > tam:
            tem = pickle.load(alcamxprod)
            rlcampxprod = camionesxproductos()
            nombreprod = (tem.nombreprod).strip(" ")
            patentemenor = tem.patentemenor.strip(" ")
            tem.netototal = int(tem.netototal)
            tem.cantprod = int(tem.cantprod)
            print(f"El producto {nombreprod} tiene {int(tam.cantprod)} camiones.\n")
            print(f"El neto total de {nombreprod} es de {int(tem.netototal)} Kgs.\n")
            if tem.cantprod != 0:
                tem.netototal = int(tem.netototal)
                tem.cantprod = int(tem.cantprod)
                tem.prmedio = int(tem.prmedio)
                tem.promedio = tem.neto/tem.cantprod
                pickle.dump(tem,alcamxprod)
                alcamxprod.flush()
                print(f"El promedio del producto {nombreprod} es {float(tem.promedio)} Kgs. ")
            if patentemenor != "":
                print(f"El camion con la patente {patentemenor} fue el que menos cantidad de {nombreprod} descargó. ")
    else:
        clearconsole()
        pausa()
        clearconsole()

#-----------------------------------------------> SILO MAYOR <--------------------------------------------------

def SILOMAYOR():
    print(">>>> SILO CON MAYOR STOCK <<<<\n")
    dec=input("¿Desea revisar el silo con mayor stock? S/N: ").upper()
    while dec != "S" and dec != "N":
        dec=input("Opcion incorrecta, ¿S/N?: ").upper()
    if (dec != 'N'):
        tamañoS = os.path.getsize(afsilos)
        if (tamañoS > 0):
            alsilos.seek(0,0)
            while (alsilos.tell() < tamañoS):
                rlsilos = pickle.load(alsilos)
                rlsilos.stock = int(rlsilos.stock)
                if (rlsilos.stock > mayorStock):
                    mayorStock = rlsilos.stock
            print(f'>>> El silo con mayor stock es: {mayorStock}')
        else:
            print(red+'\n¡NO HAY SILOS REGISTRADOS!\n'+reset)
            pausa()
        clearconsole()
    else:
        pausa()
    clearconsole()


#---------------------------------------------> CAMIONES RECHAZADOS <--------------------------------------------------

def CRECHAZADOS():
    print(">>>> CAMIONES RECHAZADOS <<<<")
    print()
    dec=input("¿Desea revisar el silo con mayor stock? S/N: ").upper()
    while dec != "S" and dec != "N":
        dec=input("Opcion incorrecta, ¿S/N?: ").upper()
    while (dec != 'N'):
        fecha = input("Ingrese una fecha: ")
        busco = ValidarFecha2(fecha)
        if busco != -1:
            alrechazados.seek(busco,0)
            f = pickle.load(alrechazados)
            clearconsole()
            print(f"El dia {fecha} han sido rechazados los siguientes camiones: \n")
            tam = os.path.getsize(afrechazados)
            alrechazados.seek(0)
            while alrechazados.tell() > tam:
                var = pickle.load(alrechazados)
                if var.fecha == fecha:
                    print(var.patente)
        else:
            print()
            print('¡NO HAY CAMIONES RECHAZADOS!')
            reintentar = input('* Pulse ENTER para reintentar...')
            clearconsole()
        print()
        clearconsole()
        opcion = input('¿Desea  volver al menu listado de silos y rechazos? S/N: ').upper()
        while (opcion != 'S') and (opcion != 'N'):
            opcion = input('Ingrese S o N volver al menu listado de silos y rechazos: ').upper()
    clearconsole()
    pausa()
    clearconsole()

#-----------------------------------------> 9. LISTADO DE SILOS Y RECHAZOS <-------------------------------------------

# variables: opcion, tamañoS, tamañoF: string;

def LISTADO():
    print('>>> BIENVENIDO A LISTADO DE SILOS Y RECHAZOS <<<\n')
    print("1- SILO CON MAYOR STOCK.\n2- CAMIONES RECHAZADOS.\n3- VOLVER AL MENU ANTERIOR. \n")
    op =input("INGRESE UNA OPCION: ")
    while op != "3":
        if op == "1":
            clearconsole()
            SILOMAYOR()
        elif op == "2":
            clearconsole()
            CRECHAZADOS()
        else:
            clearconsole()
            print('x ¡OPCIÓN INVÁLIDA! x')
            print()
            pulse = input('* Pulse ENTER para reintentar...')
            clearconsole()
        print('>>> BIENVENIDO A LISTADO DE SILOS Y RECHAZOS <<<\n')
        print("1- SILO CON MAYOR STOCK.\n2- CAMIONES RECHAZADOS.\n3- VOLVER AL MENU ANTERIOR. \n")
        op =input("INGRESE UNA OPCION: ")
    clearconsole()
    pausa()
    clearconsole()

#-----------------------------------------------> EJECUCION <-----------------------------------------------------

PROGRAMA()