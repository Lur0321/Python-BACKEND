"""finO = 0
while True: 
 print("Calculadora")
 x = int(input("Ingresa tu primer numero: "))
 y = int(input("Ingresa tu segundo numero: "))
 funO = input("Que quieres hacer? +, - , / o x ")

 if funO == "+":
    print(f"Tu numero es {x + y}")
 elif funO == "-":
    print(f"Tu numero es {x - y}")
 elif funO == "/":
    print(f"Tu numero es {x / y}")
 elif funO == "x":
    print(f"Tu numero es {x * y}")
 else:
    print("No hay una opreación valida")
 try:
    finO = int(input("1 para salir enter para continuar: "))
 except:
     finO = 0
 if finO == 1:
     break  
operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "/": lambda x, y: x / y,
    "x": lambda x, y: x * y
}

while True:
    print("Calculadora")
    try:
        x = int(input("Ingresa tu primer número: "))
        y = int(input("Ingresa tu segundo número: "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        continue

    funO = input("¿Qué quieres hacer? +, -, /, x: ").strip().lower()

    if funO in operations:
        print(f"Tu resultado es: {operations[funO](x, y)}")
    else:
        print("Operación no válida.")

    try:
        finO = int(input("1 para salir, enter para continuar: "))
    except ValueError:
        finO = 0

    if finO == 1:
        break
"""
def calcular(x, y, operacion):
    operations = {
        "+": x + y,
        "-": x - y,
        "/": "Error: División por cero" if y == 0 else x / y,
        "x": x * y
    }
    return operations.get(operacion, "Operación no válida")

def obtener_numero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Por favor, ingresa un número válido.")

while True:
    print("Calculadora")
    x = obtener_numero("Ingresa tu primer número: ")
    y = obtener_numero("Ingresa tu segundo número: ")
    operacion = input("¿Qué quieres hacer? +, -, /, x: ").strip().lower()

    resultado = calcular(x, y, operacion)
    print(f"Tu resultado es: {resultado}")

    if input("1 para salir, enter para continuar: ") == "1":
        break
