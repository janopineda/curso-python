import flet as ft
from db import conectar_mariadb

def obtener_categorias_con_id():
    conexion = conectar_mariadb()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre_categoria FROM categorias")
    categorias = cursor.fetchall()
    cursor.close()
    conexion.close()
    return categorias

def obtener_enlaces_con_categoria():
    conexion = conectar_mariadb()
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT e.nombre_pagina, e.url_pagina, c.nombre_categoria
        FROM enlaces e
        JOIN categorias c ON e.categoria_id = c.id
    """)
    enlaces = cursor.fetchall()
    cursor.close()
    conexion.close()
    return enlaces

def admin_enlaces_page(page: ft.Page):
    # Obtener las categorías con su ID y nombre
    categorias_lista = obtener_categorias_con_id()
    categoria_dropdown = ft.Dropdown(
        label="Categoría",
        width=300,
        options=[ft.dropdown.Option(str(cat[0]), cat[1]) for cat in categorias_lista],
        bgcolor="#333333",
        color="white"
    )
    categoria_borrar_dropdown = ft.Dropdown(
        label="Categoría a borrar",
        width=300,
        options=[ft.dropdown.Option(str(cat[0]), cat[1]) for cat in categorias_lista],
        bgcolor="#333333",
        color="white"
    )

    # Inputs para agregar enlace
    nombre_enlace_input = ft.TextField(label="Nombre de la página", width=300, bgcolor="#333333", color="white")
    url_enlace_input = ft.TextField(label="URL de la página", width=300, bgcolor="#333333", color="white")
    mensaje_agregar = ft.Text("", color="green")

    # Inputs para borrar enlace
    nombre_borrar_input = ft.TextField(label="Nombre de la página a borrar", width=300, bgcolor="#333333", color="white")
    url_borrar_input = ft.TextField(label="URL de la página a borrar", width=300, bgcolor="#333333", color="white")
    mensaje_borrar = ft.Text("", color="red")

    # Listado de enlaces actuales
    def actualizar_lista():
        enlaces = obtener_enlaces_con_categoria()
        enlaces_view.controls = [
            ft.Text(f"{nombre} | {url} | {categoria}", color="white")
            for nombre, url, categoria in enlaces
        ]
        page.update()

    enlaces = obtener_enlaces_con_categoria()
    enlaces_view = ft.ListView(
        [ft.Text(f"{nombre} | {url} | {categoria}", color="white") for nombre, url, categoria in enlaces],
        spacing=5,
        height=150,
        expand=False,
    )

    def agregar_enlace(e):
        nombre = nombre_enlace_input.value.strip()
        url = url_enlace_input.value.strip()
        categoria_id = categoria_dropdown.value
        if not nombre or not url or not categoria_id:
            mensaje_agregar.value = "Completa todos los campos para agregar."
            mensaje_agregar.color = "red"
        else:
            try:
                conexion = conectar_mariadb()
                cursor = conexion.cursor()
                cursor.execute(
                    "INSERT INTO enlaces (nombre_pagina, url_pagina, categoria_id) VALUES (%s, %s, %s)",
                    (nombre, url, categoria_id)
                )
                conexion.commit()
                mensaje_agregar.value = f"Enlace '{nombre}' agregado correctamente."
                mensaje_agregar.color = "green"
                nombre_enlace_input.value = ""
                url_enlace_input.value = ""
                categoria_dropdown.value = None
                cursor.close()
                conexion.close()
                actualizar_lista()
            except Exception as ex:
                mensaje_agregar.value = f"Error: {ex}"
                mensaje_agregar.color = "red"
        page.update()

    def borrar_enlace(e):
        nombre = nombre_borrar_input.value.strip()
        url = url_borrar_input.value.strip()
        categoria_id = categoria_borrar_dropdown.value
        if not nombre or not url or not categoria_id:
            mensaje_borrar.value = "Completa todos los campos para borrar."
            mensaje_borrar.color = "red"
        else:
            try:
                conexion = conectar_mariadb()
                cursor = conexion.cursor()
                cursor.execute(
                    "DELETE FROM enlaces WHERE nombre_pagina = %s AND url_pagina = %s AND categoria_id = %s",
                    (nombre, url, categoria_id)
                )
                conexion.commit()
                if cursor.rowcount > 0:
                    mensaje_borrar.value = f"Enlace '{nombre}' borrado correctamente."
                    mensaje_borrar.color = "green"
                    nombre_borrar_input.value = ""
                    url_borrar_input.value = ""
                    categoria_borrar_dropdown.value = None
                    actualizar_lista()
                else:
                    mensaje_borrar.value = "No se encontró el enlace."
                    mensaje_borrar.color = "red"
                cursor.close()
                conexion.close()
            except Exception as ex:
                mensaje_borrar.value = f"Error: {ex}"
                mensaje_borrar.color = "red"
        page.update()

    return ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.IconButton(
                            icon=ft.icons.CLOSE,
                            icon_color="red",
                            tooltip="Regresar",
                            on_click=lambda _: page.go("/admin"),
                        )
                    ],
                    alignment=ft.MainAxisAlignment.END,
                ),
                ft.Text("Agregar nuevo enlace", weight="bold"),
                nombre_enlace_input,
                url_enlace_input,
                categoria_dropdown,
                ft.ElevatedButton(
                    icon=ft.icons.ADD_LINK,
                    text="Agregar enlace",
                    on_click=agregar_enlace,
                    width=300,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=4)),
                    bgcolor="#1976D2",
                    color="white",
                ),
                mensaje_agregar,
                ft.Divider(),
                ft.Text("Borrar enlace", weight="bold"),
                nombre_borrar_input,
                url_borrar_input,
                categoria_borrar_dropdown,
                ft.ElevatedButton(
                    icon=ft.icons.REMOVE_CIRCLE_OUTLINE,
                    text="Borrar enlace",
                    on_click=borrar_enlace,
                    width=300,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=4)),
                    bgcolor="red",
                    color="white",
                ),
                mensaje_borrar,
                ft.Divider(),
                ft.Text("Enlaces actuales:", weight="bold"),
                enlaces_view,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        ),
        alignment=ft.alignment.center,
        expand=True,
    )