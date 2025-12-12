import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def crear_tabla_db():

    try:
        connection = psycopg2.connect( 
        host="localhost",
        user= "postgres",
        password="admin123",
        port= 5432
        )

        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        cur = connection.cursor()
        nom_tab = "articulos"
        consulta = sql.SQL("CREATE TABLE IF NOT EXISTS articulos (indice SERIAL PRIMARY KEY, " +
        "codigo VARCHAR(50) UNIQUE NOT NULL, " +
        "nombre_articulo VARCHAR(100) NOT NULL, " +
        "descripccion TEXT, " +
        "existencias INTEGER NOT NULL, "+
        "precio NUMERIC(10,2) NOT NULL, "+ 
        "caducidad DATE" +
        ");" )

        cur.execute(consulta)
    finally:

        if "cursor" in locals():
            cursor.close()
        if "consulta" in locals():
            connection.close()



def create_db():
    try:
        connection = psycopg2.connect( 
        host="localhost",
        user= "postgres",
        password="admin123",
        port= 5432
        )
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        cursor = connection.cursor()

        name_db = "Mi primer DB"

        consulta = sql.SQL("CREATE DATABASE {}").format(sql.Identifier(name_db))

        cursor.execute(consulta)

        print("Base de datos creada!")

    finally:

        if "cursor" in locals():
            cursor.close()
        if "consulta" in locals():
            connection.close()

def verificar_tabla():
    try:
        conexion = psycopg2.connect(
            host= "localhost",
            user= "postgres",
            password= "admin123",
            port= "5432"
        )
        conexion.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conexion.cursor()
        consulta = sql.SQL("SELECT * FROM articulos")
        cur.execute(consulta)
        lista_articulos = cur.fetchall()
        print("ARTICULOS EN LA BASE DE DATOS")
        for articulo in lista_articulos:
            print(f"{articulo}")

    finally:

        if "cursor" in locals():
            cursor.close()
        if "consulta" in locals():
            conexion.close()

def insertar_dato_bd():
    try:
        conexion = psycopg2.connect(
            host="localhost", 
            user="postgres",
            password="admin123",
            port="5432"
        )
        conexion.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conexion.cursor()
        nuevo_articulo = (1, 1 , "papel higienico", "papel para ir al baño", 5 , 15.50 , "10-10-2026")
        consulta = sql.SQL("INSERT INTO articulos(indice, codigo, nombre_articulo, descripccion, existencias, precio, caducidad) "+
        "VALUES(%s, %s, %s, %s, %s, %s, %s);")
        cur.execute(consulta, nuevo_articulo)
    except psycopg2.Error as e:
        print(f"{e}")

def verificar_db():

    try:
        conexion = psycopg2.connect(
            host= "localhost",
            user= "postgres",
            password= "admin123",
            port= "5432"
        )

        conexion.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        cursor = conexion.cursor()

        cursor.execute("SELECT datname FROM pg_database;")
        bases_datos = cursor.fetchall()

        print("BASES DE DATOS")

        for bd in bases_datos:
            print(f"{bd[0]}")
    except psycopg2.Error as e:
        print(f"{e}")

def modificar_articulo():
    try:
        conexion = psycopg2.connect(
            host="localhost",
            user = "postgres",
            password= "admin123",
            port= "5432"
        )
        conexion.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conexion.cursor()
        actualizacion = (12 , 8)
        consulta = sql.SQL("UPDATE articulos SET precio = %s, existencias = %s WHERE indice = 1")
        cur.execute(consulta, actualizacion)
    except psycopg2.Error as e:
        print(f"{e}")

def eliminar_articulo():
    try:
        conexion = psycopg2.connect(
            host="localhost",
            user = "postgres",
            password= "admin123",
            port= "5432"
        )
        conexion.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conexion.cursor()
        consulta = sql.SQL("DELETE FROM articulos WHERE indice = 1")
        cur.execute(consulta)
    except psycopg2.Error as e:
        print(f"{e}")

#create_db()
verificar_db()
#crear_tabla_db()
verificar_tabla()
#insertar_dato_bd()
modificar_articulo()
verificar_tabla()
eliminar_articulo()
verificar_tabla()
