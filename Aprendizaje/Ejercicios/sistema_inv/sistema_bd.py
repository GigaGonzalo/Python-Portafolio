import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2 import sql
import colorama
from colorama import Fore, Style, init
init(autoreset=True)
class GestorBD():

    def __init__(self):
        self.host = "localhost"
        self.user = "postgres"
        self.passw = "admin123"
        self.port = "5432"

        self.nombre_bd = "bd_inventario"
        self.c_creacion = sql.SQL("CREATE DATABASE {}").format(sql.Identifier(self.nombre_bd))
        

    def _abrir_conexion_(self):
        try:
            conexion = psycopg2.connect(
                dbname=self.nombre_bd ,
                host=self.host ,
                user=self.user ,
                password= self.passw ,
                port= self.port
            )
            conexion.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cur= conexion.cursor()
            return conexion , cur
        except Exception as e:
            print(f"{Fore.RED}Error al abrir conexion {e}")

    def _cerrar_conexion_(self, con , cur):
        
        if cur:
            try:
                cur.close()
                #print("Exito al cerrar CURSOR")
            except Exception as e:
                print(f"{Fore.RED}Error al cerrar cursor {e}")

        if con:
            try:
                con.close()
                #print("Exito al cerrar CONEXION")
            except Exception as e:
                print(f"{Fore.RED}Error al cerrar conexion {e}")

    def insertar_nuevo_articulo_bd(self, n_articulo):
        conexion , cur = self._abrir_conexion_()
        try:
            consulta = sql.SQL("INSERT INTO lista_articulos(categoria, codigo, nombre_articulo, descripccion ," +
            "precio , existencias)" + " VALUES(%s,%s,%s,%s,%s,%s);")
            cur.execute(consulta, n_articulo)
            print(f"{Fore.GREEN}{Style.DIM}ARTICULO AGREGADO CORRECTAMENTE!")
            self._cerrar_conexion_(conexion, cur)
        except Exception as e:
            print(f"{Fore.RED}Error al cargar nuevo articulo {e}")

    def modificar_articulo(self, n_valores, indice):
        conexion , cur = self._abrir_conexion_()
        try:
            n_v = (n_valores[0],n_valores[1],n_valores[2],n_valores[3],n_valores[4],n_valores[5],indice)
            consulta = sql.SQL("UPDATE lista_articulos SET categoria = %s , codigo = %s ,"+
            "nombre_articulo = %s , descripccion = %s , precio = %s , existencias = %s WHERE indice = %s;")
            cur.execute(consulta,n_v)
            print(f"{Fore.GREEN}{Style.DIM}ARTICULO ACTUALIZADO!")
            self._cerrar_conexion_(conexion, cur)
        except Exception as e:
            print(f"{Fore.RED}Error al actualizar el articulo {e}")

    def visualizar_articulo(self, index):
        try:
            conexion, cur = self._abrir_conexion_()
            consulta = sql.SQL("SELECT * FROM lista_articulos WHERE codigo = %s;")
            cur.execute(consulta, (index,))
            articulo = cur.fetchall()
            if articulo != []:
                return articulo[0]
            else:
                return []
            
        except Exception as e:
            print(f"{Fore.RED}Error al extraer datos del articulo N. {index} , {e}")

    def visualizar_articulos(self, param , valor):
        try:
            valor = '%'+valor+'%'
            print(valor)
            conexion, cur = self._abrir_conexion_()
            consulta = sql.SQL("SELECT * FROM lista_articulos WHERE " + param + " LIKE %s;")
            cur.execute(consulta, (valor,))
            articulos = cur.fetchall()
            if articulos != []:
                return articulos
            else:
                return []
            
        except Exception as e:
            print(f"{Fore.RED}Error al extraer datos del articulo , {e}")

    def visualizar_total_articulos(self):
        try:
            conexion, cur = self._abrir_conexion_()
            consulta = sql.SQL("SELECT * FROM lista_articulos;")
            cur.execute(consulta)
            articulos = cur.fetchall()
            if articulos != []:
                return articulos
            else:
                return []
            
        except Exception as e:
            print(f"{Fore.RED}Error al extraer datos del articulo N. {index} , {e}")

    def eliminar_articulo(self, index):
        try:
            conexion , cur = self._abrir_conexion_()
            consulta = sql.SQL("DELETE FROM lista_articulos WHERE indice = %s;")
            cur.execute(consulta, (index,))
            print(f"{Fore.RED}{Style.DIM}ARTICULO CORRECTAMENTE ELIMINADO")
            self._cerrar_conexion_(conexion, cur)
        except Exception as e:
            print(f"{Fore.RED}Error al eliminar articulo N. {index} , {e}")

    def verificar_db(self):
        try:
            conexion , cur = self._abrir_conexion_()
            consulta = sql.SQL("SELECT datname FROM pg_database;")
            cur.execute(consulta)
            bases = cur.fetchall()
            for bd in bases:
                if bd[0] == self.nombre_bd:
                    self._cerrar_conexion_(conexion, cur)
                    print(f"{Fore.GREEN}{Style.DIM}BASE DE DATOS ENCONTRADA!")
                    break
            else:
                cur.execute(self.c_creacion)
                self.crear_tabla_articulos()
                print(f"{Fore.YELLOW}{Style.DIM}BASE DE DATOS NO ENCONTRADA Y CREADA!")
        except Exception as e:
            print(f"{Fore.RED}ERROR AL BUSCAR BASE DE DATOS EXISTENTE!!!")

    def crear_tabla_articulos(self):
        try:
            conexion , cur = self._abrir_conexion_()
            consulta = sql.SQL("CREATE TABLE lista_articulos(indice SERIAL PRIMARY KEY, " +
            "categoria VARCHAR(20) NOT NULL, " +
            "codigo VARCHAR(15) UNIQUE NOT NULL, " +
            "nombre_articulo VARCHAR(100) NOT NULL, " +
            "descripccion TEXT, " +
            "precio NUMERIC(10,2) NOT NULL, " +
            "existencias INTEGER NOT NULL);")
            cur.execute(consulta)
            print(f"{Fore.GREEN}TABLA CREADA EXITOSAMENTE")
            self._cerrar_conexion_(conexion, cur)
        except Exception as e:
            print(f"{Fore.RED}ERROR AL CREAR TABLA DE ARTICULOS , {e}")

    def validador(self, valor):
        try:
            conexion, cur = self._abrir_conexion_()
            consulta = sql.SQL("SELECT * FROM lista_articulos WHERE codigo = %s")
            cur.execute(consulta, (valor,))
            lista = cur.fetchall()
            if lista == () or lista == []:
                print(f"{Fore.YELLOW}Sin articulos existentes con los valores ingresados")
                self._cerrar_conexion_(conexion,cur)
                return True
            else:
                print(f"{Fore.YELLOW}Articulo duplicado")
                self._cerrar_conexion_(conexion,cur)
                return False
            self._cerrar_conexion_(conexion,cur)
        except Exception as e:
            print(f"{Fore.RED}Error al comprobar en la base de datos , {e}")


