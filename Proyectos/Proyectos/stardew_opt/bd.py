import psycopg2
from psycopg2 import OperationalError
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2 import sql


class GestorBD():

    def construir_bd(self):

        try:

            conexion = psycopg2.connect(
                user="postgres" ,
                password= "admin123" ,
                host= "localhost" ,
                port= "5432"
            )

            conexion.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

            cur = conexion.cursor()

            consulta = sql.SQL("CREATE TABLE ")

        except (OperationalError, Exception) as e:
            print(f"Error en construccion: {e}")

    def verificar_bd(self):
        try:

            conexion = psycopg2.connect(
                user="postgres" ,
                password="admin123" ,
                host="localhost" ,
                port="5432"
            )
            conexion.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cur = conexion.cursor()

            consulta = sql.SQL("SELECT datname FROM pg_database;")

            cur.execute(consulta)

            bds = cur.fetchall()

            for base in bds:
                if base[0] == "stardew_bd":
                    break
                else:
                    self.crear_bd()
                    break
                    
            cur.close()
            conexion.close()

        except (psycopg2.OperationalError, Exception) as e:
            print(f"Error en verificar: {e}")    

    def crear_bd(self):

        try:

            conexion = psycopg2.connect(
                user="postgres" ,
                password="admin123" ,
                host="localhost" ,
                port="5432"
            )
            conexion.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cur = conexion.cursor()
            consulta = sql.SQL("CREATE DATABASE {}").format(sql.Identifier("stardew_bd"))
            cur.execute(consulta)
            cur.close()
            conexion.close()
            print("Base de Datos CREADA!! ")
        except (psycopg2.OperationalError, Exception) as e:
            print(f"Error en crear: {e}")

    

gbd = GestorBD()

gbd.verificar_bd()