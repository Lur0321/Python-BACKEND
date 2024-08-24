"""
Gestor de Tareas: Crea una aplicación de consola que permita agregar, eliminar y listar tareas.
"""
tareas = []
def  agregar(valor, valor2 = None):
  if valor2 is not None and 0 < valor2 <= len(tareas) + 1:
    tareas.insert(valor2-1, valor)
    pos = valor2
  else:
    tareas.append(valor)
    pos = len(tareas)
  return print(f"{valor} se agrego en la posición {pos}")

while True:
    opList = int(input("Lista de tareas\n 1.-Agregar\n 2.-Eliminar\n 3.-Listar\n 4.-Salir\n"))
    if opList == 1:
         valor = input("Agrega tu tarea\n")
         valor2_input = input(f"A que lugar deseas agregarlo? (Si solo quieres agregarla al final da ENTER)\n Tareas actuales: {len(tareas)}\n")
         valor2 = int(valor2_input) if valor2_input.strip() else None
         agregar(valor, valor2)
    elif opList == 3:
      if not tareas:
        print("Vacio")
      for indice, tarea in enumerate(tareas):
        print(f"{indice + 1}.- {tarea}")       
    else: 
      break