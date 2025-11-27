# ✅ Sistema de Gestión de Tareas en Python

Un sistema completo de gestión de tareas con categorías, niveles de importancia, recordatorios y persistencia de datos en JSON.

## 🚀 Características Principales
- **📝 Creación y edición de tareas** con categorías personalizadas
- **🎯 Sistema de importancia** (Bajo, Medio, Alto)
- **⏰ Recordatorios con fechas y horas** específicas
- **💾 Persistencia de datos** en archivo JSON
- **🎨 Interfaz colorida** con Colorama
- **📊 Categorización** (Hogar, Escuela, Trabajo)
- **✏️ Modificación y eliminación** de tareas existentes

## 🏗️ Arquitectura del Proyecto

sistema_tareas/
├── sistema_tareas.py # Lógica principal y menús
├── tareas.py # Clase Tarea con propiedades
├── historial_tareas.py # Manejo de persistencia JSON
├── enumeraciones.py # Enums para categorías e importancia
└── historial_tareas.json # Base de datos de tareas

## 🛠️ Tecnologías Utilizadas
- **Python 3.x** con POO
- **JSON** para persistencia de datos
- **Colorama** para interfaz colorida
- **Enum** para categorías predefinidas
- **Datetime** para manejo de fechas

## 🏃‍♂️ Instalación y Ejecución
```bash
# Instalar dependencias
pip install colorama

# Ejecutar el sistema
python sistema_tareas.py