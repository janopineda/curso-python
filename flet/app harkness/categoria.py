import flet as ft
from db import conectar_mariadb  # Importar la conexión a la base de datos

def obtener_enlaces_por_categoria(categoria):
    try:
        # Conectar a la base de datos
        conexion = conectar_mariadb()
        if conexion is None:
            return []  # Retornar una lista vacía si no hay conexión

        cursor = conexion.cursor()

        # Consulta para obtener los enlaces relacionados con la categoría
        consulta = """
        SELECT e.nombre_pagina, e.url_pagina
        FROM enlaces e
        JOIN categorias c ON e.categoria_id = c.id
        WHERE c.nombre_categoria = %s
        """
        cursor.execute(consulta, (categoria,))
        enlaces = cursor.fetchall()  # Obtener los resultados como una lista de tuplas

        # Cerrar la conexión
        cursor.close()
        conexion.close()

        return enlaces
    except Exception as e:
        print(f"Error al obtener enlaces: {e}")
        return []  # Retornar una lista vacía en caso de error

def categoria_page(page: ft.Page, categoria: str):
    # Obtener los enlaces relacionados con la categoría
    enlaces = obtener_enlaces_por_categoria(categoria)

    return ft.Column(
        [
            ft.Text(f"Contenido de la categoría: {categoria}", size=30, weight="bold", color="blue"),
            ft.Text(f"Aquí puedes mostrar información específica sobre {categoria}.", size=20),
            *[ 
                ft.TextButton(
                    text=f"Enlace a {nombre}",
                    on_click=lambda e, url=url: page.launch_url(url),
                    style=ft.ButtonStyle(color="blue"),
                )
                for nombre, url in enlaces
            ],
            ft.ElevatedButton("Regresar", on_click=lambda _: page.go("/home")),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )