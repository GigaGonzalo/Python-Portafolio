import json
import os

url = "historial_tareas.json"

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