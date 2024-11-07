import mysql.connector
def conectar(baseDatos):
    # Conexión a la base de datos
    conexion = mysql.connector.connect(
        host ='localhost',
        user ='root',
        password ='curso',
        database = baseDatos
    )
    return conexion
print('Conexión establecida')