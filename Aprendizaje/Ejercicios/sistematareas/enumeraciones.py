from enum import Enum

class Categorias(Enum):
    HOGAR = "HOGAR"
    ESCUELA = "ESCUELA"
    TRABAJO = "TRABAJO"
    SIN_ETIQUETA = "COMUN"

class Importancias(Enum):
    BAJO = "BAJO"
    MEDIO = "MEDIO"
    ALTO = "ALTO"
    SIN_ETIQUETA = "SIN IMPORTANCIA"
