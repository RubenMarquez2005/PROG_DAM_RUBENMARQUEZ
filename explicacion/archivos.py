archivo=open("miarchivo.txt","r")
contenido=archivo.read()
print(contenido)
archivo.close()

# print("===============================================")

# with open("miarchivo.txt","r") as archivo:
#     contenido=archivo.read()
#     print(contenido)
#     archivo.close()

# with open('mi_archivo.txt', 'w') as archivo:
#     archivo.write('Hola, este es un archivo de ejemplo.')
#     archivo.write('Podemos escribir varias líneas así.')

with open('miarchivo.txt', 'a') as archivo:
    archivo.write('Esta es una línea adicional.')
    archivo.close()