import mysql.connector

def menu():
    while True:
        """Mostrar menú de opciones para el usuario."""
        print("Seleccione una opción:")
        print("1. Crear nueva categoria")
        print("2. Leer categorias")
        print("3. Actualizar categoria")
        print("4. Eliminar categoria")
        print("5. Salir del programa")
        
        elegir_opcion = input("Elige una opción: ")
        if elegir_opcion == "1":
            CrearCategoria()
            
        elif elegir_opcion == "2":
            LeerCategorias()
            
        elif elegir_opcion == "3":
            ActualizarCategoria()
            
        elif elegir_opcion == "4":
            EliminarCategoria()
            
        elif elegir_opcion == "5":
            salir()
        else:
            print("Opción no válida")
    
def CrearCategoria(idcategoria, nombre):
    """Crear una nueva categoria en la base de datos."""
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "INSERT INTO categorias (idcategoria, nombre) VALUES (%s, %s)"
    cursor.execute(sql, (idcategoria, nombre))
    conexion.commit()
    conexion.close()
    print("Categoria creada\n")

def LeerCategorias():
    """Leer todas las categorias de la base de datos."""
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "SELECT * FROM categoria"
    cursor.execute(sql)
    categorias = cursor.fetchall()
    conexion.close()
    for categoria in categorias:
        print(categoria)

def ActualizarCategoria(idcategoria, nombre):
    """Actualizar una categoria de la base de datos."""
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "UPDATE categoria SET nombre = %s WHERE idcategoria = %s"
    cursor.execute(sql, (nombre, idcategoria))
    conexion.commit()
    conexion.close()
    print("Categoria actualizada")

def EliminarCategoria(idcategoria):
    """Eliminar una categoria de la base de datos."""
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "DELETE FROM categoria WHERE idcategoria = %s"
    cursor.execute(sql, (idcategoria,))
    conexion.commit()
    conexion.close()
    print("Categoria eliminada")

def salir():
    """Salir del programa."""
    print("Saliendo del programa...")
    exit()

def conectar():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="curso",
        database="supermercado"
    )
    return conexion
