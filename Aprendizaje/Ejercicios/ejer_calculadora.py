#**********************************************************************************************#
#**********************************************************************************************#
#**********************************************************************************************#
#**********************************************************************************************#
#**********************************************************************************************#

historial = []
total_ = 0.0

def SumaF(pos_his):
    global total_
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
                menu_operaciones(operacion, pos_his)

        except ValueError:
            print("INGRESE UN NUMERO PARA LA OPERACION")

def RestaF(pos_his):
    global total_
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
                menu_operaciones(operacion, pos_his)

        except ValueError:
            print("INGRESE UN NUMERO PARA LA OPERACION")

def MultiF(pos_his):
    global total_
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
                menu_operaciones(operacion, pos_his)
                

        except ValueError:
            print("INGRESE UN NUMERO PARA LA OPERACION")

def DiviF(pos_his):
    global total_
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
                menu_operaciones(operacion, pos_his)

        except ValueError:
            print("INGRESE UN NUMERO PARA LA OPERACION")
        except ZeroDivisionError:
            print("El divisor no puede ser igual a 0")

def peticion_de_valor(total_ : float, operacion : str) -> str:
    print("peti valor")
    print(f"Ingrese el valor numerico {operacion}:         Total = {total_}    x para salir ")
    x = input()
    return x

def peticion_de_operacion(total_ : float) -> str:
    opciones = ["+", "-", "*", "/", "x"]
    while True:
        print(f"Total = {total_}")
        opcion = input("Ingrese signo de operacion   \n+ Suma   \n- Resta   \n* Multiplicacion  \n/ Division   \nx Salir\n")
        if opcion in opciones:
            return opcion
        else:
            print("Ingrese un signo de operacion valido! ")

def menu_operaciones(operacion : str, pos_his : int):
    global total_

    if operacion == "+":
        SumaF(pos_his)
    elif operacion == "-":
        RestaF(pos_his)
    elif operacion == "*":
        MultiF(pos_his)
    elif operacion == "/":
        DiviF(pos_his)
    elif operacion == "x":
        total_ = 0
        print(historial)
        menu_principal()

def guardar_historial(posicion_historial : int, operador : str, valor : float , resultado : float):
    global historial
    operacion =  operador + str( float(valor)) + " = " + str(resultado) + " "
    historial[posicion_historial-1] += operacion

def nueva_operacion():
    global total_
    global historial
    if len(historial) == 0:
        pos_his = len(historial)
        
    else:
        pos_his = len(historial)
    while True:
        x = peticion_de_valor(total_, "a OPERAR ")
        if x == "x":
            menu_operaciones(x, pos_his)
        elif x != "x":
            total_ += float(x)
            historial.append(x)
            operacion = peticion_de_operacion(total_)
            print(pos_his)
            menu_operaciones(operacion , pos_his)
        else:
            print("Invalido")

def visualizar_historial(historial):
    if len(historial) != 0:
        print(len(historial))
        for i in historial:
            print(i)
            print()
    else:
        print("No hay datos en el historial ", len(historial))

    input("Presione x para regresar al menu ")
    menu_principal()

def menu_principal():
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
    menu_principal()
    

if __name__ == "__main__":
    main()
    
