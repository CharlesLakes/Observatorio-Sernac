from .global_vars import *
import requests

class Rangos:
    def __init__(self,id_subcategoria):
        self.data = requests.get(LINK_RANGOS.format(id_subcategoria)).json()

    def obtener_rangos(self):
        return self.data

