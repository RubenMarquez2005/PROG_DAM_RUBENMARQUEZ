tareas = {}

while True:
    nombre_tarea = input("Escribe el nombre de la tarea o fin para salir : ")
    if nombre_tarea == "fin":
        break
    urgente = int(input("Escribe 1 si es urgente o por el contrario 2 si no es urgente: "))
    if urgente == 1:
        tareas [nombre_tarea] = True
    elif urgente == 2:
        tareas [nombre_tarea] = False
    else:
        print("Número no válido vuelva a introducirlo: ")

def tar_urgentes (urgencia):
    return tareas [urgencia]
urgentes = list(filter(tar_urgentes, tareas))

print("Las tareas urgentes son: ")
print (urgentes)