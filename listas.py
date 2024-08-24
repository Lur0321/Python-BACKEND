"""
Gestor de Tareas: Crea una aplicación de consola que permita agregar, eliminar y listar tareas.
"""
tareas = []
while True:
    opList = int(input("Lista de tareas\n 1.-Agregar\n 2.-Eliminar\n 3.-Listar\n 4.-Salir\n"))
    if opList == 1:
        opAdd = int(input("Qué deseas hacer?\n1.- Agregar al final\n2.-Agregar en una posición (Si no hay nada se agregara en la primera posición)\n"))
        if opAdd == 1:
          tarea = input("Agrega tu tarea a la lista\n")
          tareas.append(tarea)
          print(f"Se agrego {tarea} en la posición {tareas.index(tarea)+1}")
        elif opAdd == 2:
          pass