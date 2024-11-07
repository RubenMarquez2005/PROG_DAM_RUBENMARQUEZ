def sumapro(numero1, numero2):
    suma = numero1 + numero2
    print(f"La suma de {numero1} + {numero2}= {suma}")
    
#Comienza mi prgrama 
num1 = int(input("Escribe el primer numero: "))
num2 = int(input("Escribe el segundo numero: "))

sumapro(num1, num2)
#################################

def restapro(numero1, numero2):
    resta = numero1 - numero2
    print(f"La suma de {numero1} - {numero2}= {resta}")
    
#Comienza mi prgrama 
num1 = int(input("Escribe el primer numero: "))
num2 = int(input("Escribe el segundo numero: "))

restapro(num1, num2)
#######################################
def multipro(numero1, numero2):
    multi = numero1 * numero2
    print(f"La multiplicación de {numero1} * {numero2}= {multi}")
    
#Comienza mi prgrama 
num1 = int(input("Escribe el primer numero: "))
num2 = int(input("Escribe el segundo numero: "))

multipro(num1, num2)


#######################################
def divipro(numero1, numero2):
    divi = numero1 / numero2
    print(f"La división de {numero1} / {numero2}= {divi}")
    
#Comienza mi prgrama 
num1 = int(input("Escribe el primer numero: "))
num2 = int(input("Escribe el segundo numero: "))

divipro(num1, num2)


###########################################################
###########################################################
###########################################################

def sumapro2 (numero1, numero2):
    suma = numero1 + numero2
    return suma

def espar (numero):
    if numero % 2 == 0:
        valor  = True
    else:
        valor = False
    return valor

num1 = int(input("Escribe el primer numero: "))
num2 = int(input("Escribe el segundo numero: "))

resultadosuma = sumapro2(num1, num2)
print(f"El resultado de la suma es: {resultadosuma}")

if espar(num1):
    print(f"El numero {num1} es par")
else:
    print(f"El numero {num1} es impar")
    
if espar(num2):
    print(f"El numero {num2} es par")
else:
    print(f"El numero {num2} es impar")
    