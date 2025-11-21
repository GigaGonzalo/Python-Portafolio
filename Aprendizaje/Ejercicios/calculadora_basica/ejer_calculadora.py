#**********************************************************************************************#
#**********************************************************************************************#
#**********************************************************************************************#
#**********************************************************************************************#
#**********************************************************************************************#

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

def menu_operaciones(pos_his : int, total_ : float, historial_proceso : list):
    """
    Menu encargado de realizar la siguiente operacion basado en el operador ingresado
    
    Args:
        operacion : str         Operador de la siguiente operacion
        pos_his   : int         Posicion de la operacion en el historial
        total_    : float       Total de la operacion en curso
    """
    while True:
        try:
            operacion = peticion_de_operacion(total_)
            if operacion == "+":
                x = peticion_de_valor(total_, "a SUMAR ")
                total_ += x
                historial_proceso = guardar_historial(pos_his, " + ", x, total_)
            elif operacion == "-":
                x = peticion_de_valor(total_, "a RESTAR ")
                total_ -= x
                historial_proceso = guardar_historial(pos_his," - ", x, total_)
            elif operacion == "*":
                x = peticion_de_valor(total_, "a MULTIPLICAR ")
                total_ *= x
                historial_proceso = guardar_historial(pos_his," * ", x, total_)
            elif operacion == "/":
                x = peticion_de_valor(total_, "a DIVIDIR ")
                total_ /= x
                historial_proceso = guardar_historial(pos_his," / ", x, total_)
            elif operacion == "x":
                menu_principal(historial_proceso)
        except ValueError:
            print("INGRESE UN NUMERO PARA LA OPERACION")
        except ZeroDivisionError:
            print("El divisor no puede ser igual a 0")

def guardar_historial(posicion_historial : int, operador : str, valor : float, resultado : float, historial = []):
    """
    Almacena la operacion en el historial de la sesion usando la variable mutable - historial
    
    Args:
        posicion_historial : int    Posicion de la operacion en el historial
        operador           : str    Operador de la operacion
        valor              : float  Valor que se aplico en la operacion
        resultado          : float  Total de la operacion realizada
        historial          : list   Almacena el historial
    """
    
    if len(historial) == posicion_historial:
        operacion =  str(resultado) + " "
        historial.append(operacion)
    else:
        operacion =  operador + str(valor) + " = " + str(resultado) + " "
        print(historial)
        historial[posicion_historial] += operacion
        print(historial)
    return historial

def nueva_operacion(historial_menu : list):
    """
    Inicia una nueva operacion de la calculadora

    """
    historial = historial_menu
    total_ = 0.0
    pos_his = len(historial)
    while True:
        try:
            x = peticion_de_valor(total_, "a OPERAR ")
            total_ += float(x)
            historial = guardar_historial(pos_his, "" , "", total_ )
            menu_operaciones(pos_his, total_, historial)
            
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
    menu_principal([])

def menu_principal(historial_actual : list):
    """
    Menu principal donde el usuario elige su accion

    """
    historial = historial_actual
    opciones = ["1", "2", "3"]
    print(" "*10 + " Calculadora " + " "*10)
    print("Seleccione una de las siguientes opciones : " + 
        "\n1. Nueva operacion" +
        "\n2. Ver historial de operaciones" + 
        "\n3. Salir")
    opcion = input("Seleccione : ")
    if opcion in opciones:
        if opcion == "1":
            nueva_operacion(historial)
        elif opcion == "2":
            visualizar_historial(historial)
        elif opcion == "3":
            exit()

def main():
    """
    Ejecucion post-validacion

    """
    menu_principal([])
    

if __name__ == "__main__":
    """
    Validacion para ejecucion

    """
    main()
    
