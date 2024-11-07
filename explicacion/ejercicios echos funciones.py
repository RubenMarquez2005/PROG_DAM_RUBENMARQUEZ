def area_triangulos (base, altura):
    return (base * altura)/2

resultado = area_triangulos(4,5)
print(f"El resultado es: {resultado}")

def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
 
resultado = es_par(8)
print(f"El numero es par, {resultado}")   

def saludo_personalizado(nombre, horadeldia):
    if horadeldia == "mañana":
        print()