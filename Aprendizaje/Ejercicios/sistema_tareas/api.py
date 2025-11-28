from fastapi import FastAPI
#from historial_tareas import conector

app = FastAPI(title="Sistema de Tareas API v.1")

@app.get("/tareas", response_model=list[TareaDB])
def obtener_tarea():
    return conector.cargar_historial_db()

@app.post("/tareas", response_model=TareaDB)
def crear_tarea(tarea: CrearTareaDB):
    return conector.crear_tarea_db(tarea)

@app.delete("/tareas", response_model=list[TareaDB])
def eliminar_tarea(index : int):
    return conector.eliminar_tarea_db(index)