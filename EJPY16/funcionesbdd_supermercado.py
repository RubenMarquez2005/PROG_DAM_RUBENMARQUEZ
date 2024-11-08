import mysql.connector

# Función para conectar a la base de datos
def conectar():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="curso",
        database="supermercado"
    )
    return conexion

# Funciones CRUD para Categorías
def CrearCategoria(id_categoria, nombre):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "INSERT INTO categoria (idcategoria, categoria) VALUES (%s, %s)"
    cursor.execute(sql, (id_categoria, nombre))
    conexion.commit()
    conexion.close()
    print("Categoría creada")

def LeerCategorias():
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "SELECT * FROM categoria"
    cursor.execute(sql)
    categorias = cursor.fetchall()
    conexion.close()
    for categoria in categorias:
        print(categoria)

def ActualizarCategoria(id_categoria, nombre):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "UPDATE categoria SET categoria = %s WHERE idcategoria = %s"
    cursor.execute(sql, (nombre, id_categoria))
    conexion.commit()
    conexion.close()
    print("Categoría actualizada")

def EliminarCategoria(id_categoria):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "DELETE FROM categoria WHERE idcategoria = %s"
    cursor.execute(sql, (id_categoria,))
    conexion.commit()
    conexion.close()
    print("Categoría eliminada")

# Funciones CRUD para Productos
def CrearProducto(id_producto, nombre, precio):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "INSERT INTO producto (idproducto, nombre, precio) VALUES (%s, %s, %s)"
    cursor.execute(sql, (id_producto, nombre, precio))
    conexion.commit()
    conexion.close()
    print("Producto creado")

def LeerProductos():
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "SELECT * FROM producto"
    cursor.execute(sql)
    productos = cursor.fetchall()
    conexion.close()
    for producto in productos:
        print(producto)

def ActualizarProducto(id_producto, nombre, precio):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "UPDATE producto SET nombre = %s, precio = %s WHERE idproducto = %s"
    cursor.execute(sql, (nombre, precio, id_producto))
    conexion.commit()
    conexion.close()
    print("Producto actualizado")

def EliminarProducto(id_producto):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "DELETE FROM producto WHERE idproducto = %s"
    cursor.execute(sql, (id_producto,))
    conexion.commit()
    conexion.close()
    print("Producto eliminado")

# Menú para la tabla Categorías
def menu_categoria():
    while True:
        print("\nSeleccione una operación para Categorías:")
        print("1. Crear nueva categoría")
        print("2. Leer categorías")
        print("3. Actualizar categoría")
        print("4. Eliminar categoría")
        print("5. Volver al menú principal")
        
        opcion = input("Elige una opción: ")
        if opcion == "1":
            id_categoria = input("Introduce el ID de la categoría: ")
            nombre = input("Introduce el nombre de la categoría: ")
            CrearCategoria(id_categoria, nombre)
        elif opcion == "2":
            LeerCategorias()
        elif opcion == "3":
            id_categoria = input("Introduce el ID de la categoría: ")
            nombre = input("Introduce el nuevo nombre de la categoría: ")
            ActualizarCategoria(id_categoria, nombre)
        elif opcion == "4":
            id_categoria = input("Introduce el ID de la categoría: ")
            EliminarCategoria(id_categoria)
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")

# Menú para la tabla Productos
def menu_producto():
    while True:
        print("\nSeleccione una operación para Productos:")
        print("1. Crear nuevo producto")
        print("2. Leer productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Volver al menú principal")
        
        opcion = input("Elige una opción: ")
        if opcion == "1":
            id_producto = input("Introduce el ID del producto: ")
            nombre = input("Introduce el nombre del producto: ")
            precio = input("Introduce el precio del producto: ")
            CrearProducto(id_producto, nombre, precio)
        elif opcion == "2":
            LeerProductos()
        elif opcion == "3":
            id_producto = input("Introduce el ID del producto: ")
            nombre = input("Introduce el nuevo nombre del producto: ")
            precio = input("Introduce el nuevo precio del producto: ")
            ActualizarProducto(id_producto, nombre, precio)
        elif opcion == "4":
            id_producto = input("Introduce el ID del producto: ")
            EliminarProducto(id_producto)
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")

# Menú principal para seleccionar la tabla
def menu_principal():
    while True:
        print("\nSeleccione una tabla:")
        print("1. Categorías")
        print("2. Productos")
        print("3. Salir")
        
        opcion_tabla = input("Elige una opción: ")
        if opcion_tabla == "1":
            menu_categoria()
        elif opcion_tabla == "2":
            menu_producto()
        elif opcion_tabla == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
