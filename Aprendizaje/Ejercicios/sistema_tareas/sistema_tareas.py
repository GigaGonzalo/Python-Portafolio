from tareas import Tarea


class SistemaTareas:

    def __init__(self):
        self. opciones_validas_menu = ["1", "2", "3"]
        pass

    def categoria_tarea(self):
        print("SELECCIONE LA CATEGORIA DE LA TAREA")
        print("1. HOGAR")
        print("2. ESCUELA")
        print("3. TRABAJO")
        print("4. SIN ETIQUETA")
        cat = input("CATEGORIA = ")
        if cat in self.opciones_validas_menu:
            if cat == "1":
                return "HOGAR"
            elif cat == "2":
                return "ESCUELA"
            elif cat == "3":
                return "TRABAJO"
            elif cat == "4":
                return "SIN ETIQUETA"
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
                return "BAJO"
            elif cat == "2":
                return "MEDIO"
            elif cat == "3":
                return "ALTO"
            elif cat == "4":
                return "SIN IMPORTANCIA"
        else:
            print("Ingrese una opccion valida!!")

    def texto_tarea(self):
        t_tarea = input("Ingrese la tarea o pendiente : ")
        return t_tarea

    def recordatorio_tarea(self):
        recordatorio = input("¿Desea crear un recordatorio para esta tarea?     S/N").lower() 
        if recordatorio.isalpha() and recordatorio in ("s", "n"):
            return True if recordatorio == "s" else False

    def alarma_recordatorio(self):
        return "02/02/2026"

    def menu_principal(self):
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
                    pass
                elif opccion == "3":
                    exit()

            else:
                print("Ingrese una opccion valida!")
                
    def menu_nueva_tarea(self, nueva_tarea = Tarea()):
        
        while True:
            opcciones_validas = ["1","2","3","4","5"]
            print("TAREA")
            print(f"1- Categoria     {nueva_tarea.getCategoria}")
            print(f"2- Importancia   {nueva_tarea.getImportancia}")
            print(f"3- Tarea         {nueva_tarea.getTarea}")
            print(f"4- Recordatorio  {"No"if nueva_tarea.getRecordatorio == False else "Si"}")
            if nueva_tarea.getRecordatorio == True:
                print(f"5- Alarma        {nueva_tarea.getAlarma}")
            print("5- Regresar")
            opccion = input("Seleccione : ")
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
                        alarma = self.alarma_recordatorio()
                        nueva_tarea.setVencimiento(alarma)
                elif opccion == "4":
                    pass
                elif opccion == "5":
                    exit()
            else:
                print("Ingrese una opccion valida!!")


Sistema = SistemaTareas()
Sistema.menu_principal()
        


