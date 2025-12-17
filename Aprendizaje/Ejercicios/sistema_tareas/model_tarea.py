from enum_tareas import CategoriasTareas
from datetime import datetime


class Tarea():

    def __init__(self, usuario = 0 , titulo = "Titulo", descripcion = "Descripcion", categoria = CategoriasTareas(0).name,
     recordatorio = False, fecha = "--/--/----", horario = "--:--"):

        self.usuario = usuario
        self.titulo = titulo
        self.descripcion = descripcion
        self.categoria = categoria
        self.recordatorio = recordatorio
        self.r_fecha = fecha
        self.r_horario = horario

    def _set_usuario(self, usu:str):
        self.usuario = usu

    def _set_titulo(self, tit:str):
        self.titulo = tit

    def _set_desc(self, desc:str):
        self.descripcion = desc

    def _set_categoria(self, cat:str):
        self.categoria = cat

    def _set_recordatorio(self, rec:bool):
        self.recordatorio = rec

    def _set_fecha(self, fecha:str):
        self.r_fecha = fecha

    def _set_horario(self, horario:str):
        self.r_horario = horario

    @property
    def get_usuario(self) -> int:
        return self.usuario

    @property
    def get_titulo(self) -> str:
        return self.titulo

    @property
    def get_descripcion(self) -> str:
        return self.descripcion

    @property
    def get_categoria(self) -> str:
        return self.categoria

    @property
    def get_recordatorio(self) -> bool:
        return self.recordatorio

    @property
    def get_fecha(self) -> str:
        return self.r_fecha

    @property
    def get_horario(self) -> str:
        return self.r_horario

    def conv_tupla(self):
        t_tarea = (
            self.get_titulo,
            self.get_descripcion,
            self.get_categoria,
            self.get_recordatorio,
            self.get_fecha, 
            self.get_horario
        )
        return t_tarea

class GestorTarea():

    def validar_titulo(self) -> str:
        while True:
            texto = input("Titulo   = \n")
            if len(texto) != 0:
                return texto
            else:
                print("El campo TITULO no puede permanecer vacio!")

    def validar_descripcion(self) -> str:
        texto = input("Descripcion  = \n")
        return texto

    def validar_categoria(self) -> str:
        while True:
            texto = input("0-sin categoria 1-hogar 2-trabajo 3-escuela 4-social" +
                "Categoria    = ").strip()
            if len(texto) == 1 and texto.isdecimal() and texto in ("0","1","2","3","4"):
                return CategoriasTareas(int(texto)).name
            else:
                print("Ingrese una categoria VALIDA!")

    def validar_recordatorio(self) -> bool:
        while True:
            texto = input("¿Desea programar un recordatorio?    S/N").strip().upper()
            if len(texto) > 0 and texto in ("S","N"):
                if texto == "S":
                    return True
                else:
                    return False
            else:
                print("Ingrese una opccion VALIDA! (S / N)")


    def validar_fecha(self) -> str:
        print("Ingrese la fecha con formato(dia/mes/año)")
        while True:
            dia = input("Ingrese el dia")
            if int(dia) > 0 and int(dia) < 31:
                dia = int(dia)
                break
            else:
                print("Ingrese una cifra valida para el dia")
        
        while True:
            mes = input("Ingrese el mes")
            if int(mes) >= 1 and int(mes) <= 12:
                mes = int(mes)
                break
            else:
                print("Ingrese una cifra valida para el mes")
        
        while True:
            an = input("Ingrese el año")
            if int(an) >= 2025 and int(an) <= 2030:
                an = int(an)
                break
            else:
                print("Ingrese una cifra valida para el mes")
        
        horario = datetime.date(an,mes,dia)
        return horario.strftime("%d/%m/%Y")

    def validar_horario(self) -> str:
        print("Ingrese la hora con formato 24 hrs (horas:minutos)")
        while True:
            hora = input("Ingrese la hora :")
            if int(hora) > 0 and int(hora) <= 23:
                hora = int(hora)
                break
            else:
                print("Ingrese una cifra valida para la hora")
        
        while True:
            minutos = input("Ingrese los minutos")
            if int(minutos) >= 0 and int(minutos) <= 59:
                minutos = int(minutos)
                break
            else:
                print("Ingrese una cifra valida para los minutos")
        horario = datetime.date(hora,minutos)

        return horario.strftime("%H:%M")