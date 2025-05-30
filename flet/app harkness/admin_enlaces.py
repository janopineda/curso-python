import flet as ft
from db import conectar_mariadb

def admin_enlaces_page(page: ft.Page):
    # Inputs para agregar enlace
    nombre_enlace_input = ft.TextField(label="Nombre del enlace", width=300, bgcolor="#f0f0f0")
    url_enlace_input = ft.TextField(label="Liga (URL)", width=300, bgcolor="#f0f0f0")
    categoria_input = ft.TextField(label="Categoría", width=300, bgcolor="#f0f0f0")
    mensaje_agregar = ft.Text("", color="green")

    # Inputs para borrar enlace
    nombre_borrar_input = ft.TextField(label="Nombre del enlace a borrar", width=300, bgcolor="#f0f0f0")
    url_borrar_input = ft.TextField(label="Liga (URL) a borrar", width=300, bgcolor="#f0f0f0")
    mensaje_borrar = ft.Text("", color="red")

    def agregar_enlace(e):
        nombre = nombre_enlace_input.value.strip()
        url = url_enlace_input.value.strip()
        categoria = categoria_input.value.strip()
        if not nombre or not url or not categoria:
            mensaje_agregar.value = "Completa todos los campos para agregar."
            mensaje_agregar.color = "red"
        else:
            try:
                conexion = conectar_mariadb()
                cursor = conexion.cursor()
                cursor.execute(
                    "INSERT INTO enlaces (nombre, url, categoria) VALUES (%s, %s, %s)",
                    (nombre, url, categoria)
                )
                conexion.commit()
                mensaje_agregar.value = f"Enlace '{nombre}' agregado correctamente."
                mensaje_agregar.color = "green"
                nombre_enlace_input.value = ""
                url_enlace_input.value = ""
                categoria_input.value = ""
                cursor.close()
                conexion.close()
            except Exception as ex:
                mensaje_agregar.value = f"Error: {ex}"
                mensaje_agregar.color = "red"
        page.update()

    def borrar_enlace(e):
        nombre = nombre_borrar_input.value.strip()
        url = url_borrar_input.value.strip()
        if not nombre or not url:
            mensaje_borrar.value = "Completa ambos campos para borrar."
            mensaje_borrar.color = "red"
        else:
            try:
                conexion = conectar_mariadb()
                cursor = conexion.cursor()
                cursor.execute(
                    "DELETE FROM enlaces WHERE nombre = %s AND url = %s",
                    (nombre, url)
                )
                conexion.commit()
                if cursor.rowcount > 0:
                    mensaje_borrar.value = f"Enlace '{nombre}' borrado correctamente."
                    mensaje_borrar.color = "green"
                    nombre_borrar_input.value = ""
                    url_borrar_input.value = ""
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
                categoria_input,
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
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        ),
        alignment=ft.alignment.center,
        expand=True,
    )