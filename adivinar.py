"""
Juego de Adivinanzas: 
Desarrolla un juego donde el usuario tenga que adivinar un número generado aleatoriamente por la computadora.
"""

import random

def numeroR():
    return random.randrange(1,10)

def validar(x,y):
    if x == y:
        print(f"Ganaste los numeros son {x}\n")
    else:
        print(f"Los numeros son diferentes {x} , {y}\n")
while True:
    print("Adivina el numero del 1 - 10\n")
    op=int(input("1.- Jugar 2.-Salir\n"))
    match op:
        case 1:
            valP = int(input("Ingresa tu numero\n"))
            validar(valP,numeroR())       
        case 2:
            break
        case _:
            print("Agregue una opción valida\n")
            
    