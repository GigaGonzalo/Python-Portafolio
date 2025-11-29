from fastapi import FastAPI
from historial_tareas import (cargar_historial_db, crear_tarea_db, eliminar_tarea_db)
from tareas import TareaDB , CrearTareaDB

app = FastAPI(title="Sistema de Tareas API v.1")

@app.get("/tareas", response_model=list[TareaDB])
def obtener_tarea():
    return cargar_historial_db()

@app.post("/tareas", response_model=TareaDB)
def crear_tarea(tarea: CrearTareaDB):
    return crear_tarea_db(tarea.index, tarea.categoria, tarea.importancia, tarea.tex_tarea, tarea.fecha_creacion,
    tarea.recordatorio, tarea.fecha_vencimiento_año, tarea.fecha_vencimiento_mes, tarea.fecha_vencimiento_dia,
    tarea.hora_alarma, tarea.min_alarma)

@app.delete("/tareas", response_model=list[TareaDB])
def eliminar_tarea(index : int):
    return eliminar_tarea_db(index)