import json
import os
from typing import Dict, List
#from sistema_tareas import SistemaTareas

url = "tareas.json"

class Guardador:

    def __init__(self):
        self.url = "historial_tareas.json"
        self.index_tareas = self._ini_index_()


    def _cargar_historial(self):
        try:
            if os.path.exists(url):
                with open(url, "r", encoding="utf-8") as archivo:
                    return json.load(archivo)
        except (json.JSONDecodeError, Exception) as e:
            print(json.load(archivo))

            print(f"{e}")

    def _guardar_historial(self, historial_tareas):
        self._limpiar_archivo_()
        try:
            with open(url, "w", encoding="utf-8") as archivo:
                json.dump(historial_tareas, archivo, ensure_ascii=False, indent=2)
        except (json.JSONDecodeError, Exception) as e:
            print(f"{e}")

    def _ini_index_(self):
        historial = self._cargar_historial()
        if historial == None:
            return 0
        else:
            index = len(historial)
            return index

    def _limpiar_archivo_(self):
        limpio = []
        try:
            with open(url, "w", encoding="utf-8") as archivo:
                json.dump(limpio, archivo, ensure_ascii=False, indent=2)
        except (json.JSONDecodeError, Exception) as e:
            print(f"{e}")

            
#sistema = SistemaTareas()

conector = Guardador()

def crear_tarea_db(index : int, categoria : str , importancia : str , tex_tarea : str , fecha_creacion : str,
recordatorio : bool , fecha_vencimiento_año : str , fecha_vencimiento_mes : str , fecha_vencimiento_dia : str, 
hora_alarma : str , min_alarma : str) -> Dict:
    lista_tareas = conector._cargar_historial()
    if index in ((t["index"] for t in lista_tareas)):
        pass
    else:
        n_index = max((t["index"] for t in lista_tareas), default = 0) + 1
    n_tarea = {
        "index" : n_index ,
        "categoria" : categoria ,
        "importancia" : importancia ,
        "tex_tarea" : tex_tarea ,
        "fecha_creacion" : fecha_creacion ,
        "recordatorio" : recordatorio ,
        "fecha_vencimiento_año" : fecha_vencimiento_año ,
        "fecha_vencimiento_mes" : fecha_vencimiento_mes ,
        "fecha_vencimiento_dia" : fecha_vencimiento_dia , 
        "hora_alarma" : hora_alarma , 
        "min_alarma" : min_alarma 
    }
    lista_tareas.append(n_tarea)
    conector._guardar_historial(lista_tareas)
    return n_tarea

def cargar_historial_db():
    return conector._cargar_historial()

def eliminar_tarea_db(index_eliminar : int):
    lista = conector._cargar_historial()
    lista.pop(index_eliminar - 1)
    lista.sort(key=lambda x: x["index"])
    index = 1
    for tarea in lista:
        tarea["index"] = index
        index += 1
    conector._guardar_historial(lista)
    return lista

def guardar_tarea_db(lista : list):
    conector._guardar_historial(lista)