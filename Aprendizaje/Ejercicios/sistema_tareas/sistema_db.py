import psycopg2
from psycopg2 import OperationalError, DatabaseError, sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class GestorBD:

    def __init__():
        self.user = "postgres"
        self.pasw = "admin123"
        self.host = "localhost"
        self.port = "5432"

        self.db_nombre = "sis_tareas_db"

        self.c_query = sql.SQL("CREATE DATABASE {};").format(sql.Identifier(self.db_nombre))

    def _uso_conexion_(self):

        try:
            conexion = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.pasw,
                host=self.host,
                port=self.port
            )
            with conexion:
                with conexion.cursor() as cur:
                    pass

        except (DatabaseError, OperationalError, Exception) as e:
            print(e)
