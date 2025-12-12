# 🏪 Sistema de Gestión de Inventario con PostgreSQL

Un sistema completo de gestión de inventario con interfaz de consola, base de datos PostgreSQL y arquitectura modular para el control de artículos, categorías y existencias.

## 🚀 Características Principales

### 📦 Gestión de Artículos
- **CRUD completo**: Crear, Leer, Actualizar, Eliminar artículos
- **Categorización**: 7 categorías predefinidas con enumeraciones
- **Validación**: Códigos únicos, precios positivos, existencias no negativas
- **Búsqueda avanzada**: Por código, categoría, precio, nombre o ver todos

### 🗄️ Base de Datos
- **PostgreSQL** con conexión segura
- **Creación automática** de base de datos y tablas si no existen
- **Transacciones** con manejo de conexiones
- **Índices únicos** para códigos de artículo
- **Tipos de datos optimizados** (VARCHAR, NUMERIC, INTEGER)

### 🖥️ Interfaz de Usuario
- **Menús interactivos** con limpieza de pantalla
- **Colores y estilos** con Colorama para mejor UX
- **Validación en tiempo real** de entradas
- **Navegación intuitiva** entre módulos

## 🏗️ Arquitectura del Proyecto
sistema_inventario/
├── 📁 Core
│ ├── main.py # Sistema principal y menús
│ ├── articulo.py # Clase Artículo con validaciones
│ ├── cat_enum.py # Enumeración de categorías
│ └── sistema_bd.py # Gestor de base de datos
│
├── 📁 Database
│ └── bd_inventario # Base de datos PostgreSQL
│ └── lista_articulos # Tabla principal

## 🛠️ Tecnologías Utilizadas
- **Python 3.x** con POO avanzada
- **PostgreSQL** como motor de base de datos
- **Psycopg2** para conexión Python-PostgreSQL
- **Colorama** para interfaz colorida
- **Enums** para categorías predefinidas
- **SQL Injection Protection** con parámetros parametrizados

## 🏃‍♂️ Instalación y Configuración
pip install psycopg2-binary colorama
# En sistema_bd.py, modificar según tu configuración:
self.host = "localhost"
self.user = "postgres"
self.passw = "tu_contraseña"
self.port = "5432"
### 1. Requisitos Previos
```bash
# Instalar PostgreSQL
# https://www.postgresql.org/download/

# Crear usuario y contraseña (modificar en sistema_bd.py)
# Usuario: postgres
# Contraseña: admin123

### 4. Ejecutar el Sistema
python main.py

🎯 Lo que Aprendí
Conceptos Avanzados

    Conexión a bases de datos relacionales con PostgreSQL

    Psycopg2 para operaciones CRUD seguras

    Enumeraciones en Python para categorías predefinidas

    Validación de datos en múltiples niveles

    Manejo de conexiones con apertura/cierre adecuado

Patrones de Diseño

    Data Access Object (DAO) con GestorBD

    Model-View-Controller (MVC) implícito

    Singleton pattern para gestión de conexiones

    Factory pattern para creación de artículos

Seguridad y Buenas Prácticas

    Prevención de SQL Injection con parámetros parametrizados

    Manejo de excepciones en operaciones de base de datos

    Validación de entrada del usuario

    Cierre seguro de conexiones y cursores

🔧 Características Técnicas Destacadas
Sistema de Categorías

# Enumeración type-safe
class Categorias(Enum):
    LACTEOS = 1
    CONGELADOS = 2
    MERCADO = 3
    # ... 7 categorías totales

Gestión de Conexiones

# Apertura y cierre seguro
def _abrir_conexion_(self):
    conexion = psycopg2.connect(...)
    conexion.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    return conexion, conexion.cursor()

Validación Completa

    Código único de 15 caracteres máximo

    Precio positivo con decimales

    Existencias no negativas

    Nombre no vacío (1-100 caracteres)

🔮 Próximas Mejoras

    Interfaz web con FastAPI/Flask

    Sistema de usuarios con roles

    Backup automático de base de datos

    API REST para integraciones

    Dashboard con gráficos de existencias

📊 Diagrama de Flujo

Usuario → Menú Principal → Opción → Validación → Base de Datos → Resultado
     ↑           ↓                                            ↓
     ←------- Navegación ←-------- Mensaje ←-----------------←
