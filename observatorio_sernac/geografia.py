from .global_vars import *
import requests

class Geografia:
    def __init__(self):
        print(LINK_GEO)
        self.data = requests.get(LINK_GEO).json()

    def obtener_comunas(self):
        return self.data["comunas"]

    def obtener_comunas_de_region(self,id_region):
        list_comunas = []
        for comuna in self.data["comunas"]:
            if comuna["id_region"] == id_region:
                list_comunas.append(comuna)
        return list_comunas

    def obtener_regiones(self):
        return self.data["regiones"]

    
