from funciones import *
from claseConexion import *
from claseRouter import *

#identificador router creado: AGUS8888
# id provincia router creado: AR-X
# id municipio router creado: CBA384
# id departamento router creado: 1401

setprovincias=cargarProvinciasyDptos()
cargarRouters()
cargarConexiones()
seguir=True
while seguir==True:
   opcion=mostrarmenu()
   if opcion==1:
      nuevomunicipio(setprovincias)
     
   elif opcion==2:
      nuevorouter()
      
   elif opcion==3:
      eliminar_router()
   elif opcion==4:
      buscarconex_prov()
           
   elif opcion==5:
      buscarconex_dep()
      
   elif opcion==6:
      buscarconex_mun()
           
   elif opcion==7:
      agregarconex()
   elif opcion==8:
         dir_mac=int(input("Ingrese la direccion Mac de la computadora que desea desconectar (numero entero)"))
         while dir_mac not in Conexion.macsactivas: #direccion mac ya utilizada
            print("Esa direccion Mac no pertence a ninguna conexion, ingresa otra")
            dir_mac=int(input("Ingrese la direccion Mac de la computadora que desea desconectar (numero entero)"))
         routerID=str(input('Ingrese el id del router del que desea conectarse: ')) 
         #creo el objeto router porque quitarConexion es un metodo de instancia
         objetorouter=Router.diccionarioRouter[routerID]
         objetorouter.quitarConexion(dir_mac)
         #borro la direccion mac del set de macs porque se elimino la conexion
         Conexion.macsactivas.remove(dir_mac)
         
   elif opcion==9:
         actualizarArchivoMunic()
         actualizarArchivoRouters()
         actualizarArchivoConexiones()
         seguir=False
         
    