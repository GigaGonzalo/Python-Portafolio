#**********************************************************************************************#
#**********************************************************************************************#
#**********************************************************************************************#
#**********************************************************************************************#
#**********************************************************************************************#

historial = []

def SumaF(pos_his : int, total_ : float):
    """
    Suma el valor recibido al valor global de la operacion
    
    Args:
        pos_his : int       Posicion de la operacion en el historial
        total_  : float     Valor total de la operacion 
    """
    while True:
        try:
            x = peticion_de_valor(total_, "a SUMAR ")
            if x == "s":
                main()
            else:
                x = float(x)
                total_ += x
                guardar_historial(pos_his, " + ", x, total_)
                operacion = peticion_de_operacion(total_)
                menu_operaciones(operacion, pos_his, total_)

        except ValueError:
            print("INGRESE UN NUMERO PARA LA OPERACION")

def RestaF(pos_his : int, total_ : float):
    """
    Resta el valor recibido al valor global de la operacion
    
    Args:
        pos_his : int       Posicion de la operacion en el historial
        total_  : float     Valor total de la operacion 
    """
    while True:
        try:
            x = peticion_de_valor(total_, "a RESTAR ")
            if x == "s":
                main()
            else:
                x = float(x)
                total_ -= x
                guardar_historial(pos_his," - ", x, total_)
                operacion = peticion_de_operacion(total_)
                menu_operaciones(operacion, pos_his, total_)

        except ValueError:
            print("INGRESE UN NUMERO PARA LA OPERACION")

def MultiF(pos_his : int, total_ : float):
    """
    Multiplica el valor recibido al valor global de la operacion
    
    Args:
        pos_his : int       Posicion de la operacion en el historial
        total_  : float     Valor total de la operacion 
    """
    while True:
        try:
            x = peticion_de_valor(total_, "a MULTIPLICAR ")
            if x == "s":
                main()
            else:
                x = float(x)
                total_ *= x
                guardar_historial(pos_his," * ", x, total_)
                operacion = peticion_de_operacion(total_)
                menu_operaciones(operacion, pos_his, total_)
                

        except ValueError:
            print("INGRESE UN NUMERO PARA LA OPERACION")

def DiviF(pos_his : int, total_ : float):
    """
    Divide el valor recibido al valor global de la operacion
    
    Args:
        pos_his : int       Posicion de la operacion en el historial
        total_  : float     Valor total de la operacion 
    """
    while True:
        try:
            x = peticion_de_valor(total_, "a DIVIDIR ")
            if x == "s":
                main()
            else:
                x = float(x)
                total_ /= x
                guardar_historial(pos_his," / ", x, total_)
                operacion = peticion_de_operacion(total_)
                menu_operaciones(operacion, pos_his, total_)

        except ValueError:
            print("INGRESE UN NUMERO PARA LA OPERACION")
        except ZeroDivisionError:
            print("El divisor no puede ser igual a 0")

def peticion_de_valor(total_ : float, operacion : str) -> str:
    """
    Solicita el valor para la operacion al usuario
    
    Args:
        total_ : float        Total de la operacion en curso
        operacion : str       Operador a realizar 
        
    Returns:
        Valor ingresado, en caso de alfabeto, en minusculas
    """
    print(f"Ingrese el valor numerico {operacion}:         Total = {total_}    x para salir ")
    x = input().lower()
    return x

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

def menu_operaciones(operacion : str, pos_his : int, total_ : float):
    """
    Menu encargado de realizar la siguiente operacion basado en el operador ingresado
    
    Args:
        operacion : str         Operador de la siguiente operacion
        pos_his   : int         Posicion de la operacion en el historial
        total_    : float       Total de la operacion en curso
    """
    if operacion == "+":
        SumaF(pos_his, total_)
    elif operacion == "-":
        RestaF(pos_his, total_)
    elif operacion == "*":
        MultiF(pos_his, total_)
    elif operacion == "/":
        DiviF(pos_his, total_)
    elif operacion == "x":
        menu_principal()

def guardar_historial(posicion_historial : int, operador : str, valor : float , resultado : float):
    """
    Almacena la operacion en el historial de la sesion
    
    Args:
        posicion_historial : int    Posicion de la operacion en el historial
        operador           : str    Operador de la operacion
        valor              : float  Valor que se aplico en la operacion
        resultado          : float  Total de la operacion realizada
    """
    global historial
    operacion =  operador + str( float(valor)) + " = " + str(resultado) + " "
    historial[posicion_historial] += operacion

def nueva_operacion():
    """
    Inicia una nueva operacion de la calculadora

    """
    global historial
    total_ = 0.0
    if len(historial) == 0:
        pos_his = len(historial)
        
    elif len(historial) > 0:
        pos_his = len(historial)
    while True:
        x = peticion_de_valor(total_, "a OPERAR ")
        if x == "x":
            menu_operaciones(x, pos_his)
        elif x != "x":
            total_ += float(x)
            historial.append(x)
            operacion = peticion_de_operacion(total_)
            menu_operaciones(operacion , pos_his, total_)
        else:
            print("Invalido")

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

    input("Presione x para regresar al menu ")
    menu_principal()

def menu_principal():
    """
    Menu principal donde el usuario elige su accion

    """
    global historial
    opciones = ["1", "2", "3"]
    print(" "*10 + " Calculadora " + " "*10)
    print("Seleccione una de las siguientes opciones : " + 
        "\n1. Nueva operacion" +
        "\n2. Ver historial de operaciones" + 
        "\n3. Salir")
    opcion = input("Seleccione : ")
    if opcion in opciones:
        if opcion == "1":
            nueva_operacion()
        elif opcion == "2":
            visualizar_historial(historial)
        elif opcion == "3":
            exit()

def main():
    """
    Ejecucion post-validacion

    """
    menu_principal()
    

if __name__ == "__main__":
    """
    Validacion para ejecucion

    """
    main()
    
