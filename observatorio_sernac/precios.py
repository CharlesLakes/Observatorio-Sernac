from .global_vars import *
import requests
import json

class Precios:
    def __init__(self,id_comuna):
        self.id_comuna = id_comuna
        self.productos = []

    def agregar_producto(self,id_subcategoria,id_rango):
        self.productos.append({
            "id_rango": id_rango,
            "id_subcategoria": id_subcategoria
        })
    
    def obtener_disponibilidad(self):
        req = json.dumps({
            "id_comuna": self.id_comuna,
            "productos": self.productos
        })

        headers = {
            "content-type":"application/json"
        }

        self.minimo = requests.post(LINK_DISPO,data=req,headers=headers).json()
        return self.minimo

    def obtener_minimo(self):
        req = json.dumps({
            "id_comuna": self.id_comuna,
            "productos": self.productos
        })

        headers = {
            "content-type":"application/json"
        }

        self.minimo = requests.post(LINK_MINIMO,data=req,headers=headers).json()
        return self.minimo

    def obtener_promedio(self):
        req = json.dumps({
            "id_comuna": self.id_comuna,
            "productos": self.productos
        })

        headers = {
            "content-type":"application/json"
        }

        self.minimo = requests.post(LINK_PROMEDIO,data=req,headers=headers).json()
        return self.minimo
