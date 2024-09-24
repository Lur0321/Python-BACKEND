"""
    Conversor de Unidades: Escribe un programa 
    que convierta entre diferentes unidades de medida 
    (por ejemplo, kilómetros a millas, Celsius a Fahrenheit).

operation = {
    1: lambda x: x / 1.609, 
    2: lambda x: x * 1.60934,
    3: lambda x: (x * 1.8) + 32,
    4: lambda x: (x - 32) * 0.555
}

nameOp = {
    1: "K a M", 
    2: "M a K",
    3: "C a F",
    4: "F a C"
}


while True:
    print("Conversor de Unidades")
    try:
        ope = float(input("Que operación desea hacer? 1.- K a M, 2.- M a K, 3.- C a F, 4.- F a C\n"))
        try:
            print(nameOp[ope])
            x = float(input("Ingrese su valor a copnvertir en numeros\n"))
            if ope in operation:
                print(f"Tu resultado es {operation[ope](x):.3f}")
        except  ValueError:
            print("Ingrese un numero")
            continue
    except  ValueError:
        print("Ingrese un valor de la lista")
        continue
    try:
        finO = int(input("1.- Para salir, enter para continuar\n"))
    except ValueError:
        finO = 0
    if finO == 1:
        break
"""
operation = {
    1: lambda x: x / 1.609, 
    2: lambda x: x * 1.60934,
    3: lambda x: (x * 1.8) + 32,
    4: lambda x: (x - 32) * 0.555
}

nameOp = {
    1: "Kilómetros a Millas", 
    2: "Millas a Kilómetros",
    3: "Celsius a Fahrenheit",
    4: "Fahrenheit a Celsius"
}

while True:
    print("Conversor de Unidades")
    try:
        ope = int(input("¿Qué operación desea hacer?\n1.- Kilómetros a Millas\n2.- Millas a Kilómetros\n3.- Celsius a Fahrenheit\n4.- Fahrenheit a Celsius\n"))
        
        if ope not in operation:
            print("Seleccione una operación válida de la lista.")
            continue
        
        x = float(input(f"Ingrese su valor a convertir en {nameOp[ope].split()[0]}\n"))
        resultado = operation[ope](x)
        print(f"Resultado: {resultado:.3f} {nameOp[ope].split()[2]}")

    except ValueError:
        print("Entrada no válida. Por favor, ingrese números únicamente.")

    finO = input("Presione 1 para salir, o enter para continuar\n")
    if finO == "1":
        break
   
    