import random  # Importamos la librería 'random' 


# Diccionario de los monstruos y su nivel de dificultad
monstruos = { 'vampiro': 3, 'momia': 2, 'bruja': 4, 'esqueleto': 1, 'fantasma': 5 }
# Lista de objetos que el jugador puede elegir para intentar capturar al monstruo
objetos = ['estaca', 'poción mágica', 'hechizo']

# Función para mostrar el monstruo y su dificultad
def mostrar_monstruo():
    monstruo = random.choice(list(monstruos.keys()))
    dificultad = monstruos[monstruo] # Variable de la dificultad del monstruo seleccionado
    print(f"¡Un {monstruo} ha aparecido de la nada! Tiene dificultad {dificultad}.")
    return monstruo, dificultad

# Función para intentar capturar al monstruo
def intentar_captura(monstruo, dificultad, objeto):
    probabilidad = random.randint(1, 5) # Generamos un número aleatorio entre 1 y 5
    if probabilidad > dificultad:
        print(f"¡Capturaste al {monstruo} con {objeto}!")
        return True  
    else:
        print(f"Fallaste al capturar al {monstruo}")
        return False 

# Función para la caza del monstruo
def caza_monstruo():
    monstruo, dificultad = mostrar_monstruo()
    intentos = 3
    while intentos > 0:
        print(f"Tienes {intentos} intentos")
        objeto = input("Elige un objeto (estaca, poción mágica, hechizo): ")
        if intentar_captura(monstruo, dificultad, objeto):
            break  
        else:
            intentos -= 1  
    if intentos == 0:
        print(f"El {monstruo} se escapó")

# Ejecuta el juego
caza_monstruo()
