import psycopg2
from psycopg2 import OperationalError, DatabaseError, sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT



class GestorBD:

    def __init__(self):
        self.user = "postgres"
        self.pasw = "admin123"
        self.host = "localhost"
        self.port = "5432"

        self.db_nombre = "sis_tareas_db"
        self.db_tabla = "lista_tareas"

        self.c_query = sql.SQL("CREATE DATABASE {};").format(sql.Identifier(self.db_nombre))

        self.ini_base()

    def ini_base(self):
        try:
            conexion = psycopg2.connect(
                user=self.user,
                password=self.pasw,
                host=self.host,
                port=self.port
            )
            with conexion:
                with conexion.cursor() as cur:
                    consulta = sql.SQL("SELECT datname FROM pg_database;")
                    cur.execute(consulta)
                    bases = cur.fetchall()
                    print(bases)
                    for bd in bases:
                        if bd[0] == self.db_nombre:
                            print("BASE DE DATOS ENCONTRADA!")
                            break
                    else:
                        self._usar_conexion_(self.c_query)
                        self.ini_tabla()
                        print("BASE DE DATOS NO ENCONTRADA Y CREADA!")
        except:
            pass

    def ini_tabla(self):
        tabla_db = (self.n_tabla,)
        consulta = sql.SQL("SELECT EXISTS (SELECT FROM pg_tables WHERE tablename = %s);")
        validacion = self._uso_conexion_retorno_(consulta, tabla_db)
        if validacion == [] or validacion == () or validacion == None:
            consulta = sql.SQL("CREATE TABLE lista_tareas(indice SERIAL PRIMARY KEY, " +
            "titulo VARCHAR(30) NOT NULL, " +
            "descripcion TEXT, " +
            "categoria VARCHAR(15) NOT NULL, " +
            "recordatorio BOOLEAN DEFAULT FALSE, " +
            "fecha DATE NOT NULL, " +
            "horario TIME NOT NULL);") 
            self._usar_conexion_(consulta)

    def _uso_conexion_(self, consulta, dat = None):

        try:
            conexion = psycopg2.connect(
                dbname=self.db_nombre,
                user=self.user,
                password=self.pasw,
                host=self.host,
                port=self.port
            )
            with conexion:
                with conexion.cursor() as cur:
                    if dat == None:
                        cur.execute(consulta)
                    else:
                        cur.execute(consulta, dat)

        except (DatabaseError, OperationalError, Exception) as e:
            print(e)

    def _uso_conexion_retorno_(self, consulta, dat = None):

        try:
            conexion = psycopg2.connect(
                dbname=self.db_nombre,
                user=self.user,
                password=self.pasw,
                host=self.host,
                port=self.port
            )
            with conexion:
                with conexion.cursor() as cur:
                    if dat == None:
                        cur.execute(consulta)
                        r_tupla = cur.fetchall()
                        print(r_tupla)
                        return r_tupla
                    else:
                        cur.execute(consulta, dat)
                        r_tupla = cur.fetchall()
                        print(r_tupla)
                        return r_tupla

        except (DatabaseError, OperationalError, Exception) as e:
            print(e)

    def db_crear_tarea(self, valores_tupla):
        consulta = sql.SQL("INSERT INTO lista_tareas(titulo,descripcion,categoria,"+
        "recordatorio,fecha,horario) VALUES (%s,%s,%s,%s,%s,%s)")
        self._uso_conexion_(consulta,valores_tupla)

    def db_consultar_tareas(self, filtro): # Mandar tupla en filtro =  (filtro , valor)
        consulta = sql.SQL("SELECT * FROM lista_tareas WHERE %s = %s")
        self._uso_conexion_(consulta, filtro)

    