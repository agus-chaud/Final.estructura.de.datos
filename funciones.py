from claseRouter import *
from claseMunicipio import *
from claseConexion import *
import csv
import traceback
from random import randint

def mostrarmenu():
    print('''
        1. Cargar nuevo  municipio
        2. Cargar nuevo punto de acceso
        3. Dar de baja un punto de acceso
        4. Ver N° de conexiones activas por provincia dada
        5. Ver N° de conexiones activas por departamento dado
        6. Ver N° de conexiones activas por municipio dado
        7. Agregar conexion
        8. Quitar conexion
        9. Cerrar y guardar cambios''')
    opcion=int(input("Elija de estas opciones  que accion desea ejecutar: "))
    return opcion

def agregarconex():
    try:
            dir_ip=randint(-5000,5000) #esta validacion debe ser por router
            dir_mac=int(input("Ingrese la direccion Mac de su computadora (numero entero)"))
            while str(dir_mac) in Conexion.macsactivas: #direccion mac ya utilizada
                print("Esa direccion Mac ya esta usada, ingresa otra")
                dir_mac=int(input("Ingrese la direccion Mac de su computadora (numero entero)"))   
            routerID=str(input('Ingrese el id del router al que desea conectarse: ')) 
            routerID=routerID.upper()
            #validar q exista router id
            while routerID not in Router.diccionarioRouter:
               print ("Ese identificador no pertenece a ningun router, ingresa otro") 
               routerID=str(input('Ingrese el id del router al que desea conectarse: ')) 
               routerID=routerID.upper()
            #creo el objeto router porque agregarConexion es un metodo de instancia
            objetorouter=Router.diccionarioRouter[routerID]
            #chequeo q en ese router haya menos de 20 conexiones
            if len(objetorouter.conexiones) < 20:
                conect=Conexion(dir_ip,dir_mac,routerID) #creo el objeto conexion
                objetorouter.agregarConexion(conect)
            else:
                print("Ese router ya no acepta mas conexiones")
    except:
            print("Ingresaste mal los datos")
            traceback.print_exc()

def nuevorouter():
    try:
        id=int(input('Ingrese el id del router(ej:598)')) 
        identificador=str(input('Ingrese el identificador del router(ej:TUC100-01): '))
        identificador=identificador.upper()
        while identificador in Router.diccionarioRouter:
            print ("Ese identificador ya fue usado, ingresa otro") 
            identificador=str(input('Ingrese el identificador del router(ej:TUC100-01): '))
            identificador=identificador.upper()
        #listar ids provincias
        listarprovs()
        provinciaID=str(input('Ingrese el id de la provincia del router(ej:AR-T): '))
        provinciaID=provinciaID.upper()
        prov = Provincia.diccionarioProv[provinciaID]
        print("El id que ingreso pertenece a la provincia ",prov.provincia)
        while provinciaID not in Provincia.diccionarioProv:
            print ("Ese identificador no pertence a ninguna provincia, ingresa otro") 
            provinciaID=str(input('Ingrese el id de la provincia del router(ej:AR-T): '))
            provinciaID=provinciaID.upper()
        decision=str(input("Desea ver los departamentos asociados a esa provincia? (si/no)"))    
        if decision.lower()=="si":
            listardeps(prov)            
        else:
            pass  
        departamentoID=str(input('Ingrese el id del departamento del router(ej:1648): '))
        municipioID=str(input('Ingrese el id del municipio del router(ej:TUC100): '))
        
        ubicacion=str(input('Ingrese la ubicacion del router(ej:Dependencia Municipal): '))
        latitud=float(input('Ingrese la latitud del router(ej:-35): '))
        longitud=float(input('Ingrese la longitud del router(ej:-65): '))

        nuevorouter=Router(id,identificador,ubicacion,latitud,longitud,municipioID,provinciaID,departamentoID)
        print("Su router se ha creado y guardado exitosamente")
        
    except:
        print("Error: los campos: id , latitud y longitud deben ser datos numericos")       
def listarprovs():
    ## recorrer diccionario imprimiendo provincias
    for clave, valor in Provincia.diccionarioProv.items():
        #en valor tengo los objetos provincia
        print(clave,":",valor)   
 
def listardeps(prov):
    ## recorrer diccionario imprimiendo departamentos de una provincia
    for clave, valor in prov.diccionarioDptos.items():
            #en valor tengo los objetos departamento
            print(clave,":",valor) 
  
def listarmuns(dep):
    ## recorrer diccionario imprimiendo municipios de un departamento
    for clave, valor in dep.diccionarioMunicipios.items():
            #en valor tengo los objetos departamento
            print(clave,":",valor)   
        
def nuevomunicipio(setprovincias):
    listarprovs()
    prov_id=str(input(" Ingrese el id de la provincia del nuevo municipio(ej:AR-T): "))
    prov_id= prov_id.upper()
    if prov_id not in Provincia.diccionarioProv:
            print("Ese id es invalido, ingrese uno correcto")
            prov_id=str(input(" Ingrese el id de la provincia (ej:AR-T): "))
            prov_id= prov_id.upper()
    prov = Provincia.diccionarioProv[prov_id]
    print("El id que ingreso pertenece a la provincia ",prov.provincia)
    decision=str(input("Desea ver los departamentos asociados a esa provincia? (si/no)"))
    if decision.lower()=="si":
        ## recorrer diccionario imprimiendo departamentos
        for clave, valor in prov.diccionarioDptos.items():
            #en valor tengo los objetos departamento
            print(clave,":",valor)
    else:
        pass
    
    id_departamento=str(input(" Ingrese el id del departamento del nuevo municipio(ej:1648): "))
    while id_departamento not in prov.diccionarioDptos.keys():
            print("Ese id no pertenece a un departamento, ingrese uno correcto")
            id_departamento=int(input(" Ingrese el id del departamento (ej:1648): "))
    dpto = prov.diccionarioDptos[id_departamento]
    print("El id que ingreso pertenece al departamento",dpto.departamento)
    decision=str(input("Desea ver los municipios asociados a ese departamento ? (si/no)"))
    if decision.lower()=="si":
        ## recorrer diccionario imprimiendo municipios
        for clave, valor in dpto.diccionarioMunicipios.items():
            #en valor tengo los objetos municipios
            print(clave,":",valor)
    else:
        pass
    municipio=str(input(" Ingrese el nombre del nuevo municipio: "))
    mun_id=str(input(" Ingrese el id del municipio (ej:TUC100): "))
    mun_id=mun_id.upper()
    while mun_id in dpto.diccionarioMunicipios:
        print('Ese id de municipio ya fue usado, ingrese otro')
        mun_id=str(input(" Ingrese el id del municipio (ej:TUC100): "))
        mun_id=mun_id.upper()

    nuevomun=Municipio(prov_id,prov.provincia,id_departamento,dpto.departamento, mun_id,municipio)
    print("Su municipio se ha creado y guardado exitosamente")
 
def eliminar_router():
    try:
        identificador=str(input('Ingrese el identificador del router q desea eliminar(ej:TUC100-01): '))
        identificador=identificador.upper()
        if identificador not in Router.diccionarioRouter:
            print("El identificador ingresado no pertence a ningun router existente")  
            return
        else:
            del Router.diccionarioRouter[identificador]
            print("Su router se ha eliminado exitosamente")
        
    except ValueError as e:
        print("Su error fue {}, el id , la latitud y longitud deben ser datos numericos".format(e))       

def buscarconex_prov():
    #condicion de que haya conecciones activas, sino ni busco
    if(len(Conexion.macsactivas)>0):
        listarprovs()
        inputprovinciaID=str(input('Ingrese el id de la provincia de la q desea ver las conexiones (ej:AR-T): '))
        inputprovinciaID=inputprovinciaID.upper()
        contadorconexprov=0
        for clave, valor in Router.diccionarioRouter.items():
            #en valor tengo los objetos router
            if valor.provinciaID ==  inputprovinciaID: 
                for i in range(len(valor.conexiones)):
                    contadorconexprov+=1
        if contadorconexprov>0:
            print("Se encontraron {} conexiones abiertas en esa provincia".format(contadorconexprov)) 
        else: 
            print("No se encontraron conexiones abiertas en esa provincia")
    else:
        print("No se encontraron conexiones abiertas en esa provincia")  
 
def buscarconex_dep():
    #condicion de que haya conecciones activas, sino ni busco
    if(len(Conexion.macsactivas)>0):
        listarprovs()
        inputprovinciaID=str(input('Ingrese el id de la provincia al que pertenece el departamento (ej:AR-T): '))
        inputprovinciaID=inputprovinciaID.upper()
        prov = Provincia.diccionarioProv[inputprovinciaID]
        listardeps(prov)
        inputdepartamentoID=str(input('Ingrese el id del departamento del q desea ver las conexiones(ej:1648): '))
        contadorconexdep=0
        for clave, valor in Router.diccionarioRouter.items():
            if valor.provinciaID ==  inputprovinciaID:
               if valor.departamentoID==inputdepartamentoID:
                    for i in range(len(valor.conexiones)):
                        contadorconexdep+=1
        if contadorconexdep>0:
            print("Se encontraron {} conexiones abiertas en ese departamento".format(contadorconexdep)) 
        else: 
            print("No se encontraron conexiones abiertas en ese departamento")                
    else:
        print("No se encontraron conexiones abiertas en ese departamento")
        
def buscarconex_mun():
    #condicion de que haya conecciones activas, sino ni busco
    if(len(Conexion.macsactivas)>0):
        listarprovs()
        inputprovinciaID=str(input('Ingrese el id de la provincia al que pertenece el departamento (ej:AR-T): '))
        inputprovinciaID=inputprovinciaID.upper()
        prov = Provincia.diccionarioProv[inputprovinciaID]
        listardeps(prov)
        inputdepartamentoID=str(input('Ingrese el id del departamento al que pertenece el municipio(ej:1648): '))
        dpto = prov.diccionarioDptos[inputdepartamentoID]
        listarmuns(dpto)
        inputmunicipioID=str(input('Ingrese el id del municipio del q desea ver las conexiones(ej:): '))
        inputmunicipioID=inputmunicipioID.upper()
        contadorconexmun=0
        for clave, valor in Router.diccionarioRouter.items():
            if valor.provinciaID ==  inputprovinciaID:
               if valor.departamentoID==inputdepartamentoID:
                    if valor.municipioID==inputmunicipioID:
                        for i in range(len(valor.conexiones)):
                            contadorconexmun+=1
        if contadorconexmun>0:
            print("Se encontraron {} conexiones abiertas en ese municipio".format(contadorconexmun)) 
        else: 
            print("No se encontraron conexiones abiertas en ese municipio") 
    else:
        print("No se encontraron conexiones abiertas en ese municipio")           
        
def cargarProvinciasyDptos(pathMunicipios="C:/Agus/ITBA/3er cuatri/Estructura de datos y programacion/AAA_final_febrero_agustin_chaud/municipios.csv"):
    with open(pathMunicipios, encoding= 'unicode_escape') as csvFile:
        reader=csv.DictReader(csvFile, delimiter=';')
        i=0
        setprovincias=set()
        for linea in reader:
            try:
                i+=1
                #Se crea el objeto Provincia
                Provincia(linea['provincia_id'], linea['provincia'])
                setprovincias.add(linea['provincia'])
                
                #Se crea el objeto Departamento
                Departamento(linea['provincia_id'], linea['provincia'],linea['id_departamento'], linea['departamento'])

                #Se crea el objeto Municipio
                Municipio(linea['provincia_id'], linea['provincia'], linea['id_departamento'], linea['departamento'], linea['ï»¿municipio_id'], linea['municipio'])
            except:
                print('Linea {} no pudo ser cargada correctamente'.format(i))
                traceback.print_exc()
        return setprovincias  
    
def cargarRouters(pathRouters="C:/Agus/ITBA/3er cuatri/Estructura de datos y programacion/AAA_final_febrero_agustin_chaud/routers.csv"):
    #Lectura del csv routers
    with open(pathRouters, encoding='unicode-escape') as csvFile:
        reader=csv.DictReader(csvFile, delimiter=';')
        i=0
        for linea in reader:
            try:
                i+=1
                if linea['provincia_id'] not in Provincia.diccionarioProv:
                    raise Exception("Router no creado --> Provincia no registrada")
                
                prov = Provincia.diccionarioProv[linea['provincia_id']]
                if linea['id_departamento'] not in prov.diccionarioDptos:
                    raise Exception("Router no creado --> Departamento no registrado")
                
                if linea['latitud'] != "0" and linea['longitud'] != "0":
                    linea['latitud'] = int(linea['latitud'].replace('.',''))
                    linea['longitud'] = int(linea['longitud'].replace('.', ''))

                if linea['identificador'] not in Router.diccionarioRouter:
                    Router(linea['ï»¿id'], linea['identificador'],linea['ubicacion'],linea['latitud'],linea['longitud'],
                        linea['municipio_id'], linea['provincia_id'], linea['id_departamento'])
                else:
                    print('Router {} ya fue cargado previamente'.format(linea['ï»¿id']))
            except Exception as e:
                print(e)
                print('Linea {} no pudo ser cargada correctamente'.format(i))
                traceback.print_exc()
def cargarConexiones(pathconexiones="C:/Agus/ITBA/3er cuatri/Estructura de datos y programacion/AAA_final_febrero_agustin_chaud/conexiones.csv"):
    #Lectura del csv conexiones
    with open(pathconexiones, encoding='unicode-escape') as csvFile:
        reader=csv.DictReader(csvFile, delimiter=';')
        i=0
        for linea in reader:
            try:
                i+=1
                #creo el objeto router porque agregarConexion es un metodo de instancia
                objetorouter=Router.diccionarioRouter[linea['routerID']]
                #chequeo q en ese router haya menos de 20 conexiones
                if len(objetorouter.conexiones) < 20:
                    conect=Conexion(linea['direccionIP'],linea['direccionMAC'],linea['routerID']) #creo el objeto conexion
                    objetorouter.agregarConexion(conect)
                else:
                    print("Ese router ya no acepta mas conexiones")
           
            except Exception as e:
                print(e)

def actualizarArchivoRouters(pathRouter="C:/Agus/ITBA/3er cuatri/Estructura de datos y programacion/AAA_final_febrero_agustin_chaud/routers.csv"):
    with open(pathRouter, "w") as archivo:
        writer = csv.writer(archivo, delimiter=';',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['ï»¿id','identificador','ubicacion','latitud','longitud','municipio_id','provincia_id','id_departamento'])
        for routerId in Router.diccionarioRouter:
            router = Router.diccionarioRouter[routerId]
            writer.writerow([router.id, router.identificador, router.ubicacion, router.latitud, router.longitud, router.municipioID, router.provinciaID, router.departamentoID])
    print("Archivo de routers actualizado")

def actualizarArchivoMunic(pathMuni="C:/Agus/ITBA/3er cuatri/Estructura de datos y programacion/AAA_final_febrero_agustin_chaud/municipios.csv"):
    with open(pathMuni, "w") as archivo:
        contadorprov=0
        writer = csv.writer(archivo, delimiter=';',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['ï»¿municipio_id','provincia_id','id_departamento','municipio','provincia','departamento'])
        for provId in Provincia.diccionarioProv:
            contadorprov+=1 
            prov = Provincia.diccionarioProv[provId]
            contadordep=0
            for dptoId in prov.diccionarioDptos:
                contadordep+=1
                dpto = prov.diccionarioDptos[dptoId]
                contadormun=0
                for municipioId in dpto.diccionarioMunicipios:
                    contadormun+=1
                    municipio = dpto.diccionarioMunicipios[municipioId]
                    writer.writerow([municipioId, prov.provinciaID, dpto.departamentoID,municipio, prov.provincia, dpto.departamento])
    print("Archivo de municipios actualizado")
    
def actualizarArchivoConexiones(pathRouter="C:/Agus/ITBA/3er cuatri/Estructura de datos y programacion/AAA_final_febrero_agustin_chaud/conexiones.csv"):
    with open(pathRouter, "w") as archivo:
        writer = csv.writer(archivo, delimiter=';',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['direccionIP','direccionMAC','routerID'])
        for clave, valor in Conexion.diccionarioconexiones.items():
            #en valor tengo los objetos conexion
            writer.writerow([valor.direccionIP,valor.direccionMAC,valor.routerID ])
    print("Archivo de conexiones actualizado")
  
