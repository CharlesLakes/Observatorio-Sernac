from .global_vars import *
import requests

class Categorizacion:
    def __init__(self,id_comuna):
        self.data = requests.get(LINK_CATE).json()
    
    def obtener_departamentos(self):
        return self.data["departamentos"]

    def obtener_categorias(self):
        return self.data["categorias"]

    def obtener_subcategorias(self):
        return self.data["subcategorias"]

    def obtener_categorias_por_departamento(self,id_departamento):
        list_categorias = []
        for categoria in self.data["departamentos"]:
            if categoria["id_departamento"] == id_departamento:
                list_categorias.append(categoria)
        return list_categorias
    
    def obtener_subcategorias_por_categoria(self,id_categoria):
        list_subcategorias = []
        for subcategoria in self.data["categorias"]:
            if subcategoria["id_categoria"] == id_categoria:
                list_subcategorias.append(subcategoria)
        return list_subcategorias
        

