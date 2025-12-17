import os
from model_tarea import Tarea, GestorTarea
from sistema_db import GestorBD

class SistemWorks:

    def __init__(self):
        self.gestor_t = GestorTarea()
        self.gestor_db = GestorBD()

    def limpiar_pantalla(self):
        if os.name == 'nt':
            _ = os.system('cls')
        else: 
            _ = os.system('clear')

    def main_menu(self):
        self.limpiar_pantalla()
        options = ("1","2","3","4","5")
        print("*"*15 + "     Main   Menu    " + "*"*15)
        print("1. Crear Tarea")
        print("2. Lista de Tareas")
        print("3. Modificar Tareas")
        print("4. Eliminar Tareas")
        print("5. Salir")
        select = input("Seleccione :").strip()
        if select in options:
            if select == "1":
                self.crear_tarea()
            elif select == "2":
                pass
            elif select == "3":
                pass
            elif select == "4":
                pass
            elif select == "5":
                quit()
        else:
            print("Ingrese una opccion valida! (1,2,3,4,5)")

    def crear_tarea(self, n_tarea = None):
        option_t = ["1","2","3","4","5","6","7","8"]
        option_f = ["1","2","3","4","5","6"]
        if n_tarea == None:
            n_tarea = Tarea()
        tarea_tup = ""
        while True:
            self.limpiar_pantalla()
            print("*"*17 + "     Tareas     " + "*"*17)
            
            if n_tarea.get_recordatorio == True:
                options = option_t
                print("1. Titulo")
                print(n_tarea.get_titulo)
                print("2. Descripcion")
                print(n_tarea.get_descripcion)
                print("3. Categoria")
                print(n_tarea.get_categoria)
                print("4. Recordatorio")
                print("SI")
                print("5. Fecha recordatorio")
                print(n_tarea.get_fecha)
                print("6. Horario recordatorio")
                print(n_tarea.get_horario)
                print("7. Guardar tarea")
                print("8. Regresar al menu")
            else:
                options = option_f
                print("1. Titulo")
                print(n_tarea.get_titulo)
                print("2. Descripcion")
                print(n_tarea.get_descripcion)
                print("3. Categoria")
                print(n_tarea.get_categoria)
                print("4. Recordatorio")
                print("NO")
                print("5. Guardar tarea")
                print("6. Regresar al menu")
            select = input("Seleccione")
            if select in options:
                if select == "1":
                    n_tarea._set_titulo(self.gestor_t.validar_titulo())
                elif select == "2":
                    n_tarea._set_desc(self.gestor_t.validar_descripcion())
                elif select == "3":
                    n_tarea._set_categoria(self.gestor_t.validar_categoria())
                elif select == "4":
                    n_tarea._set_recordatorio(self.gestor_t.validar_recordatorio())
                elif select == "5":
                    if options == option_t:
                        n_tarea._set_fecha(self.gestor_t.validar_fecha())
                    else:
                        tarea_tup = n_tarea.conv_tupla()
                        pass #Guardar
                elif select == "6":
                    if options == option_f:
                        n_tarea._set_horario(self.gestor_t.validar_horario())
                    else:
                        self.regresar_menu()
                elif select == "7" and options == option_t:
                    tarea_tup = n_tarea.conv_tupla()
                    print(tarea_tup)
                    pass  #guardar
                elif select == "8" and options == option_t:
                    self.regresar_menu()
            else:
                print(f"Ingrese una opccion valida {options}")
        
    def listar_tarea(self):
        pass

    def eliminar_tarea(self):
        print("*"*15 + "   ELIMINAR TAREA   " + "*"*15)
        select = input("Ingrese el numero de la tarea a ELIMINAR : ")

    def regresar_menu(self):
        self.main_menu()

def main():
    system = SistemWorks()
    system.main_menu()
    

if __name__ == "__main__":
    main()
