import utilidades
texto = input("Introduce un texto: ")
print("Texto en mayúsculas:", utilidades.convertir_a_mayusculas(texto))
print("Texto en minúsculas:", utilidades.convertir_a_minusculas(texto))
if utilidades.es_palindromo(texto):
    print("El texto es un palíndromo")
else:
    print("El texto no es un palíndromo")