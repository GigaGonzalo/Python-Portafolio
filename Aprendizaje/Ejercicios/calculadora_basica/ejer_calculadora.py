#**********************************************************************************************#
#**********************************************************************************************#
#**********************************************************************************************#
#**********************************************************************************************#
#**********************************************************************************************#
import os
import json

EXTERNAL = "calculadora_historial.json"

def vaciar_historial():
    """
    Verifica si el archivo de historial existe para su eliminacion
        
    """ 
    if os.path.exists(EXTERNAL):
        os.remove(os.path.abspath(EXTERNAL))
    else:
        pass

def extraer_historial_externo():
    """
    Devuelve el archivo JSON en formato de lista con el historial

    Returns:
        Lista con el historial
        
    Raises:
        JSONDecodeError: Si el archivo no se puede cargar
    """ 
    try:
        if os.path.exists(EXTERNAL):
            with open(EXTERNAL, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        else:
            return []
    except (json.JSONDecodeError, Exception) as e:
        print(f"{e}")

def guardar_historial_externo(historial : str, index : int):
    """
    Almacena las cadenas de caracteres del historial en el indice correspondiente
    
    Args:
        historial   :   String de la operacion a almacenar
        index       :   Indice correspondiente del historial

    Raises:
        IndexError: Si el indice del historial aun no existe
        JSONDecodeEror: Si el archivo no se puede guardar
    """ 
    historial_ext = extraer_historial_externo()
    try: 
        historial_ext[index] += historial
    except IndexError:
        historial_ext.append(historial)
    
    try:
        with open(EXTERNAL, "w", encoding="utf-8") as archivo:
            print(historial_ext)
            json.dump(historial_ext, archivo, ensure_ascii=False, indent=2)

    except (json.JSONDecodeError, Exception) as e:
        print(f"{e}")


def peticion_de_valor(total_ : float, operacion : str) -> str:
    """
    Solicita el valor para la operacion al usuario
    
    Args:
        total_ : float        Total de la operacion en curso
        operacion : str       Operador a realizar 
        
    Returns:
        Valor ingresado, en caso de alfabeto, en minusculas
    """
    while True:
        print(f"Ingrese el valor numerico {operacion}:         Total = {total_} ")
        x = input().lower()
        try:
            x = float(x)
            return x
        except ValueError:
            print("INGRESE SOLO VALORES NUMERICOS!")

def peticion_de_operacion(total_ : float) -> str:
    """
    Solicita al usuario el siguiente operador
    
    Args:
        total_ : float      Total de la operacion en curso
        
    Returns:
        Operador valido
    """
    opciones = ["+", "-", "*", "/", "x"]
    while True:
        print(f"Total = {total_}")
        opcion = input("Ingrese signo de operacion   \n+ Suma   \n- Resta   "
                       +"\n* Multiplicacion  \n/ Division   \nx Salir\n").lower()
        if opcion in opciones:
            return opcion
        else:
            print("Ingrese un signo de operacion valido! ")

def menu_operaciones(formato, pos_his : int, total_ : float):
    """
    Menu encargado de realizar la siguiente operacion basado en el operador ingresado
    
    Args:
        formato     : int         Indicador del formato a guardar
        pos_his     : int         Posicion de la operacion en el historial
        total_      : float       Total de la operacion en curso
    """
    
    while True:

        try:

            operacion = peticion_de_operacion(total_)

            if operacion == "+":
                x = peticion_de_valor(total_, "a SUMAR ")
                total_ += x
                guardar_historial(formato, pos_his, " + ", x, total_)
            elif operacion == "-":
                x = peticion_de_valor(total_, "a RESTAR ")
                total_ -= x
                guardar_historial(formato, pos_his," - ", x, total_)
            elif operacion == "*":
                x = peticion_de_valor(total_, "a MULTIPLICAR ")
                total_ *= x
                guardar_historial(formato, pos_his," * ", x, total_)
            elif operacion == "/":
                x = peticion_de_valor(total_, "a DIVIDIR ")
                total_ /= x
                guardar_historial(formato, pos_his," / ", x, total_)
            elif operacion == "x":
                menu_principal()

        except ValueError:
            print("INGRESE UN NUMERO PARA LA OPERACION")
        except ZeroDivisionError:
            print("El divisor no puede ser igual a 0")

def guardar_historial(formato : int, posicion_historial : int, operador : str, valor : float, resultado : float):
    """
    Almacena la operacion en el historial de la sesion usando la variable mutable - historial
    
    Args:
        formato            : int    Indicador del formato
        posicion_historial : int    Posicion de la operacion en el historial
        operador           : str    Operador de la operacion
        valor              : float  Valor que se aplico en la operacion
        resultado          : float  Total de la operacion realizada
    """
    if formato == 0:
        operacion =  str(resultado) + " "
        guardar_historial_externo(operacion, posicion_historial)
    elif formato == 1:
        operacion =  operador + str(valor) + " = " + str(resultado) + " "
        guardar_historial_externo(operacion , posicion_historial)
        

def nueva_operacion(index):
    """
    Inicia una nueva operacion de la calculadora

    """
    total_ = 0.0
    while True:
        try:
            x = peticion_de_valor(total_, "a OPERAR ")
            total_ += float(x)
            guardar_historial(0, index, "" , "", total_ )
            menu_operaciones(1, index, total_)
            
        except ValueError:
            print("INGRESE UN NUMERO PARA LA OPERACION")

def visualizar_historial(historial : list):
    """
    Devuelve en pantalla el historial de operaciones de la sesion
    
    Args:
        historial : list    Historial de la sesion actual
    """
    if len(historial) != 0:
        print(len(historial))
        for i in historial:
            print(i)
    else:
        print("No hay datos en el historial ", len(historial))

    input("Presione enter para regresar al menu ")
    menu_principal()

def menu_principal():
    """
    Menu principal donde el usuario elige su accion

    """
    historial = extraer_historial_externo()
    opciones = ["1", "2", "3"]
    print(" "*10 + " Calculadora " + " "*10)
    print("Seleccione una de las siguientes opciones : " + 
        "\n1. Nueva operacion" +
        "\n2. Ver historial de operaciones" + 
        "\n3. Salir")
    opcion = input("Seleccione : ")
    if opcion in opciones:
        if opcion == "1":
            nueva_operacion(len(historial))
        elif opcion == "2":
            visualizar_historial(historial)
        elif opcion == "3":
            vaciar_historial()
            exit()

def main():
    """
    Ejecucion post-validacion

    """
    vaciar_historial()
    menu_principal()
    

if __name__ == "__main__":
    """
    Validacion para ejecucion

    """
    main()
    
