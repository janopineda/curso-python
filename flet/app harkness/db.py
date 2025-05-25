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

def obtener_categorias():
    conexion = conectar_mariadb()
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre_categoria FROM categorias")
    categorias = [fila[0] for fila in cursor.fetchall()]
    cursor.close()
    conexion.close()
    return categorias

def obtener_enlaces_por_categoria(categoria):
    conexion = conectar_mariadb()
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre, url FROM enlaces WHERE categoria = %s", (categoria,))
    enlaces = cursor.fetchall()
    cursor.close()
    conexion.close()
    return enlaces