import funciones_bdd as bdd
#Conectamos con la base de datos animales que va a ser la carretera
conexion = bdd.conectar('animales')
# Creamos la furgoneta para transportar los datos
cursor = conexion.cursor()
# Creamos la consulta
# consulta = """
# select ANIMAL.animal, Familia.familia
# from ANIMAL
# JOIN FAMILIA ON ANIMAL.idFamilia = FAMILIA.idFamiia;"""

#Creamos la consulta para contar los animales por familia
# consulta = """select familia.familia, count(animal.animal) as total
# from animal
# join familia on animal.idFamilia = familia.idfamilia
# group by familia.familia;"""

#Definimos los datos del nuevo animal
# nuevo_animal = (10, 2, 'Tigre',2) #idAnimal, idFamilia, nombre, cantidad


#Creamos la consulta para insertar un nuevo animal
# consulta = """insert into animal (idAnimal, idFamilia, animal, cuantos)
# values (%s, %s, %s, %s)"""
# cursor.execute(consulta, nuevo_animal)

#Definir nuevos datos
nueva_cantidad = 5
animal_id= 1
#Conuslta para actualizar la cantidad
consulta = """update animal set cuantos = %s where idAnimal = %s"""
cursor.execute(consulta, (nueva_cantidad, animal_id))

#Ejecutamos la consulta
conexion.commit()
# print('Nuevo animal insertado correctamente')
print('Cantidad actualizada correctamente')
# cursor.execute(consulta)

#Recogemos todos los resultados de la consulta
# resultados = cursor.fetchall() 

#Recorremos todos los resultados y los mostramos
# for familia, total in resultados:#Recorremos los resultados y que nos muestre los resultados animal y familia
    # print(f"Familia: {familia}, Total: {total}") #Mostramos los resultados
    
cursor.close()#Llevamos la furgo al desguace
conexion.close()#Destruimos la carretera
