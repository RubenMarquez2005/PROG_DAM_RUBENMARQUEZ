import numpy as np


matriz = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])


promedios = np.mean(matriz, axis=1)


for i, promedio in enumerate(promedios):
    print(f"El promedio de la fila {i+1} es: {promedio}")