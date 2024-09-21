from claseRouter import Router
class Conexion:
    # Set con todas las macs activas,registradas en los routers
    macsactivas = set()
    diccionarioconexiones:dict[int,'Conexion'] = dict()

    def __init__(self, direccionIP: int, direccionMAC: int, routerID: str):
        self.direccionIP = direccionIP
        self.direccionMAC = direccionMAC
        self.routerID = routerID

        if  self.routerID not in Router.diccionarioRouter:
            print("No pudo crearse la conexion-->El id ingresado no pertence a ningun router")
            return

        # Agrego la conexion al set de macs activas
        if self.direccionMAC not in Conexion.macsactivas:
            Conexion.macsactivas.add(self.direccionMAC)
            Conexion.diccionarioconexiones[direccionIP]=self
    def __str__(self):
        return f"Direccion ip: {self.direccionIP} - Direccion Mac:{self.direccionMAC} - Router id: {self.routerID}"