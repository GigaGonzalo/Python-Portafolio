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
        
    def _usar_conexion_(self, consulta , datos_tupla = None, retorno = False):
        if datos_tupla == None:
            datos_tupla = ()

        try:
            conexion = psycopg2.connect(
                dbname=self.nombre_bd ,
                host=self.host ,
                user=self.user ,
                password= self.passw ,
                port= self.port
                )
            conexion.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            with conexion:
                with conexion.cursor() as cur:
                    if datos_tupla != () and retorno == True:
                        cur.execute(consulta, datos_tupla)
                        articulos = cur.fetchall()
                        return articulos
                    elif datos_tupla != () and retorno == False:
                        cur.execute(consulta, datos_tupla)
                        return True
                    else:
                        cur.execute(consulta)
                        articulos = cur.fetchall()
                        return articulos
        except (psycopg2.DatabaseError, Exception) as e:
            print(f"Error en la Base de Datos {e}")
        finally:
            if conexion:
                conexion.close()

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
        consulta = sql.SQL("INSERT INTO lista_articulos(categoria, codigo, nombre_articulo, descripccion ," +
        "precio , existencias)" + " VALUES(%s,%s,%s,%s,%s,%s);")
        confirmacion = self._usar_conexion_(consulta, n_articulo , False)
        if confirmacion:
            print(f"{Fore.GREEN}{Style.DIM}ARTICULO AGREGADO CORRECTAMENTE!")

    def modificar_articulo(self, n_valores, indice):
            n_v = (n_valores[0],n_valores[1],n_valores[2],n_valores[3],n_valores[4],n_valores[5],indice)
            consulta = sql.SQL("UPDATE lista_articulos SET categoria = %s , codigo = %s ,"+
            "nombre_articulo = %s , descripccion = %s , precio = %s , existencias = %s WHERE indice = %s;")
            confirmacion = self._usar_conexion_(consulta , n_v , False)
            if confirmacion:
                print(f"{Fore.GREEN}{Style.DIM}ARTICULO ACTUALIZADO!")

    def visualizar_articulo(self, index):
        consulta = sql.SQL("SELECT * FROM lista_articulos WHERE codigo = %s;")
        t_index = (index,)
        articulo = self._usar_conexion_(consulta,t_index,True)
        if articulo != []:
            return articulo[0]
        else:
            return []

    def visualizar_articulos(self, param , valor):
        
        if param in ("precio", "existencias"):
            consulta = sql.SQL("SELECT * FROM lista_articulos WHERE {} = %s;").format(sql.Identifier(param))
            t_valor = (float(valor) if param == "precio" else int(valor),)
            print(t_valor)
            articulos = self._usar_conexion_(consulta,t_valor,True)
        else:
            valor = '%'+str(valor)+'%'
            consulta = sql.SQL("SELECT * FROM lista_articulos WHERE {} LIKE %s;").format(sql.Identifier(param))
            t_valor = (valor,)
            articulos = self._usar_conexion_(consulta , t_valor, True)
        print(articulos)
        if articulos != []:
            return articulos
        else:
            return []
        
    def visualizar_total_articulos(self):
        
        consulta = sql.SQL("SELECT * FROM lista_articulos;")
        articulos = self._usar_conexion_(consulta, None , True)
        if articulos != []:
            return articulos
        else:
            return []

    def eliminar_articulo(self, index):
            consulta = sql.SQL("DELETE FROM lista_articulos WHERE indice = %s;")
            confirmacion = self._usar_conexion_(consulta, (index,),False)
            if confirmacion:
                print(f"{Fore.RED}{Style.DIM}ARTICULO CORRECTAMENTE ELIMINADO")

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


