libros = {}
while True:
    titulo = input("Escribe el título del libro o salir para finalizar: ")
    if titulo.lower() == 'fin':
        break
    categoria = input ("Escribe la categoria del libro (novela, ensayo, poesia...) : ")
    genero = input ("Escribe el genero del libro(fantasía, romance... ): ")

    if categoria == "novela":
        libros [titulo] = True
    else:
        libros[ titulo]= False

def es_novela(libro):
    return libros [libro]

novelas = list(filter(es_novela, libros))

print ("Los libros introducidos que son de categoria novela son: ")
print (novelas)