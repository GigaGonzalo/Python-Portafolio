from fastapi import FastAPI, HTTPException
from historial_tareas import (cargar_historial_db, crear_tarea_db, eliminar_tarea_db, guardar_tarea_db)
from tareas import TareaDB , CrearTareaDB

app = FastAPI(title="Sistema de Tareas API v.1")

@app.get("/tareas", response_model=list[TareaDB])
def obtener_tareas():
    return cargar_historial_db()

@app.get("/tareas/{index}", response_model=TareaDB)
def obtener_una_tarea(index : int):
    lista = cargar_historial_db()
    for t in lista:
        if t["index"] == index:
            return t
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

@app.post("/tareas", response_model=TareaDB)
def crear_tareas(tarea: CrearTareaDB):
    return crear_tarea_db(tarea.index, tarea.categoria, tarea.importancia, tarea.tex_tarea, tarea.fecha_creacion,
    tarea.recordatorio, tarea.fecha_vencimiento_año, tarea.fecha_vencimiento_mes, tarea.fecha_vencimiento_dia,
    tarea.hora_alarma, tarea.min_alarma)

@app.delete("/tareas", response_model=list[TareaDB])
def eliminar_tarea(index : int):
    return eliminar_tarea_db(index)

@app.put("/tareas", response_model=TareaDB)
def actualizar_tarea(index : int, tarea_act : CrearTareaDB):
    lista = cargar_historial_db()
    for t in lista:
        if t["index"] == index:
            t["index"] = index
            t["categoria"] = tarea_act.categoria
            t["importancia"] = tarea_act.importancia
            t["tex_tarea"] = tarea_act.tex_tarea
            t["fecha_creacion"] = tarea_act.fecha_creacion
            t["recordatorio"] = tarea_act.recordatorio
            t["fecha_vancimiento_año"] = tarea_act.fecha_vencimiento_año
            t["fecha_vencimiento_mex"] = tarea_act.fecha_vencimiento_mes
            t["fecha_vencimiento_dia"] = tarea_act.fecha_vencimiento_dia
            t["hora_alarma"] = tarea_act.hora_alarma
            t["min_alarma"] = tarea_act.min_alarma
            guardar_tarea_db(lista)
            return t
    raise HTTPException(status_code=404, detail="Tarea no encontrada")


