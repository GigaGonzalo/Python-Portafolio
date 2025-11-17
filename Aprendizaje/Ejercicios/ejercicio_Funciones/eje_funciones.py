#**********************************************************************************************#
#**********************************************************************************************#
#**********************************************************************************************#
#**********************************************************************************************#
#**********************************************************************************************#

import random

def funcion_Sencilla():
    """
    Crea una variable de valor 10
    
    Args:
        
    Returns:

    """
    x = 10

    print(f"El valor de X es {x}")

def funcion_con_Argumento(x : int):
    """
    Suma el valor del agumento x + 10 para el valor de y
    
    Args:
        El valor de x
        
    Returns:

    """
    y = x +10

    print(f"El valor de Y es igual a la suma del argumento + 10   :  {x} + 10 = {y}")

def funcion_Return() -> int:
    """
    Crea una variable con un valor random entre 0 y 1500
    
    Args:
        
    Returns:
        El valor random entero entre 0 y 1500
    """
    x = random.randint(0,1500)
    return x

def funcion_con_Argumento_Opcionales(x , y = 10):
    """
    Define el valor de x2 con la multiplicacion de x, Y = 10 como valor opcional
    
    Args:
        x: Primer valor 
        y: Segundo valor(Opcional)
        
    Returns:
        
    """
    x2 = x * y

    print(f"El valor de X es argumento * (Y = 15) igual a {x2}")

def funcion_con_Args(*args) -> int:
    """
    Suma todos los argumentos recibidos
    
    Args:
        *args: Un numero de variables no definidas
        
    Returns:
        Sumatoria de todos los argumentos
    """
    sumatoria=0
    for i in args:
        sumatoria += i
    return sumatoria

def funcion_con_Kwargs(**kwargs):
    """
    Muestra las claves y valores recibidos en **kwargs
    
    Args:
        **kwargs: Un numero de argumentos nombrados
        
    Returns:
    
    """
    for clave, valor in kwargs.items():
        print(f"El {clave} es {valor}")
    

print("Ejercicio de Practica para Funciones")
print("Ejercicio de Funcion Sencilla, sin argumntos ni returns, solo ejecuta codigo")

funcion_Sencilla()

print("Ejemplo de Funcion con Argumento de Entrada simple")

s = random.randint(0,10)

funcion_con_Argumento(s)

print("Ejemplo de Funcion con retorno de un valor(return)")

s = funcion_Return()

print(f"El valor generado es {s}")

print("Ejemplo de Funcion con Argumentos Opcionales")

s = funcion_con_Argumento_Opcionales(15)

print("Ejemplo de Funcion con *Args")

s = funcion_con_Args(10,15,100,471,78456,1,-8)

print(f"La suma de todos los numero es igual a {s}")

print("Ejemplo de Funcion con *Kwargs")

funcion_con_Kwargs(nombre="Pedro", edad=30, ocupacion="Mesero", sueldo=10500.58 , casado=True)

