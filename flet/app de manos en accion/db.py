import mysql.connector

def conectar_mariadb():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",       # Cambia esto si tu servidor no está en localhost
            user="janopineda",      # Usuario de la base de datos
            password="pisa010478",  # Contraseña del usuario
            database="appharkpoint" # Nombre de la base de datos
        )
        print("Conexión exitosa")
        return conexion  # Devuelve la conexión para que pueda ser usada en otros archivos
    except mysql.connector.Error as err:
        print(f"Error de conexión: {err}")
        return None  # Devuelve None si hay un error