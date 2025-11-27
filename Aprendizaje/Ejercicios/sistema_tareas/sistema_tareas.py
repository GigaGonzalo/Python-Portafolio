from tareas import Tarea
from historial_tareas import Guardador
from enumeraciones import Importancias, Categorias


class SistemaTareas:

    def __init__(self):
        self.opciones_validas_menu = ["1", "2", "3","4"]
        self.guardar = Guardador()

    def categoria_tarea(self):
        print("SELECCIONE LA CATEGORIA DE LA TAREA")
        print("1. HOGAR")
        print("2. ESCUELA")
        print("3. TRABAJO")
        print("4. SIN ETIQUETA")
        cat = input("CATEGORIA = ")
        if cat in self.opciones_validas_menu:
            if cat == "1":
                return Categorias.HOGAR.value
            elif cat == "2":
                return Categorias.ESCUELA.value
            elif cat == "3":
                return Categorias.TRABAJO.value
            elif cat == "4":
                return Categorias.SIN_ETIQUETA.value
        else:
            print("Ingrese una opccion valida!!")

    def importancia_tarea(self):
        print("SELECCIONE NIVEL DE IMPORTANCIA")
        print("1. BAJO")
        print("2. MEDIO")
        print("3. ALTO")
        print("4. SIN IMPORTANCIA")
        cat = input("CATEGORIA = ")
        if cat in self.opciones_validas_menu:
            if cat == "1":
                return Importancias.BAJO.value
            elif cat == "2":
                return Importancias,MEDIO.value
            elif cat == "3":
                return Importancias.ALTO.value
            elif cat == "4":
                return Importancias.SIN_ETIQUETA.value
        else:
            print("Ingrese una opccion valida!!")

    def texto_tarea(self):
        t_tarea = input("Ingrese la tarea o pendiente : ")
        return t_tarea

    def recordatorio_tarea(self):
        while True:
            recordatorio = input("¿Desea crear un recordatorio para esta tarea?     s/n  ").lower()
            if recordatorio.isalpha() and recordatorio in ("s", "n"):
                return True if recordatorio == "s" else False
            else:
                print("Ingrese una opccion valida!!! (s / n)")

    def fecha_recordatorio(self):
        
        print("Ingrese la fecha de la alarma en formato 00/00/0000)")
        
        while True:
            año = input("Ingrese el año : ")
            try:
                year = int(año)
                if 2025 <= year <= 2225:
                    break
                else:
                    raise ValueError("Ingrese un valor entre 2025 y 2225")
            except ValueError as e:
                print("Ingrese un numero entre (2025 - 2225)")
        while True:
            mes = input("Ingrese el mes de la alarma :")
            try:
                month = int(mes)
                if 0 < month <= 12:
                    break
                else:
                    raise ValueError("Ingrese un valor entre 01 y 12")
            except ValueError:
                print("Ingrese un numero entre (01 - 12)")
        while True:
            dia = input("Ingrese el dia de la alarma :")
            try:
                day = int(dia)
                dia_ultimo = 31 if month == (1,3,5,7,9,11) else 30
                if 0 < day <= dia_ultimo:
                    break
                else:
                    raise ValueError(f"Ingrese un valor entre 01 y {dia_ultimo}")
            except ValueError:
                print(f"Ingrese un numero entre (01 - {dia_ultimo})")
        return (año, mes, dia)

    def alarma_tarea(self):
        
        print("Ingrese la hora de la alarma con formato 24hrs (00:00)")
        
        while True:
            hrs = input("Ingrese la hora : ")
            try:
                f_hrs = int(hrs)
                if 0 <= f_hrs < 24:
                    break
                else:
                    raise ValueError("Ingrese un valor entre 0 y 24")
            except ValueError as e:
                print("Ingrese un numero entre (00 - 23)")
        while True:
            m = input("Ingrese los minutos de la alarma :")
            try:
                f_min = int(m)
                if 0 <= f_min < 60:
                    break
                else:
                    raise ValueError("Ingrese un valor entre 0 y 60")
            except ValueError:
                print("Ingrese un numero entre (00 - 59)")
        return (hrs, m)
        
    def menu_lista_tareas(self, lista_tareas):
        print("*"*10 + " LISTA DE TAREAS " + "*"*10)
        if lista_tareas != None:
            for tarea in lista_tareas:
                print(f"Tarea No. {tarea.getIndex} \nAsunto : {tarea.getTarea} \nCategoria : {tarea.getCategoria} \nImportancia : {tarea.getImportancia} "
                + f"\nRecordatorio {"SI" if tarea.getRecordatorio == True else "NO"} ")
                if tarea.getRecordatorio == True:
                    print(f"Fecha de Recordatorio : {tarea.getFechaAlarma} \nHora de Recordatorio : {tarea.getHoraAlarma}\n")
                else:
                    print()
        print("Presione x para regresar " + 
        ("O ingrese el numero de la tarea para modificar" if lista_tareas != [] else ""))
        opccion = input("Seleccione : ").lower()
        if opccion == "x":
            self.menu_principal()
        elif opccion.isdecimal() and int(opccion) <= len(lista_tareas):
            self.menu_nueva_tarea(lista_tareas[int(opccion) - 1])
        else:
            print("Ingrese una opccion valida!")

    def eliminar_tarea(self, index_eliminar):
        lista = self.guardar._cargar_historial()
        print(lista)
        lista.pop(index_eliminar - 1)
        print(lista)
        lista_reindexada = self.reindexado(lista)
        print(lista)
        self.guardar._guardar_historial(lista_reindexada)
        print("TAREA ELIMINADA EXITOSAMENTE!!")

    def reindexado(self, lista_hueco):
        lista_hueco.sort(key=lambda x: x["index"])
        index = 1
        for tarea in lista_hueco:
            tarea["index"] = index
            index += 1
        return lista_hueco


    def menu_principal(self):
        lista = self.conversor_total_dic_obj(self.guardar._cargar_historial())
        while True:
            print("*"*15 + " Sistema de Tareas " + "*"*15 + "\n")
            print("1. Nueva Tarea")
            print("2. Lista de Tareas")
            print("3. Salir")
            opccion = input("Seleccione : ")

            if opccion in self.opciones_validas_menu:
                if opccion == "1":
                    self.menu_nueva_tarea()
                elif opccion == "2":
                    self.menu_lista_tareas(lista)
                elif opccion == "3":
                    exit()
            else:
                print("Ingrese una opccion valida!")
                
    def menu_nueva_tarea(self, nueva_tarea = None):
        borrable = False
        if nueva_tarea == None:
            nueva_tarea = Tarea()
        else:
            borrable = True

        while True:
            opcciones_validas = ["1","2","3","4","5","6", "x"]
            print("TAREA")
            print(f"1- Categoria     {nueva_tarea.getCategoria}")
            print(f"2- Importancia   {nueva_tarea.getImportancia}")
            print(f"3- Tarea         {nueva_tarea.getTarea}")
            print(f"4- Recordatorio  {"No"if nueva_tarea.getRecordatorio == False else "Si"}")
            if nueva_tarea.getRecordatorio == True:
                print(f"    Fecha        {nueva_tarea.getFechaAlarma}")
                print(f"    Hora         {nueva_tarea.getHoraAlarma}" +
                " pm" if int(nueva_tarea.hora_alarma) > 11 else " am")
            print("5- Guardar \n")
            if borrable:
                print("X - Eliminar")
            print("6- Regresar")
            opccion = input("Seleccione : ").lower()

            if opccion in opcciones_validas:
                if opccion == "1":
                    cat = self.categoria_tarea()
                    nueva_tarea.setCategoria(cat)
                elif opccion == "2":
                    imp = self.importancia_tarea()
                    nueva_tarea.setImportancia(imp)
                elif opccion == "3":
                    tex = self.texto_tarea()
                    nueva_tarea.setTarea(tex)
                elif opccion == "4":
                    rec = self.recordatorio_tarea()
                    nueva_tarea.setRecordatorio(rec)
                    if nueva_tarea.getRecordatorio == True:
                        año_alarma, mes_alarma, dia_alarma = self.fecha_recordatorio()
                        nueva_tarea.setFecha_Alarma(año_alarma, mes_alarma, dia_alarma)
                        h_alarma, m_tarea = self.alarma_tarea()
                        nueva_tarea.setHora_Alarma(h_alarma, m_tarea)
                elif opccion == "5":
                    nueva_tarea.fecha_creacion = nueva_tarea.fecha_creacion_tarea()
                    tarea_dic = self._conversor_Dicc(nueva_tarea)
                    self.guardar_tarea(tarea_dic)
                    self.menu_principal()
                elif opccion == "x" and borrable == True:
                    self.eliminar_tarea(nueva_tarea.getIndex)
                    self.menu_principal()
                elif opccion == "6":
                    self.menu_principal()
            else:
                print("Ingrese una opccion valida!!")
    def guardar_tarea(self, dic_tarea):
        h_tareas = self.guardar._cargar_historial()
        if h_tareas == None:
            h_tareas = []
        print(h_tareas)
        h_tareas.append(dic_tarea)
        print(h_tareas)
        self.guardar._guardar_historial(h_tareas)

    def _conversor_Dicc(self, tarea_obj):
        
        tarea_dic = {
            "index": int(self.guardar.index_tareas) + 1 ,
            "categoria": tarea_obj.getCategoria ,
            "importancia": tarea_obj.importancia ,
            "tex_tarea": tarea_obj.tex_tarea ,
            "fecha_creacion": tarea_obj.fecha_creacion , 
            "recordatorio": tarea_obj.recordatorio ,
            "fecha_vencimiento_año": tarea_obj.fecha_vencimiento_año ,
            "fecha_vencimiento_mes": tarea_obj.fecha_vencimiento_mes ,
            "fecha_vencimiento_dia": tarea_obj.fecha_vencimiento_dia ,
            "hora_alarma": tarea_obj.hora_alarma ,
            "min_alarma": tarea_obj.min_alarma
        }
        self.guardar.index_tareas += 1
        return tarea_dic

    def _conversor_Obj(self, diccionario : dict):
        n_tarea = Tarea()

        n_tarea.setIndex(diccionario["index"])
        print(n_tarea.getIndex)
        n_tarea.setCategoria(diccionario["categoria"])
        n_tarea.setImportancia(diccionario["importancia"])
        n_tarea.setTarea(diccionario["tex_tarea"])
        n_tarea.fecha_creacion = diccionario["fecha_creacion"]
        n_tarea.setRecordatorio(diccionario["recordatorio"])
        n_tarea.setFecha_Alarma(diccionario["fecha_vencimiento_año"],
        diccionario["fecha_vencimiento_mes"],diccionario["fecha_vencimiento_dia"])
        n_tarea.setHora_Alarma(diccionario["hora_alarma"],diccionario["min_alarma"])

        return n_tarea

    def conversor_total_dic_obj(self, lista_dic : list):
        if lista_dic != None:
            print(lista_dic)
            lista_objs = []
            for tarea in lista_dic:
                print(tarea)
                lista_objs.append(self._conversor_Obj(tarea))
            return lista_objs
        else: 
            return []

    def conversor_total_obj_dic(self, lista_objs):
        lista_dic = []
        for tarea in lista_objs:
            lista_dic.append(self._conversor_Dicc(tarea))
        return lista_dic


Sistema = SistemaTareas()
Sistema.menu_principal()
        


