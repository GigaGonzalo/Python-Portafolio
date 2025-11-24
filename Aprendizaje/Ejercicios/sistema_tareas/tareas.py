

import datetime
class Tarea:

    def __init__(self):
        
        self.categoria = "Ninguna"
        self.importancia = "Ninguna"
        self.tex_tarea = "Vacio"
        self.fecha_creacio = ""
        self.recordatorio = False
        self.fecha_vencimiento = ""
        

    def ini_tarea(self):
        self.tex_tarea = input("Anote la tarea a recordar: ")

    def fecha_vencimiento(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def importancia_tarea(self, nivel_imp):
        self.importancia = nivel_imp

    def categoria_tarea(self, categoria_tarea):
        self.categoria = categoria_tarea
        

    def setCategoria(self , nueva_categoria):
        self.categoria = nueva_categoria

    def setImportancia(self , nueva_importancia):
        self.importancia = nueva_importancia

    def setTarea(self , nueva_tarea):
        self.tex_tarea = nueva_tarea

    def setRecordatorio(self , nuevo_recordatorio):
        self.recordatorio = nuevo_recordatorio

    def setVencimiento(self, fecha_vencimiento):
        self.fecha_vencimiento = fecha_vencimiento


    @property
    def getCategoria(self):
        return self.categoria
    @property
    def getImportancia(self):
        return self.importancia
    @property
    def getTarea(self):
        return self.tex_tarea
    @property
    def getRecordatorio(self):
        return self.recordatorio
    @property
    def getAlarma(self):
        return self.fecha_vencimiento
        
    def conversor_Dicc():
        pass

    def conversor_Obj():
        pass

        