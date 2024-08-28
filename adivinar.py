"""
Juego de Adivinanzas: 
Desarrolla un juego donde el usuario tenga que adivinar un número generado aleatoriamente por la computadora.


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
"""
import random

def generar_numero():
    return random.randint(1, 10)  # Utiliza randint para incluir ambos extremos

def validar(numero_usuario, numero_generado):
    if numero_usuario == numero_generado:
        print(f"¡Ganaste! El número era {numero_generado}.\n")
        return True
    elif numero_usuario < numero_generado:
        print(f"El número es mayor que {numero_usuario}. Intenta de nuevo.\n")
    else:
        print(f"El número es menor que {numero_usuario}. Intenta de nuevo.\n")
    return False

def jugar():
    numero_secreto = generar_numero()
    intentos = 0
    
    while True:
        try:
            numero_usuario = int(input("Ingresa tu número (1-10): "))
            if numero_usuario < 1 or numero_usuario > 10:
                print("Por favor, ingresa un número entre 1 y 10.")
                continue
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número.")
            continue

        intentos += 1
        
        if validar(numero_usuario, numero_secreto):
            print(f"Adivinaste el número en {intentos} intentos.\n")
            break

def main():
    while True:
        print("Adivina el número del 1 al 10\n")
        try:
            op = int(input("1.- Jugar 2.- Salir\n"))
        except ValueError:
            print("Por favor, ingresa una opción válida.\n")
            continue

        match op:
            case 1:
                jugar()
            case 2:
                print("Gracias por jugar. ¡Hasta la próxima!")
                break
            case _:
                print("Agregue una opción válida\n")

if __name__ == "__main__":
    main()
            
    