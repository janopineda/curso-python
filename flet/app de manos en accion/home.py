import flet as ft
from db import conectar_mariadb  # Importar la función de conexión desde db.py

def obtener_categorias():
    try:
        # Conectar a la base de datos
        conexion = conectar_mariadb()
        cursor = conexion.cursor()

        # Consulta para obtener las categorías
        consulta = "SELECT nombre_categoria FROM categorias"
        cursor.execute(consulta)
        categorias = [fila[0] for fila in cursor.fetchall()]  # Obtener solo los nombres de las categorías

        # Cerrar la conexión
        cursor.close()
        conexion.close()

        # Depuración: Imprimir las categorías obtenidas
        print(f"Categorías obtenidas: {categorias}")

        return categorias
    except Exception as e:
        # Depuración: Imprimir el error si ocurre
        print(f"Error al obtener categorías: {e}")
        return []  # Retornar una lista vacía en caso de error

def home_page(page: ft.Page):
    # Obtener las categorías desde la base de datos
    listaCategorias = obtener_categorias()

    # Depuración: Imprimir las categorías que se usarán en la interfaz
    print(f"Lista de categorías en home_page: {listaCategorias}")

    # Generar dinámicamente los botones para las categorías
    return ft.Column(
        [
            ft.Text("Bienvenido a la página principal", size=30, weight="bold", color="green"),
            *[
                ft.ElevatedButton(
                    text=f"Categoría: {coleccion}",
                    on_click=lambda e, categoria=coleccion: page.go(f"/categoria/{categoria}"),
                    width=300,
                )
                for coleccion in listaCategorias
            ],
            ft.ElevatedButton("Cerrar sesión", on_click=lambda _: page.go("/")),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )