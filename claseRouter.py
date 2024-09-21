from claseMunicipio import *

class Router():
    diccionarioRouter: dict[str,'Router'] = dict()
    
    def __init__(self, id:int, identificador:str, ubicacion, latitud:float, longitud:float, municipioID:str, provinciaID:str, departamentoID: str):
        self.id = id
        self.identificador = identificador
        self.ubicacion = ubicacion
        self.latitud = float(latitud)
        self.longitud = float(longitud)
        self.provinciaID = provinciaID
        self.departamentoID = departamentoID
        self.municipioID = municipioID
        self.conexiones = []
        #agrego el router creado al diccionario de routers
        Router.diccionarioRouter[self.identificador] = self
        # if self.identificador not in Router.diccionarioRouter:
        #     Router.diccionarioRouter[self.identificador] = self        
        # else:
        #     print ("Router no creado --> Ese identificador ya fue usado") 
        #     return 
        
    #Metodo para agregar las conexiones extraidas a los routers (vinculados entre direccionIP-routerID)
    def agregarConexion(self, conect):
        self.conexiones.append(conect)
        print("Conexion agregada exitosamente")
        
    def quitarConexion(self, direccionMAC: int):
        try:
            for i in range(len(self.conexiones)):
                if(self.conexiones[i].direccionMAC==direccionMAC):
                    del self.conexiones[i]
                    print("Conexion eliminada")
        except:
            print("No se preocupe, igual su conexion fue eliminada")
            
            
    def __str__(self):
        return self.identificador