
#INTEGRANTES: ALESANDRONI VALENTINO, RUIZ MILTON FRANCO, RADINS NICOLAS ARIEL, RODRÍGUEZ MARTINIANO.

#------------------------------------------> Limpiar Consola <----------------------------------------------

import os
clearconsole= lambda: os.system('cls')

#----------------------------------------> COLORCITO <-------------------------------------------------
Negro= '\033[30m'
Rojo= '\033[31m'
Verde= '\033[32m'
Amarillo= '\033[33m'
Azul= '\033[34m'
Violeta= '\033[35m'
Cyan= '\033[36m'
Blanco= '\033[37m'
Reset = '\033[39m'

#---------------------------------------> MODULO DE ADMINISTRACIONES <--------------------------------------

# variables: op2: string

def MODULOADMINISTRACIONES():
    clearconsole()
    print(Cyan+">>> BIENVENIDO AL MENU ADMINISTRACIONES <<<\n")
    print(Amarillo+"A - TITULARES")
    print("B - PRODUCTOS")
    print("C - RUBROS")
    print("D - RUBROS x PRODUCTOS")
    print("E - SILOS")
    print("F - SUCURSALES")
    print("G - PRODUCTOS x TITULAR")
    print("V - VOLVER AL MENÚ PRINCIPAL")
    print(Reset+"")
    op2 = input(Cyan+'INGRESE UNA OPCIÓN: ').upper()
    print(Reset+"")
    while (op2!="V"):
        op2=op2.upper()
        if(op2=="A"):
            clearconsole()
            print(Cyan+">>>MENU DE OPCIONES DE TITULARES <<<")
            OPMENU()
        elif(op2=="B"):
            clearconsole()
            print(Cyan+">>> MENU DE OPCIONES DE PRODUCTOS <<<")
            OPMENUPRODUCTOS()
        elif(op2=="C"):
            clearconsole()
            print(Cyan+">>> MENU DE OPCIONES DE RUBROS <<<")
            OPMENU()
        elif(op2=="D"):
            clearconsole()
            print(Cyan+">>> MENU DE OPCIONES DE RUBROS x PRODUCTOS <<<")
            OPMENU()
        elif(op2=="E"):
            clearconsole()
            print(Cyan+">>> MENU DE OPCIONES DE SILOS <<<")
            OPMENU()
        elif(op2=="F"):
            clearconsole()
            print(Cyan+">>> MENU DE OPCIONES SUCURSALES <<<")
            OPMENU()
        elif(op2=="G"):
            clearconsole()
            print(Cyan+">>> MENU DE OPCIONES DE PRODUCTOS x TITULAR <<<")
            OPMENU()
        else:
            clearconsole()
            print(Rojo+"x ¡¡OPCION INVÁLIDA!! x")
            print(Reset+"")
        print(Cyan+">>> BIENVENIDO AL MENU ADMINISTRACIONES <<<\n")
        print(Reset+Amarillo+"A - TITULARES")
        print("B - PRODUCTOS")
        print("C - RUBROS")
        print("D - RUBROS x PRODUCTOS")
        print("E - SILOS")
        print("F - SUCURSALES")
        print("G - PRODUCTOS x TITULAR")
        print("V - VOLVER AL MENÚ PRINCIPAL\n")
        op2 = input(Cyan+'INGRESE UNA OPCIÓN NUEVAMENTE: ').upper()
        print(Reset+"")
    clearconsole()

#------------------> MODULO MENÚ DE OPCIONES <------------------------------

# variables: op3: string;

def OPMENU():
    print(Reset+Amarillo+"A. ALTA")
    print("B. BAJA")
    print("C. CONSULTA")
    print("M. MODIFICACION")
    print("V. VOLVER AL MENÚ ANTERIOR\n")
    op3=input(Cyan+"Ingrese una opcion:").upper()
    while(op3!="V"):
        if(op3=="A"):
            clearconsole()
            print(Reset+Rojo+"En construccion...")
            print(Reset+"")
        elif(op3=="B"):
            clearconsole()
            print(Rojo+"En construccion...")
            print(Reset+"")
        elif(op3=="C"):
            clearconsole()
            print(Rojo+"En construccion...")
            print(Reset+"")
        elif(op3=="M"):
            clearconsole()
            print(Rojo+"En construccion...")
            print(Reset+"")
        else:
            clearconsole()
            print(Rojo+"OPCION INVALIDA.")
            print(Reset+"")
        print(Cyan+"SELECCIONE UNA OPCION NUEVAMENTE\n")
        print(Reset+Amarillo+"A. ALTA")
        print("B. BAJA")
        print("C. CONSULTA")
        print("M. MODIFICACION")
        print("V. VOLVER AL MENÚ ANTERIOR\n")
        op3=input(Cyan+"Ingrese una opcion:").upper()
        print(Reset+"")
    clearconsole()

#-----------------> CALCULO DE PROMEDIOS <-------------------------------------

def PROMEDIOSINDIVIDUALES():
    global promedioSoja, promedioMaiz, promedioTrigo, promedioGirasol, promedioCebada

    if camionesSoja !=0:
        promedioSoja=netoSoja/camionesSoja

    if camionesMaiz!=0:
        promedioMaiz=netoMaiz/camionesMaiz

    if camionesTrigo!=0:
        promedioTrigo=netoTrigo/camionesTrigo

    if camionesGirasol!=0:
        promedioGirasol=netoGirasol/camionesGirasol

    if camionesCebada!=0:
        promedioCebada=netoCebada/camionesCebada


#-------------------> MENU DE OPCIONES DE PRODUCTO<----------------------------
def OPMENUPRODUCTOS():
    global ingresorecepcion, modificacion, ingresocupos
    print(Reset+Amarillo+"A. ALTA")
    print("B. BAJA")
    print("C. CONSULTA")
    print("M. MODIFICACION")
    print("V. VOLVER AL MENÚ ANTERIOR\n")
    op3=input(Cyan+"INGRESE UNA OPCIÓN: ")
    print(Reset+"")
    op3=op3.upper()
    if vecprod[0]=="" and vecprod[1]=="" and vecprod[2]=="":
        ingresorecepcion=False
        ingresocupos=False
    else:
        ingresorecepcion=True
        ingresocupos=True
    while(op3!="V"):
        if(op3=="A"):
            clearconsole()
            print(Cyan+">>> ALTA <<<\n")
            print("Ingrese el nombre de los prodctos:")
            print("PRODUCTOS DISPONIBLES:",Amarillo+" SOJA, MAIZ, TRIGO, GIRASOL Y CEBADA / Presionar ENTER para no ingresar un producto")
            for i in range (0,3):
                vecprod[i]= input(Violeta+"-").upper()
                while vecprod[i]!="SOJA" and vecprod[i]!="MAIZ" and vecprod[i]!="TRIGO" and vecprod[i]!="GIRASOL" and vecprod[i]!="CEBADA" and vecprod[i]!="":
                    print(Rojo+"Opcion erronea / no disponible")
                    vecprod[i]= input(Cyan+"Seleccione nuevamente: -").upper()
                    print(Reset+"")
            if (vecprod[0] and vecprod[1])!="" or (vecprod[0] and vecprod[2])!="" or (vecprod[1] and vecprod[2])!="":
                while vecprod[0]==vecprod[1] or vecprod[0]==vecprod[2] or vecprod[1]==vecprod[2]:
                    if vecprod[0]==vecprod[1]:
                        print(Rojo+"Productos repetidos, seleccionar otro")
                        print(Reset+"")
                        vecprod[1]=input(Violeta+"-").upper()
                        print(Reset+"")
                        while vecprod[1]!="SOJA" and vecprod[1]!="MAIZ" and vecprod[1]!="TRIGO" and vecprod[1]!="GIRASOL" and vecprod[1]!="CEBADA" and vecprod[1]!="":
                            print(Rojo+"Opcion erronea / No disponible\n")
                            print(Reset+Cyan+"Selecciona una opcion nuevamente:")
                            vecprod[1]=input(Violeta+"-").upper()
                            print(Reset+"")
                    if vecprod[0]==vecprod[2]:
                        print(Rojo+"Productos repetidos, seleccionar otro")
                        print(Reset+"")
                        vecprod[2]=input(Violeta+"-").upper()
                        print(Reset+"")
                        while vecprod[2]!="SOJA" and vecprod[2]!="MAIZ" and vecprod[2]!="TRIGO" and vecprod[2]!="GIRASOL" and vecprod[2]!="CEBADA" and vecprod[2]!="":
                            print(Rojo+"Opcion erronea / No disponible\n")
                            print(Reset+Cyan+"Selecciona una opcion nuevamente:")
                            vecprod[1]=input(Violeta+"-").upper()
                            print(Reset+"")
                    if vecprod[1]==vecprod[2]:
                        print(Rojo+"Productos repetidos, seleccionar otro")
                        print(Reset+"")
                        vecprod[2]=input(Violeta+"-").upper()
                        print(Reset+"")
                        while vecprod[2]!="SOJA" and vecprod[2]!="MAIZ" and vecprod[2]!="TRIGO" and vecprod[2]!="GIRASOL" and vecprod[2]!="CEBADA" and vecprod[2]!="":
                            print(Rojo+"Opcion erronea / No disponible\n")
                            print(Reset+Cyan+"Selecciona una opcion nuevamente:")
                            print(Reset+"")
                            vecprod[1]=input(Violeta+"-").upper()
                            print(Reset+"")
            ingresorecepcion=True
            ingresocupos=True
            clearconsole()
        elif(op3=="B"):
            clearconsole()
            print(Cyan+">>> BAJA <<<\n")
            print(Azul+"Los productos dados de alta son:\n")
            for i in range (0,3):
                print(f"-{i+1} {vecprod[i]}\n")
            print(Reset+Cyan+"¿Desea dar de baja un producto?  S/N")
            dec=input(Violeta+"-").upper()
            print(Reset+"")
            while dec!="S" and dec!="SI" and dec!="N" and dec!="NO":
                clearconsole()
                print(Rojo+"Opcion invalida! Por favor ingrese una opcion nuevamente: S/N\n")
                dec=input(Violeta+"-").upper()
                clearconsole()
            if dec=="S" or dec=="SI":
                print(Cyan+"Que producto desea dar de baja? 1/2/3")
                dec2=int(input(Violeta+"-"))
                print(Reset+"")
                while dec2<1 or dec2>3:
                    print(Rojo+"Producto no existente, por favor seleccione un producto nuevamente... 1/2/3")
                    dec2=int(input(Violeta+"-"))
                    print(Reset+"")
                vecprod[dec2-1]=""
                clearconsole()
                print(Cyan+ f"Producto {dec2} dado de baja con exito\n")
        elif(op3=="C"):
            clearconsole()
            print(Cyan+">>> CONSULTA <<<\n")
            print(Azul+"El listado de productos es:\n")
            for i in range (0,3):
                print(Azul+ f"-{i+1} {vecprod[i]}\n")
                print(Reset+"")
            print("Presione cualquier tecla para continuar...\n")
            nisman=input("")
            clearconsole()
        elif(op3=="M"):
            clearconsole()
            if modificacion==True:
                print(Cyan+">>> MODIFICACIÓN <<<")
                print(Azul+ f"Los productos dados de alta son:\n")
                for i in range (0,3):
                    print(f"-{i+1} {vecprod[i]}\n")
                    print(Reset+"")
                print(Amarillo+"¿Desea modificar un producto?  S/N")
                dec3=input(Violeta+"-").upper()
                print(Reset+"")
                while dec3!="S" and dec3!="SI" and dec3!="N" and dec3!="NO":
                    print(Rojo+"Opcion invalida! Por favor ingrese una opcion nuevamente: S/N\n")
                    dec3=input(Violeta+"-").upper()
                    print(Reset+"")
                if dec3=="S" or dec3=="SI":
                    print(Amarillo+"Que producto desea modificar? 1/2/3")
                    dec4=int(input(Violeta+"-"))
                    print(Reset+"")
                    while dec4<1 and dec4>3:
                        print(Rojo+"Producto no existente,", Amarillo+" por favor seleccione un producto nuevamente... 1/2/3")
                        dec4=int(input(Violeta+"-"))
                        print(Reset+"")
                    print(Amarillo+"Ingrese el nuevo producto")
                    vecprod[dec4-1]= input(Violeta+"-").upper()
                    print(Reset+"")
                    while vecprod[dec4-1]!="SOJA" and vecprod[dec4-1]!="MAIZ" and vecprod[dec4-1]!="TRIGO" and vecprod[dec4-1]!="GIRASOL" and vecprod[dec4-1]!="CEBADA" and vecprod[dec4-1]!="":
                        print(Rojo+"Opcion erronea / no disponible")
                        vecprod[dec4-1]= input(Cyan+"Seleccione nuevamente: -").upper()
                        print(Reset+"")
                    if (vecprod[0] and vecprod[1])!="" or (vecprod[0] and vecprod[2])!="" or (vecprod[1] and vecprod[2])!="":
                        while vecprod[0]==vecprod[1] or vecprod[0]==vecprod[2] or vecprod[1]==vecprod[2]:
                            if vecprod[0]==vecprod[1]:
                                print(Rojo+"Productos repetidos, seleccionar otro")
                                vecprod[1]=input(Violeta+"-").upper()
                                print(Reset+"")
                            if vecprod[0]==vecprod[2]:
                                print(Rojo+"Productos repetidos, seleccionar otro")
                                vecprod[2]=input(Violeta+"-").upper()
                                print(Reset+"")
                            if vecprod[1]==vecprod[2]:
                                print(Rojo+"Productos repetidos, seleccionar otro")
                                vecprod[2]=input(Violeta+"-").upper()
                                print(Reset+"")
                        clearconsole()
                        print(Verde+ f"Producto {dec4} modificado con exito\n")
                else: clearconsole()
            else:
                    print(Rojo+"Los productos no pueden ser modificados si ya ha ingresado un camion")
                    nisman=input(Violeta+"Pulse ENTER para continuar...")
                    print(Reset+"")
                    clearconsole()
        else:
            clearconsole()
            print(Rojo+"x ¡¡OPCION INVALIDA!! x\n")
        print(Amarillo+"A. ALTA")
        print("B. BAJA")
        print("C. CONSULTA")
        print("M. MODIFICACIÓN")
        print("V. VOLVER AL MENÚ ANTERIOR\n")
        op3=input(Cyan+"INGRESE UNA OPCIÓN NUEVAMENTE: -").upper()
    clearconsole()

#-----------------------> MÓDULO DE REPORTES <------------------------------------

# variables: op5,opvolver: string; salir: integer;

def REPORTES():
    print(Cyan+">>> BIENVENIDO AL MENU DE REPORTES <<<\n")
    print("¿Desea revisar los últimos datos ingresados? S/N\n")
    op5=input(Violeta+"-").upper()
    print(Reset+"")
    while (op5!="S" and op5!="N"):
        clearconsole()
        print(Rojo+"¡¡OPCION INVALIDA!!")
        print(Cyan+'¿Desea revisar los últimos datos ingresados? S/N\n')
        op5 = input(Violeta+"-").upper()
        print(Reset+"")
    if (op5=="S"):
        clearconsole()
        if (totalCamiones!=0):
            print(Cyan+">>> BIENVENIDO AL MENU DE REPORTES <<<\n")
            print(Azul+ f"Hasta el momento han sido otorgados {cont} cupos. \n")
            print(f"Cantidad total de camiones que llegaron: {totalCamiones}")
            print(f"Cantidad total de camiones de soja: {camionesSoja}")
            print(f"Cantidad total de camiones de maíz: {camionesMaiz}")
            print(f"Cantidad total de camiones de trigo: {camionesTrigo}")
            print(f"Cantidad total de camiones de girasol: {camionesGirasol}")
            print(f"Cantidad total de camiones de cebada: {camionesCebada}")
            print(f"Peso neto total de soja: {netoSoja}")
            print(f"Peso neto total de maiz: {netoMaiz}")
            print(f"Peso neto total de trigo: {netoTrigo}")
            print(f"Peso neto total de girasol: {netoGirasol}")
            print(f"Peso neto total de cebada: {netoCebada}\n")
            PROMEDIOSINDIVIDUALES()
            print(f"Promedio del peso neto de soja por camión: {promedioSoja}Kg")
            print(f"Promedio del peso neto de maiz por camión: {promedioMaiz}Kg")
            print(f"Promedio del peso neto de trigo por camión: {promedioTrigo}Kg")
            print(f"Promedio del peso neto de girasol por camión: {promedioGirasol}Kg")
            print(f"Promedio del peso neto de cebada por camión: {promedioCebada}Kg\n")

            print(f"Patente del camion de maiz que mayor cantidad de maiz descargó: {mayorpat[0]}")
            print(f"Patente del camion de maiz que menor cantidad de maiz descargó: {menorpat[0]}")
            print(f"Patente del camion de soja que mayor cantidad de soja descargó: {mayorpat[1]}")
            print(f"Patente del camion de soja que menor cantidad de soja descargó: {menorpat[1]}")
            print(f"Patente del camion de trigo que mayor cantidad de soja descargó: {mayorpat[2]}")
            print(f"Patente del camion de trigo que menor cantidad de soja descargó: {menorpat[2]}")
            print(f"Patente del camion de girasol que mayor cantidad de soja descargó: {mayorpat[3]}")
            print(f"Patente del camion de girasol que menor cantidad de soja descargó: {menorpat[3]}")
            print(f"Patente del camion de cebada que mayor cantidad de soja descargó: {mayorpat[4]}")
            print(f"Patente del camion de cebada que menor cantidad de soja descargó: {menorpat[4]}\n")

            for t in range (0,7):
                for v in range (t+1,8):
                    if todosNetos[t]<todosNetos[v]:
                        aux=todosNetos[t]
                        todosNetos[t]=todosNetos[v]
                        todosNetos[v]=aux
                        aux2=vpatente[t]
                        vpatente[t]=vpatente[v]
                        vpatente[v]=aux2
                        aux3=ppatente[t]
                        ppatente[t]=ppatente[v]
                        ppatente[v]=aux3
            print("Listado de camiones ordenados por peso descendente:\n")
            for j in range (0,8):
                if todosNetos[j] != 0:
                    print(vpatente[j], ppatente[j], todosNetos[j])
        else:
            print(Rojo+"No hay datos que mostrar...")
    print()
    opvolver=input(Cyan+"* Pulse cualquier tecla para volver al Menú Principal: ")
    print(Reset+"")
    clearconsole()

#------------------> MÓDULO DE RECEPCION <------------------------------------

# variables: totalCamiones,camionesSoja,camionesMaiz: intger;
#            netos,netom,netoSoja,netoMaiz,promedioSoja,promedioMaiz,mayor,menor,brutos,brutom,taras,taram: float;
#            opconteo,op4,producto,patentes,patentem: string;

def RECEPCION():
    global salir, totalCamiones, camionesSoja, camionesMaiz, camionesGirasol, camionesTrigo, camionesCebada, mayor, menor, patente, vecprod, ingresorecepcion, modificacion
    clearconsole()
    if ingresorecepcion==True:
        print(Cyan+"BIENVENIDO AL MENÚ RECEPCION\n")
        print("¿Desea ingresar un producto? S/N\n")
        op4=input(Violeta+"").upper()
        print(Reset+"")
        clearconsole()
        while (op4!="S" and op4!="N"):
            clearconsole()
            print(Rojo+"¡¡OPCION INVALIDA!!")
            print(Cyan+'¿Desea ingresar un producto?  S / N\n')
            op4 = input(Violeta+"").upper()
            print(Reset+"")
            clearconsole()
        while op4!="N":
            print(Cyan+"Ingrese la patente del camion:")
            patente=input(Violeta+"-").upper()
            print(Reset+"")
            clearconsole()
            while len(patente)<6 or len(patente)>7:
                print(Rojo+"Patente invalida, ingresar otra patente: \n")
                patente=input(Violeta+"-").upper()
                print(Reset+"")
                clearconsole()
            x=0
            while x<8 and vpatente[x]!=patente:
                x+=1
            if x==8:
                print(Rojo+"No se ha encontrado la patente\n")
                print(Cyan+'¿Desea ingresar un producto?  S / N\n')
                op4 = input(Violeta+"-").upper()
                clearconsole()
            else:
                if vEstado[x]=="P":
                    vEstado[x]="E"
                    print(Cyan+"Ingrese el nombre del producto, Soja, Maiz, Trigo, Girasol, Cebada")
                    producto=input(Violeta+"-").upper()
                    print(Reset+"")
                    clearconsole()
                    while BUSCARPRO(vecprod, producto)!=True:
                        print(Rojo+"El producto no esta disponible, por favor seleccionar otro.")
                        producto=input(Violeta+"-").upper()
                        print(Reset+"")
                        clearconsole()
                    if producto=="SOJA":
                        ppatente[x]=producto
                        camionesSoja+=1
                    elif producto=="MAIZ":
                        ppatente[x]=producto
                        camionesMaiz+=1
                    elif producto=="GIRASOL":
                        ppatente[x]=producto
                        camionesGirasol+=1
                    elif producto=="TRIGO":
                        ppatente[x]=producto
                        camionesTrigo+=1
                    elif producto=="CEBADA":
                        ppatente[x]=producto
                        camionesCebada+=1
                    totalCamiones+=1
                    modificacion=False
                    print(Cyan+"¿Desea ingresar otro producto?")
                    op4=input(Violeta+"-").upper()
                    while (op4!="S" and op4!="N"):
                        clearconsole()
                        print(Rojo+"¡¡OPCION INVALIDA!!")
                        print(Cyan+'¿Desea ingresar otro producto?  S / N\n')
                        op4 = input(Violeta+"-").upper()
                else:
                    print(Cyan+"El camion ya fue atendido.")
                    nisman=input("Pulse ENTER para continuar...")
                    print(Reset+"")
                    clearconsole()
    else:
        print(Rojo+"No hay productos dados de alta")
        nisman=input(Cyan+"Pulse enter para continuar")
        print(Reset+"")

#-----------------------> PESO BRUTO <---------------------------------------
def PESOBRUTO():
    global entradatara, pbruto
    decisionbruta=input(Cyan+"¿Desea ingresar un peso bruto? :").upper()
    print(Reset+"")
    while decisionbruta!="S" and decisionbruta!="N" and decisionbruta!="SI" and decisionbruta!="NO":
        print(Rojo+"Opcion ivalida, por favor seleccione SI o NO.")
        decisionbruta=input(Violeta+"-").upper()
    while decisionbruta=="S" or decisionbruta=="SI":
        print(Cyan+"Ingresar patente:\n")
        patentebruta=input(Violeta+"-").upper()
        while len(patentebruta)<6 or len(patentebruta)>7:
            print(Rojo+"La patente ingresada no es valida, por favor ingrese otra.\n")
            patentebruta=input(Violeta+"-").upper()
            print(Reset+"")
        y=0
        while y<8 and vpatente[y]!=patentebruta:
            y+=1
        if y==8:
            print(Rojo+"La patente no se encuentra registrada en el sistema.")
        else:
            if vEstado[y]=="E":
                if arraybruto[y]==0:
                    pbruto=int(input("Ingrese el peso bruto:-"))
                    while pbruto<1:
                        print(Rojo+"Peso bruto negativo, por favor agregue un peso bruto positivo\n")
                        pbruto=int(input(Violeta+"-"))
                        print(Reset+"")
                    arraybruto[y]=pbruto
                    entradatara=True
                else:
                    print(Rojo+"A esta patente ya se le fue asignado un peso bruto.")
                    print(Reset+"")
            else:
                print(Rojo+'El estado de esta patente no es "En Proceso"')
                print(Reset+"")
        decisionbruta=input(Cyan+"¿Desea ingresar un peso bruto? :").upper()
        print(Reset+"")
        while decisionbruta!="S" and decisionbruta!="N" and decisionbruta!="SI" and decisionbruta!="NO":
            print(Rojo+"Opcion ivalida, por favor seleccione SI o NO.")
            decisionbruta=input(Violeta+"-").upper()
        clearconsole()

#-------------------------> TARA <-------------------------------------------

def TARAdo():
    global netoMaiz, netoSoja, netoCebada, netoGirasol, netoTrigo, mayores, entradatara

    if entradatara==True:
        decisiontarada=input(Cyan+"¿Desea ingresar una tara?:-").upper()
        print(Reset+"")
        while decisiontarada!="S" and decisiontarada!="N" and decisiontarada!="SI" and decisiontarada!="NO":
            print(Rojo+"Opcion ivalida, por favor seleccione SI o NO.")
            decisiontarada=input(Violeta+"-").upper()
            print(Reset+"")
        while decisiontarada=="S" or decisiontarada=="SI":
            print(Cyan+"Ingresar patente:\n")
            patentetarada=input(Violeta+"-").upper()
            print(Reset+"")
            while len(patentetarada)<6 or len(patentetarada)>7:
                print(Rojo+"La patente ingresada no es valida, por favor ingrese otra.\n")
                patentetarada=input(Violeta+"-").upper()
                print(Reset+"")
            z=0
            while z<8 and vpatente[z]!=patentetarada:
                z+=1
            if z==8:
                print(Cyan+"La patente no se encuentra registrada en el sistema.")
                print(Reset+"")
            else:
                if vEstado[z]=="E":
                    if arraybruto[z]!=0:
                        if arraytarado[z]!=0:
                            print(Rojo+"Esta patente ya tiene una tara asignada.")
                            print(Reset+"")
                        else:
                            tara=int(input(Cyan+"Ingrese la tara:- "))
                            print(Reset+"")
                            while tara<1 or tara>pbruto:
                                print(Rojo+"Tara negativa o mayor al peso bruto, por favor ingrese otra.\n")
                                tara=int(input(Violeta+"-"))
                                print(Reset+"")
                            arraytarado[z]=tara
                            todosNetos[z]=arraybruto[z]-tara
                            if ppatente[z]=="MAIZ":
                                netoMaiz+=arraybruto[z]-tara
                                if arraybruto[z]-tara>mayores[0]:
                                    mayores[0]=netoMaiz
                                    mayorpat[0]=patentetarada
                                if arraybruto[z]<menores[0]:
                                    menores[0]=netoMaiz
                                    menorpat[0]=patentetarada
                            if ppatente[z]=="SOJA":
                                netoSoja+=arraybruto[z]-tara
                                if arraybruto[z]-tara>mayores[1]:
                                    mayores[1]=netoSoja
                                    mayorpat[1]=patentetarada
                                if arraybruto[z]<menores[1]:
                                    menores[1]=netoSoja
                                    menorpat[1]=patentetarada
                            if ppatente[z]=="TRIGO":
                                netoTrigo+=arraybruto[z]-tara
                                if arraybruto[z]-tara>mayores[2]:
                                    mayores[2]=netoTrigo
                                    mayorpat[2]=patentetarada
                                if arraybruto[z]<menores[2]:
                                    menores[2]=netoMaiz
                                    menorpat[2]=patentetarada
                            if ppatente[z]=="GIRASOL":
                                netoGirasol+=arraybruto[z]-tara
                                if arraybruto[z]-tara>mayores[3]:
                                    mayores[3]=netoGirasol
                                    mayorpat[3]=patentetarada
                                if arraybruto[z]<menores[3]:
                                    menores[3]=netoGirasol
                                    menorpat[3]=patentetarada
                            if ppatente[z]=="CEBADA":
                                netoCebada+=arraybruto[z]-tara
                                if arraybruto[z]-tara>mayores[4]:
                                    mayores[4]=netoCebada
                                    mayorpat[4]=patentetarada
                                if arraybruto[z]<menores[4]:
                                    menores[4]=netoCebada
                                    menorpat[4]=patentetarada
                    else:
                        print(Rojo+"A esta patente aún no se le ha asignado un peso bruto.")
                        print(Reset+"")
                else:
                    print(Rojo+'El estado de esta patente no es "En Proceso"')
            decisiontarada=input(Cyan+"¿Desea ingresar una tara?:-").upper()
            print(Reset+"")
            while decisiontarada!="S" and decisiontarada!="N" and decisiontarada!="SI" and decisiontarada!="NO":
                print(Rojo+"Opcion ivalida, por favor seleccione SI o NO.")
                decisiontarada=input(Violeta+"-").upper()
                print(Reset+"")
    else:
        print(Rojo+"Antes de ingresar la tara debe ingresar el peso bruto")
        print(Cyan+"Pulse ENTER para continuar...")
        nisman=input(Violeta+"-")
        print(Reset+"")
        clearconsole()

#--------------------------------------------------------------------------
def BUSCARPRO(vecprod, producto):
    for i in range(0,3):
        if vecprod[i]==producto and vecprod[i] != "":
            return True

def BUSCARPAT(npatente, vpatente):
    for i in range(0,8):
        if vpatente[i]==npatente:
            return True


#-----------------> MÓDULO DEL  PROGRAMA PRINCIPAL <------------------

# variables: op: integer;

def MENUP():
    INARRAYS()
    INVAR()
    global salir, cont
    cont=0
    salir=0
    clearconsole()
    print(Cyan+">>> BIENVENIDO AL PROGRAMA PRINCIPAL <<<\n")
    print(Reset+Amarillo+"1 - ADMINISTRACIONES")
    print("2 - ENTREGAS DE CUPOS")
    print("3 - RECEPCION")
    print("4 - REGISTRAR CALIDAD")
    print("5 - REGISTRAR PESO BRUTO")
    print("6 - REGISTRAR DESCARGA")
    print("7 - REGISTRAR TARA")
    print("8 - REPORTES")
    print("0 - FIN DEL PROGRAMA\n")
    op=input(Cyan+"INGRESE UNA OPCIÓN: ")
    print(Reset+"")
    while (op != "0"):
        if (op == "1"):
            #Administraciones
            MODULOADMINISTRACIONES()
        elif (op == "2"):
            clearconsole()
            #Cupos
            ENTREGADECUPOS()
        elif(op == "3"):
            RECEPCION()
        elif(op == "4"):
            clearconsole()
            print(Cyan+'* REGISTRAR CALIDAD *')
            print(Reset+Rojo+"Esta funcionalidad está en construccion...")
            print(Reset+"")
        elif(op == "5"):
            clearconsole()
            #Peso bruto
            PESOBRUTO()
        elif(op == "6"):
            clearconsole()
            print('* REGISTRAR DESCARGA *')
            print(Reset+Rojo+"Esta funcionalidad está en construccion...")
            print(Reset+"")
        elif(op == "7"):
            clearconsole()
            #Registrar tara
            TARAdo()
        elif(op == "8"):
            clearconsole()
            REPORTES()
        else:
            clearconsole()
            print(Rojo+"x ¡¡OPCIÓN INGRESADA INVÁLIDA!! x")
            print(Reset+"")
        print(Cyan+">>> BIENVENIDO AL PROGRAMA PRINCIPAL <<<\n")
        print(Reset+Amarillo+"1 - ADMINISTRACIONES")
        print("2 - ENTREGAS DE CUPOS")
        print("3 - RECEPCIÓN")
        print("4 - REGISTRAR CALIDAD")
        print("5 - REGISTRAR PESO BRUTO")
        print("6 - REGISTRAR DESCARGA")
        print("7 - REGISTRAR TARA")
        print("8 - REPORTES")
        print("0 - FIN DEL PROGRAMA\n")
        op=input(Cyan+"INGRESE UNA OPCIÓN NUEVAMENTE: \n")
    print(Reset+Violeta+"¡Gracias por su visita, hasta pronto!")
    print()


#---------------------------> ENTREGA DE CUPOS <--------------------------
def ENTREGADECUPOS():
    global cont, npatente, ingresocupos
    print(Cyan+"BIENVENIDO A ENTREGA DE CUPOS\n")
    print("¿Desea pedir un cupo? S/N\n")
    if ingresocupos==True:
        opcion=input(Violeta+"-").upper()
        print(Reset+"")
        clearconsole()
        while opcion!="N" and opcion!="S" and opcion!="SI" and opcion!="NO":
            print(Rojo+"x ¡¡OPCIÓN INGRESADA INVÁLIDA!! x")
            opcion=input(Violeta+"-").upper()
            print(Reset+"")
            clearconsole()
        while (opcion!="N") and (opcion!="NO") and cont<=7:
            npatente=input(Cyan+"Ingrese el número de patente:-").upper()
            print(Reset+"")
            while len(npatente)<6 or len(npatente)>7:
                npatente=input(Rojo+"Cantidad de Caracteres incorrecta, ingrese la patente nuevamente:-").upper()
            if BUSCARPAT(npatente, vpatente):
                npatente=input(Rojo+"No se pueden asignar más cupos a esta patente, por favor ingresar otra:-").upper()
                print(Reset+"")
            vpatente[cont]=npatente
            vEstado[cont]="P"
            cont+=1
            clearconsole()
            print(Cyan+"¿Desea pedir otro turno?")
            opcion=input(Violeta+"-").upper()
            print(Reset+"")
            clearconsole()
            while opcion!="N" and opcion!="S" and opcion!="SI" and opcion!="NO":
                print(Rojo+"x ¡¡OPCIÓN INGRESADA INVÁLIDA!! x")
                opcion=input(Violeta+"-").upper()
                print(Reset+"")
        if (opcion=="SI") or (opcion=="S") and (cont>7):
            print(Cyan+"Lo sentimos, no hay más cupos disponibles")
            print("Presione ENTER para volver al menu principal")
            nisman=input("")
            print(Reset+"")
            clearconsole()
    else:
        print("Los productos deben estar dados de alta para poder entregar cupos")


#------------------------> INICIALIZACION <-------------------------------
def INVAR():
    global totalCamiones, camionesSoja, camionesMaiz, camionesTrigo, camionesGirasol, camionesCebada, netoSoja, netoMaiz, patenteMayor, patenteMenor, netoSoja, netoMaiz, netoTrigo, netoGirasol, netoCebada, promedioMaiz, promedioSoja, promedioTrigo, promedioCebada, promedioGirasol, mayor, menor, pbruto, entradatara, ingresorecepcion, modificacion, ingresocupos
    ingresocupos=False
    modificacion=True
    ingresorecepcion=False
    entradatara=False
    pbruto=0
    patenteMayor=0
    patenteMenor=0
    netoSoja=0
    netoMaiz=0
    netoTrigo=0
    netoGirasol=0
    netoCebada=0
    promedioMaiz=0
    promedioSoja=0
    promedioTrigo=0
    promedioGirasol=0
    promedioCebada=0
    totalCamiones=0
    camionesSoja=0
    camionesMaiz=0
    camionesGirasol=0
    camionesTrigo=0
    camionesCebada=0
    mayor=0
    menor=0

#------------------------> INICIALIZACION DE ARRAYS <---------------------
def INARRAYS():
    global vpatente, vecprod, vEstado, arraybruto, arraytarado, todosNetos, ppatente, mayores, menores, mayorpat, menorpat
    ppatente=[""]*8
    todosNetos=[0]*8
    arraybruto=[0]*8
    arraytarado=[0]*8
    vpatente=[""]*8
    vEstado=[""]*8
    vecprod=[""]*3
    mayores=[0]*5
    menores=[9999999999999]*5
    mayorpat=[""]*5
    menorpat=[""]*5
#------------------------> M E N U <-------------------------------------
MENUP()