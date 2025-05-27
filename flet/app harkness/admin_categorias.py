import flet as ft
from db import conectar_mariadb

def admin_categorias_page(page: ft.Page):
    # Mostrar lista de categorías (todas las columnas)
    def obtener_lista_categorias():
        try:
            conexion = conectar_mariadb()
            cursor = conexion.cursor()
            cursor.execute("SHOW COLUMNS FROM categorias")
            columnas = [col[0] for col in cursor.fetchall()]
            cursor.execute("SELECT * FROM categorias")
            categorias = cursor.fetchall()
            cursor.close()
            conexion.close()
            return columnas, categorias
        except Exception as ex:
            return [], []

    columnas, lista_categorias = obtener_lista_categorias()
    if lista_categorias:
        categorias_view = ft.ListView(
            [
                ft.Text(
                    " | ".join(f"{col}: {valor}" for col, valor in zip(columnas, fila))
                )
                for fila in lista_categorias
            ],
            spacing=5,
            height=150,
            expand=False,
        )
    else:
        categorias_view = ft.ListView(
            [ft.Text("No hay categorías registradas.", color="grey")],
            spacing=5,
            height=150,
            expand=False,
        )

    # Input para agregar categoría
    categoria_input = ft.TextField(label="Nombre de la categoría", width=250, bgcolor="#2e2d2d")
    mensaje = ft.Text("", color="green")

    def actualizar_lista():
        columnas, lista = obtener_lista_categorias()
        if lista:
            categorias_view.controls = [
                ft.Text(
                    " | ".join(f"{col}: {valor}" for col, valor in zip(columnas, fila))
                )
                for fila in lista
            ]
        else:
            categorias_view.controls = [ft.Text("No hay categorías registradas.", color="grey")]
        page.update()

    def agregar_categoria(e):
        nombre = categoria_input.value.strip()
        if not nombre:
            mensaje.value = "Debes escribir un nombre de categoría."
            mensaje.color = "red"
        else:
            try:
                conexion = conectar_mariadb()
                cursor = conexion.cursor()
                cursor.execute(
                    "INSERT INTO categorias (nombre_categoria) VALUES (%s)",
                    (nombre,)
                )
                conexion.commit()
                mensaje.value = f"Categoría '{nombre}' agregada correctamente."
                mensaje.color = "green"
                categoria_input.value = ""
                actualizar_lista()
                cursor.close()
                conexion.close()
            except Exception as ex:
                mensaje.value = f"Error: {ex}"
                mensaje.color = "red"
        page.update()

    # Input para borrar categoría
    borrar_categoria_input = ft.TextField(label="Categoría a borrar", width=250, bgcolor="#f0f0f0")
    mensaje_borrar = ft.Text("", color="red")

    def borrar_categoria(e):
        nombre = borrar_categoria_input.value.strip()
        if not nombre:
            mensaje_borrar.value = "Escribe la categoría a borrar."
            mensaje_borrar.color = "red"
            page.update()
            return
        try:
            conexion = conectar_mariadb()
            cursor = conexion.cursor()
            cursor.execute(
                "DELETE FROM categorias WHERE nombre_categoria = %s",
                (nombre,)
            )
            conexion.commit()
            if cursor.rowcount > 0:
                mensaje_borrar.value = f"Categoría '{nombre}' borrada correctamente."
                mensaje_borrar.color = "green"
                borrar_categoria_input.value = ""
                actualizar_lista()
            else:
                mensaje_borrar.value = "No se encontró la categoría."
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
                ft.Text("Alta/Baja Categoría", size=22, weight="bold"),
                ft.Text("Agregar categoría", weight="bold"),
                categoria_input,
                ft.ElevatedButton(
                    icon=ft.icons.ADD,
                    text="Agregar categoría",
                    on_click=agregar_categoria,
                    width=250,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=4)),
                    bgcolor="#1976D2",
                    color="white",
                ),
                mensaje,
                ft.Divider(),
                ft.Text("Borrar categoría", weight="bold"),
                borrar_categoria_input,
                ft.ElevatedButton(
                    icon=ft.icons.REMOVE,
                    text="Borrar categoría",
                    on_click=borrar_categoria,
                    width=250,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=4)),
                    bgcolor="red",
                    color="white",
                ),
                mensaje_borrar,
                ft.Divider(),
                ft.Text("Categorías actuales:", weight="bold"),
                categorias_view,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        ),
        alignment=ft.alignment.center,
        expand=True,
    )