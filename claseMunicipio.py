class Provincia():
    diccionarioProv: dict[str, 'Provincia'] = dict()

    def __init__(self, provinciaID: str, provincia: str):
        if provinciaID == None:
            #print("No se pudo crear la provincia-->Provincia sin identificador")
            return
        
        if provinciaID in Provincia.diccionarioProv:
            #print("No se pudo crear la provincia-->Provincia ya registrada")
            return
            
        self.provinciaID = provinciaID
        self.provincia = provincia
        self.diccionarioDptos: dict[str, 'Departamento'] = dict()
        ##agrego el objeto creado al dic de provincias
        Provincia.diccionarioProv[self.provinciaID] = self

    def __str__(self):
        return self.provincia
    
class Departamento():
    def __init__(self, provinciaID:str, provincia:str, departamentoID:int, departamento:str):
        self.provinciaID = provinciaID
        self.provincia = provincia        
        self.departamentoID = departamentoID
        self.departamento = departamento
        self.diccionarioMunicipios:dict[str, 'Municipio'] = dict()

        if self.departamentoID == None:
            print("No se pudo crear el departamento--> Departamento sin identificacion")
            return

        if self.provinciaID not in Provincia.diccionarioProv:
            print("No se pudo crear el departamento -->Provincia no registrada")
            return
        
        prov = Provincia.diccionarioProv[self.provinciaID]

        if self.departamentoID not in prov.diccionarioDptos:
            prov.diccionarioDptos[self.departamentoID] = self
                    
    def __str__(self):
        return self.departamento

class Municipio():
    def __init__(self, provinciaID:str, provincia:str, departamentoID:str, departamento:str, municipioID:str, municipio:str):
        self.provinciaID = provinciaID
        self.provincia = provincia        
        self.departamentoID = departamentoID
        self.departamento = departamento
        self.municipioID = municipioID
        self.municipio = municipio
        
        if self.municipioID == None:
            print("No se pudo crear el municipio-->Municipio sin identificacion")
            return
        
        if self.provinciaID not in Provincia.diccionarioProv:
            print("No se pudo crear el municipio-->Provincia no registrada")
            return

        prov: Provincia = Provincia.diccionarioProv[self.provinciaID]
        if self.departamentoID not in prov.diccionarioDptos:
            print ("Departamento no registrado")
            return 
    
        dpto = prov.diccionarioDptos[self.departamentoID]
        if self.municipioID not in dpto.diccionarioMunicipios:
            dpto.diccionarioMunicipios.update({self.municipioID:self})
            #dpto.diccionarioMunicipios[self.municipioID] = self 

    def __str__(self):
        return self.municipio    