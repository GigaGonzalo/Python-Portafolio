
from cat_enum import Categorias
from sistema_bd import GestorBD
import colorama
from colorama import Fore, Style, init

init(autoreset=True)

gestor = GestorBD()

class Articulo:

    def __init__(self, categoria = Categorias.SIN_CATEGORIA, codigo = 0, n_articulo = "sin nombre", des = "sin descripcion",
    precio = 0.0, existencia = 0):
        self.categoria = categoria
        self.codigo = codigo
        self.nombre_producto = n_articulo
        self.descripcion = des
        self.precio = precio
        self.existencias = existencia

    def set_categoria(self, cat:str):
        self.categoria = cat
        
    def set_codigo(self,codigo:str):
        self.codigo = codigo
    
    def set_nom_producto(self, n_articulo:str):
        self.nombre_producto = n_articulo
    
    def set_descripcion(self, desc:str):
        self.descripcion = desc
        
    def set_precio(self, precio:float):
        self.precio = precio
        
    def set_existencia(self, exis:int):
        self.existencias = exis
        
    @property
    def get_categoria(self) -> str:
        return self.categoria

    @property
    def get_codigo(self)-> str:
        return self.codigo
    
    @property
    def get_nom_producto(self)-> str:
        return self.nombre_producto
    
    @property
    def get_descripcion(self)-> str:
        return self.descripcion
    
    @property
    def get_precio(self)-> float:
        return self.precio

    @property
    def get_existencia(self)-> int:
        return self.existencias

    def conv_tupla(self)-> tuple:
        tupla_obj = (
            self.categoria ,
            self.codigo ,
            self.nombre_producto ,
            self.descripcion , 
            self.precio , 
            self.existencias
        )
        return tupla_obj

class GestorArticulo():
    def mod_categoria(self):
        while True:
            print(f"Ingrese la categoria del articulo : \n1. {Categorias.LACTEOS.name} \n2. {Categorias.CONGELADOS.name} \n3. {Categorias.MERCADO.name}" +
            f"\n4. {Categorias.ABARROTES.name} \n5. {Categorias.ROPA.name} \n6. {Categorias.HOGAR.name} \n7. {Categorias.ELECTRONICA.name}")
            categoria = input("Ingrese la CATEGORIA a la que pertenece :").strip()
            if categoria in ("1","2","3","4","5","6","7"):
                categoria = int(categoria)
                return Categorias(categoria).name
            else:
                print(f"{Back.YELLOW}Ingrese una categoria VALIDA!")

    def mod_codigo(self):
        while True:
            codigo = input("Ingrese el CODIGO UNICO del articulo :").strip()
            if len(codigo) <= 15 and codigo.isdecimal():
                if gestor.validador(codigo):
                    return codigo
                else:
                    print(f"{Back.YELLOW}Validar! Codigo ya existente")
            else:
                print(f"{Back.YELLOW}Ingrese un codigo valido")

    def mod_nombre(self):
        while True:
            nombre_ar = input("Ingrese el NOMBRE del articulo :")
            if len(nombre_ar) > 0  and len(nombre_ar) <= 100 :
                return nombre_ar
            else:
                print(f"{Back.YELLOW}Ingrese un nombre de articulo valido! No puede ser un campo VACIO!")
        
    def mod_descripcion(self):
        while True:
            descripcion = input("Ingrese DESCRIPCION del articulo :")
            return descripcion
    def mod_precio(self):
        while True:
            precio = input("Ingrese el PRECIO UNITARIO del articulo:").strip()
            try:
                precio = float(precio)
                if precio > 0:
                    return precio
                else:
                    print(f"{Back.YELLOW}Ingrese un valor(precio) mayor a 0")
            except ValueError:
                print(f"{Back.YELLOW}Ingrese una cantidad numerica para el valor")
    
    def mod_existencias(self):
        while True:
            existencia = input("Ingrese las EXISTENCIAS del articulo :").strip()
            try:
                existencia = int(existencia)
                if existencia >= 0:
                    return existencia
                else:
                    print(f"{Back.YELLOW}Ingrese un valor(existencias) mayor a 0")
            except ValueError:
                print(f"{Back.YELLOW}Ingrese una cantidad numerica para el valor")