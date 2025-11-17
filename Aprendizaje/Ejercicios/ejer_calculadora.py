#**********************************************************************************************#
#**********************************************************************************************#
#**********************************************************************************************#
#**********************************************************************************************#
#**********************************************************************************************#
import keyboard
def SumaF():
    vars_suma = []
    suma_total = 0.0
    while True:
        try:
            x = float(input("Ingrese el valor a sumar :"))
            if keyboard.isPressed("+"):
                vars_suma.append(x)
                suma_total += x
            elif keyboard.isPressed("enter"):
                vars_suma.append(x)
                suma_total += x
        except ValueError:
            print("INGRESE UN NUMERO PARA LA OPERACION")








def main():
    opciones = [1,2,3,4,5]
    print("Calculadora Basica")
    print("Ingrese la opcion de la operacion a realizar:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")

    opcion = int(input("Operacion : "))
    try:
        while True:
            if opcion in opciones:
                if opcion == 1:
                    SumaF()
                elif opcion == 2:
                    print("Unfer")
                    #RestaF()
                elif opcion == 3:
                    print("Unfer")
                    #MultiF()
                elif opcion == 4:
                    print("Unfer")
                    #DiviF()
                elif opcion == 5:
                    print("Unfer")
                    exit()
                    #SalidaF()
    except ValueError:
        print("Ingrese un NUMERO valido")

if __name__ == "__main__":
    main()
    
