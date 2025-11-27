
from datetime import datetime
class Tarea:

    def __init__(self):
        
        self.index = 0
        self.categoria = "Ninguna"
        self.importancia = "Ninguna"
        self.tex_tarea = "Vacio"
        self.fecha_creacion = ""
        self.recordatorio = False
        self.fecha_vencimiento_año = ""
        self.fecha_vencimiento_mes = ""
        self.fecha_vencimiento_dia = ""
        self.hora_alarma = ""
        self.min_alarma = ""
 
    def fecha_creacion_tarea(self):
       return datetime.now().strftime("%Y-%m-%d %H:%M")
    
    def importancia_tarea(self, nivel_imp):
        self.importancia = nivel_imp

    def categoria_tarea(self, categoria_tarea):
        self.categoria = categoria_tarea
        
    def setIndex(self, ind):
        self.index = ind
        
    def setCategoria(self , nueva_categoria):
        self.categoria = nueva_categoria

    def setImportancia(self , nueva_importancia):
        self.importancia = nueva_importancia

    def setTarea(self , nueva_tarea):
        self.tex_tarea = nueva_tarea

    def setRecordatorio(self , nuevo_recordatorio):
        self.recordatorio = nuevo_recordatorio

    def setFecha_Alarma(self, año, mes , dia):
        self.fecha_vencimiento_año = año
        self.fecha_vencimiento_mes = mes
        self.fecha_vencimiento_dia = dia

    def setHora_Alarma(self, hora, minuto):
        self.hora_alarma = hora
        self.min_alarma = minuto

    @property
    def getIndex(self):
        return self.index
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
    def getFechaAlarma(self):
        fecha = self.fecha_vencimiento_dia + "/" + self.fecha_vencimiento_mes + "/" + self.fecha_vencimiento_año
        return fecha
    @property
    def getHoraAlarma(self):
        hora = self.hora_alarma + ":" + self.min_alarma
        return hora
    @property
    def getMinAlarma(self):
        return self.min_alarma
        
    

        