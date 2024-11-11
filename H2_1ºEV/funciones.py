# Estructuras de datos principales
clientes = {}  # Almacena clientes con su DNI como clave
productos = {
    1: {"nombre": "Producto 1", "precio": 10.0},
    2: {"nombre": "Producto 2", "precio": 15.0},
    3: {"nombre": "Producto 3", "precio": 20.0},
}
pedidos = {}  # Almacena los pedidos con el número de pedido como clave
contador_pedido = 1  # Generador de número de pedido único

# Funciones de la aplicación

def registrar_cliente():
    dni = input("Ingrese DNI del cliente: ")
    if dni in clientes:
        print("Cliente ya registrado.")
    else:
        nombre = input("Ingrese nombre del cliente: ")
        direccion = input("Ingrese dirección: ")
        telefono = input("Ingrese teléfono: ")
        clientes[dni] = {"nombre": nombre, "direccion": direccion, "telefono": telefono}
        print("Cliente registrado correctamente.")

def visualizar_clientes():
    if clientes:
        for dni, datos in clientes.items():
            print(f"DNI: {dni}, Nombre: {datos['nombre']}, Dirección: {datos['direccion']}, Teléfono: {datos['telefono']}")
    else:
        print("No hay clientes registrados.")

def realizar_compra():
    global contador_pedido
    dni = input("Ingrese DNI del cliente para realizar la compra: ")
    if dni not in clientes:
        print("Cliente no encontrado. Debe registrarse primero.")
    else:
        carrito = []
        print("Productos disponibles:")
        for id_producto, info in productos.items():
            print(f"{id_producto}: {info['nombre']} - ${info['precio']}")
        while True:
            id_producto = int(input("Seleccione el ID del producto para agregar al carrito (0 para finalizar): "))
            if id_producto == 0:
                break
            if id_producto in productos:
                carrito.append(productos[id_producto])
                print(f"{productos[id_producto]['nombre']} agregado al carrito.")
            else:
                print("ID de producto no válido.")
        
        if carrito:
            numero_pedido = contador_pedido
            pedidos[numero_pedido] = {"cliente": dni, "productos": carrito}
            contador_pedido += 1
            print(f"Compra realizada. Número de pedido: {numero_pedido}")
        else:
            print("No se ha seleccionado ningún producto.")

def seguimiento_pedido():
    numero_pedido = int(input("Ingrese el número de pedido para seguimiento: "))
    if numero_pedido in pedidos:
        pedido = pedidos[numero_pedido]
        cliente = clientes[pedido["cliente"]]
        print("Datos del cliente:")
        print(f"DNI: {pedido['cliente']}, Nombre: {cliente['nombre']}, Dirección: {cliente['direccion']}, Teléfono: {cliente['telefono']}")
        print("Productos del pedido:")
        for producto in pedido["productos"]:
            print(f"- {producto['nombre']} - ${producto['precio']}")
    else:
        print("Número de pedido no encontrado.")

# Menú principal

def menu():
    while True:
        print("\n--- Menú de Gestión de Pedidos ---")
        print("1. Registrar cliente")
        print("2. Visualizar clientes")
        print("3. Realizar compra")
        print("4. Seguimiento de compra")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            visualizar_clientes()
        elif opcion == "3":
            realizar_compra()
        elif opcion == "4":
            seguimiento_pedido()
        elif opcion == "5":
            print("Saliendo de la aplicación.")
            break
        else:
            print("Opción no válida, intente de nuevo.")

