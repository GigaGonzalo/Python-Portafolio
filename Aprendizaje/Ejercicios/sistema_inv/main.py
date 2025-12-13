from sistema_bd import GestorBD
from cat_enum import Categorias
from articulo import Articulo
from articulo import GestorArticulo
import colorama
from colorama import Fore, Style, init, Back
import os

init(autoreset=True)
class SistemaInventario():

    def __init__(self):
        self.gestor = GestorBD()
        self.gestor.verificar_db()
        self.gestor.crear_tabla_articulos()

        self.gestor_ar = GestorArticulo()

    def registro_nuevo_producto(self):
        nuevo_articulo = Articulo()
        self.limpiar_pantalla()
        nuevo_articulo.set_categoria(self.gestor_ar.mod_categoria())
        self.limpiar_pantalla()
        nuevo_articulo.set_codigo(self.gestor_ar.mod_codigo())
        self.limpiar_pantalla()
        nuevo_articulo.set_nom_producto(self.gestor_ar.mod_nombre())
        self.limpiar_pantalla()
        nuevo_articulo.set_descripcion(self.gestor_ar.mod_descripcion())
        self.limpiar_pantalla()
        nuevo_articulo.set_precio(self.gestor_ar.mod_precio())
        self.limpiar_pantalla()
        nuevo_articulo.set_existencia(self.gestor_ar.mod_existencias())
        self.limpiar_pantalla()
        
        nuevo_articulo = nuevo_articulo.conv_tupla()

        self.gestor.insertar_nuevo_articulo_bd(nuevo_articulo)

        input("Presione ENTER para regresar al menu")
        self.menu_principal()

    def visualizar_articulos_menu(self):
        self.limpiar_pantalla()
        opcciones_validas = ("1","2","3","4","5","6")
        print("Lista de Articulos Exsistentes")
        print("1. Articulo por CODIGO")
        print("2. Articulo por CATEGORIA")
        print("3. Articulo por PRECIO")
        print("4. Articulo por NOMBRE")
        print("5. TODOS los articulos existentes")
        print("6. Regresar al menu")
        opccion = input("Seleccione : ")
        if opccion in opcciones_validas:
            if opccion == "1":
                while True:
                    self.limpiar_pantalla()
                    codigo = input("Ingrese CODIGO del articulo a buscar : ").strip()
                    if len(codigo) < 15 and codigo.isnumeric():
                        b_articulo = self.gestor.visualizar_articulo(codigo)
                        if b_articulo != ():
                            print(f"Articulo No. {b_articulo[0]} \n Codigo : {b_articulo[2]} \n Categoria : {b_articulo[1]}"+
                            f"\n Nombre : {b_articulo[3]} \n Descripcion = {b_articulo[4]} \n Precio : {b_articulo[5]} \n"+
                            f" Existencias : {b_articulo[6]}")
                            break
                        else:
                            print(f"{Fore.YELLOW}Ingrese un CODIGO de articulo existente")
                    else:
                        print(f"{Fore.YELLOW}Ingrese un codigo valido")
                input(f"{Style.DIM}Presione ENTER para regresar! ")
                self.visualizar_articulos_menu()
            if opccion == "2":
                while True:
                    self.limpiar_pantalla()
                    cat = input("Ingrese la CATEGORIA del articulo a buscar : \n"+
                    "1-LACTEOS, 2-CONGELADOS, 3-MERCADO, 4-ABARROTES, 5-ROPA, 6-HOGAR, 7-ELECTRONICA\n").strip()
                    if cat in ("1","2","3","4","5","6","7"):
                        b_articulos = self.gestor.visualizar_articulos("categoria" ,Categorias(int(cat)).name)
                        if b_articulos != []:
                            for b_articulo in b_articulos:
                                print(f" Codigo : {b_articulo[2]} \n Categoria : {b_articulo[1]}"+
                                f"\n Nombre : {b_articulo[3]} \n Descripcion = {b_articulo[4]} \n Precio : {b_articulo[5]} \n"+
                                f" Existencias : {b_articulo[6]}")
                            break
                        else:
                            print(f"{Fore.YELLOW}Ningun articulo en la categoria seleccionada")
                    else:
                        print(f"{Fore.YELLOW}Ingrese un codigo valido")
                input(f"{Style.DIM}Presione ENTER para regresar! ")
                self.visualizar_articulos_menu()
            if opccion == "3":
                while True:
                    self.limpiar_pantalla()
                    precio = input("Ingrese PRECIO del articulo a buscar : \n").strip()
                    try:
                        if float(precio) > 0:
                            b_articulos = self.gestor.visualizar_articulos("precio" ,precio)
                            if b_articulos != []:
                                for b_articulo in b_articulos:
                                    print(f" Codigo : {b_articulo[2]} \n Categoria : {b_articulo[1]}"+
                                    f"\n Nombre : {b_articulo[3]} \n Descripcion = {b_articulo[4]} \n Precio : {b_articulo[5]} \n"+
                                    f" Existencias : {b_articulo[6]}")
                                break
                            else:
                                print(f"{Fore.YELLOW}Ningun articulo en la categoria seleccionada")
                        else:
                            print(f"{Fore.YELLOW}Ingrese un codigo valido")
                    except ValueError:
                        print(f"{Fore.YELLOW}Ingrese PRECIO del articulo!")
                input(f"{Style.DIM}Presione ENTER para regresar! ")
                self.visualizar_articulos_menu()
            if opccion == "4":
                while True:
                    self.limpiar_pantalla()
                    nombre_ar = input("Ingrese NOMBRE del articulo a buscar : \n").strip()
                    if len(nombre_ar) > 0 and nombre_ar.isalpha():
                        b_articulos = self.gestor.visualizar_articulos("nombre_articulo" ,nombre_ar)
                        if b_articulos != []:
                            for b_articulo in b_articulos:
                                print(f" Codigo : {b_articulo[2]} \n Categoria : {b_articulo[1]}"+
                                f"\n Nombre : {b_articulo[3]} \n Descripcion = {b_articulo[4]} \n Precio : {b_articulo[5]} \n"+
                                f" Existencias : {b_articulo[6]}")
                            break
                        else:
                            print(f"{Fore.YELLOW}Ningun articulo en la categoria seleccionada")
                    else:
                        print(f"{Fore.YELLOW}Ingrese un codigo valido")
                input(f"{Style.DIM}Presione ENTER para regresar! ")
                self.visualizar_articulos_menu()
        if opccion == "5":
                while True:
                    self.limpiar_pantalla()
                    b_articulos = self.gestor.visualizar_total_articulos()
                    if b_articulos != []:
                        for b_articulo in b_articulos:
                            print(f" Codigo : {b_articulo[2]} \n Categoria : {b_articulo[1]}"+
                            f"\n Nombre : {b_articulo[3]} \n Descripcion = {b_articulo[4]} \n Precio : {b_articulo[5]} \n"+
                            f" Existencias : {b_articulo[6]} \n")
                        break
                    else:
                        print(f"{Fore.YELLOW}Ningun articulo EXISTENTE")
                    
                input(f"{Style.DIM}Presione ENTER para regresar! ")
                self.visualizar_articulos_menu()
        if opccion == "6":
                self.menu_principal()

    def modificar_articulo(self):
        self.limpiar_pantalla()
        print("Modificacion de Articulos")
        codigo = input("Ingrese Articulo por CODIGO : \n").strip()
        try:
            if int(codigo) > 0 and len(codigo) < 15:
                articulo = self.gestor.visualizar_articulo(codigo)
                if articulo != ():
                    index = articulo[0]
                    mod_articulo = Articulo(articulo[1],articulo[2],articulo[3],articulo[4],articulo[5],articulo[6])
                    while True:
                        self.limpiar_pantalla()
                        op = input("Ingrese la opcion a modificar : \n1. Categoria \n2. Codigo \n3. Nombre del articulo " +
                        "\n4. Descripcion \n5. Precio \n6.Existencias \n7. Guardar articulo \n")
                        if op in ("1","2","3","4","5","6","7"):
                            if op == "1":
                                self.limpiar_pantalla()
                                mod_articulo.set_categoria(self.gestor_ar.mod_categoria())
                            elif op == "2":
                                self.limpiar_pantalla()
                                mod_articulo.set_codigo(self.gestor_ar.mod_codigo())
                            elif op == "3":
                                self.limpiar_pantalla()
                                mod_articulo.set_nom_producto(self.gestor_ar.mod_nombre())
                            elif op == "4":
                                self.limpiar_pantalla()
                                mod_articulo.set_descripcion(self.gestor_ar.mod_descripcion(9))
                            elif op == "5":
                                mod_articulo.set_precio(self.gestor_ar.mod_precio())
                            elif op == "6":
                                self.limpiar_pantalla()
                                mod_articulo.set_existencia(self.gestor_ar.mod_descripcion())
                            elif op == "7":
                                self.limpiar_pantalla()
                                self.gestor.modificar_articulo(mod_articulo.conv_tupla(), index)
                                break
                    input(f"{Style.DIM}Presione ENTER para regresar ")
                    self.menu_principal()
                else:
                    print(f"{Fore.YELLOW}Ingrese un CODIGO de articulo existente!")
            else:
                print(f"{Fore.YELLOW}Ingrese el CODIGO del articulo correctamente")
        except ValueError:
            print(f"{Fore.YELLOW}Ingrese un CODIGO valido!")

    def eliminar_articulo(self):
        self.limpiar_pantalla()
        print("ELIMINACION de Articulos")
        codigo = input("Ingrese Articulo por CODIGO : \n").strip()
        try:
            if int(codigo) > 0 and len(codigo) < 15:
                articulo = self.gestor.visualizar_articulo(codigo)
                if articulo != ():
                    index = articulo[0]
                    print("El articulo que desea ELIMINAR es el siguiente : ")
                    print(f"Codigo : {articulo[2]} \n Categoria : {articulo[1]}"+
                            f"\n Nombre : {articulo[3]} \n Descripcion = {articulo[4]} \n Precio : {articulo[5]} \n"+
                            f" Existencias : {articulo[6]}")
                    if articulo[6] == 0:
                        validacion = input(f"{Fore.RED}¿Desea Eliminar?    Y/N     \n").strip().upper()
                        if validacion in ("Y","N"):
                            if validacion == "Y":
                                self.gestor.eliminar_articulo(index)
                                input(f"{Style.DIM}Presione ENTER para regresar! ")
                                self.menu_principal()
                            else:
                                input(f"{Style.DIM}Presione ENTER para regresar! ")
                                self.menu_principal()
                    else:
                        print(f"{Fore.BLUE}{Style.DIM}El articulo aun cuenta con existencias, las existencias deben ser 0 para eliminar")
                    input("Presione ENTER para regresar ")
                    self.menu_principal()
                else:
                    print(f"{Fore.YELLOW}Ingrese un CODIGO de articulo existente!")
            else:
                print(f"{Fore.YELLOW}Ingrese el CODIGO del articulo correctamente")
        except ValueError:
            print(f"{Fore.YELLOW}Ingrese un CODIGO valido!")

    def menu_principal(self):
        opcciones_validas = ["1","2","3","4","5"]
        while True:
            self.limpiar_pantalla()
            print("MENU")
            print("1. Registrar nuevo articulo")
            print("2. Lista de articulo")
            print("3. Modificar articulo")
            print("4. Borrar articulo de registro")
            print("5. Salir")
            opccion = input("Seleccione: ")
            if opccion in opcciones_validas:
                if opccion == "1":
                    self.registro_nuevo_producto()
                elif opccion == "2":
                    self.visualizar_articulos_menu()
                elif opccion == "3":
                    self.modificar_articulo()
                elif opccion == "4":
                    self.eliminar_articulo()
                elif opccion == "5":
                    exit()

    def limpiar_pantalla(self):
        if os.name == 'nt':
            _ = os.system('cls')
        else: 
            _ = os.system('clear')

def main():
    sistema = SistemaInventario()
    sistema.menu_principal()

if __name__ == "__main__":
    main()