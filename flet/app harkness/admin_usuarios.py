import flet as ft
from db import conectar_mariadb

def admin_usuarios_page(page: ft.Page):
    # Mostrar lista de usuarios
    def obtener_lista_usuarios():
        try:
            conexion = conectar_mariadb()
            cursor = conexion.cursor()
            cursor.execute("SELECT usuario, rol FROM usuarios")
            usuarios = cursor.fetchall()
            cursor.close()
            conexion.close()
            return usuarios
        except Exception as ex:
            return []

    lista_usuarios = obtener_lista_usuarios()
    usuarios_view = ft.ListView(
        [ft.Text(f"{u[0]} ({u[1]})") for u in lista_usuarios],
        spacing=5,
        height=150,
        expand=False,
    )

    # Input para borrar usuario
    borrar_usuario_input = ft.TextField(
        label="Usuario a borrar",
        width=250,
        bgcolor="#333333",
        color="white"
    )
    mensaje_borrar = ft.Text("", color="red")

    def actualizar_lista():
        lista = obtener_lista_usuarios()
        usuarios_view.controls = [ft.Text(f"{u[0]} ({u[1]})") for u in lista]
        page.update()

    def borrar_usuario(e):
        usuario = borrar_usuario_input.value.strip()
        if not usuario:
            mensaje_borrar.value = "Escribe el usuario a borrar."
            mensaje_borrar.color = "red"
            page.update()
            return
        try:
            conexion = conectar_mariadb()
            cursor = conexion.cursor()
            cursor.execute(
                "DELETE FROM usuarios WHERE usuario = %s",
                (usuario,)
            )
            conexion.commit()
            if cursor.rowcount > 0:
                mensaje_borrar.value = f"Usuario '{usuario}' borrado correctamente."
                mensaje_borrar.color = "green"
                borrar_usuario_input.value = ""
                actualizar_lista()
            else:
                mensaje_borrar.value = "No se encontró el usuario."
                mensaje_borrar.color = "red"
            cursor.close()
            conexion.close()
        except Exception as ex:
            mensaje_borrar.value = f"Error: {ex}"
            mensaje_borrar.color = "red"
        page.update()

    # Alta usuario (con botón cuadrado y símbolo de más)
    usuario_input = ft.TextField(
        label="Usuario",
        width=250,
        bgcolor="#333333",
        color="white"
    )
    contrasena_input = ft.TextField(
        label="Contraseña",
        width=250,
        password=True,
        can_reveal_password=True,
        bgcolor="#333333",
        color="white"
    )
    rol_dropdown = ft.Dropdown(
        label="Rol",
        width=250,
        options=[ft.dropdown.Option("usuario"), ft.dropdown.Option("admin")],
        value="usuario",
        bgcolor="#333333",
        color="white"
    )
    mensaje = ft.Text("", color="green")

    def alta_usuario(e):
        usuario = usuario_input.value.strip()
        contrasena = contrasena_input.value.strip()
        rol = rol_dropdown.value
        if not usuario or not contrasena:
            mensaje.value = "Usuario y contraseña requeridos"
            mensaje.color = "red"
        else:
            try:
                conexion = conectar_mariadb()
                cursor = conexion.cursor()
                cursor.execute(
                    "INSERT INTO usuarios (usuario, contrasena, rol) VALUES (%s, %s, %s)",
                    (usuario, contrasena, rol)
                )
                conexion.commit()
                mensaje.value = f"Usuario '{usuario}' creado con rol '{rol}'"
                mensaje.color = "green"
                usuario_input.value = ""
                contrasena_input.value = ""
                rol_dropdown.value = "usuario"
                actualizar_lista()
                cursor.close()
                conexion.close()
            except Exception as ex:
                mensaje.value = f"Error: {ex}"
                mensaje.color = "red"
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
                ft.Text("Alta/Baja Usuario", size=22, weight="bold"),
                ft.Text("Dar de alta usuario", weight="bold"),
                usuario_input,
                contrasena_input,
                rol_dropdown,
                ft.ElevatedButton(
                    icon=ft.icons.ADD,
                    text="Crear usuario",
                    on_click=alta_usuario,
                    width=250,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=4)),
                    bgcolor="#1976D2",
                    color="white",
                ),
                mensaje,
                ft.Divider(),
                ft.Text("Borrar usuario", weight="bold"),
                borrar_usuario_input,
                ft.ElevatedButton(
                    icon=ft.icons.REMOVE,
                    text="Borrar usuario",
                    on_click=borrar_usuario,
                    width=250,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=4)),
                    bgcolor="red",
                    color="white",
                ),
                mensaje_borrar,
                ft.Divider(),
                ft.Text("Usuarios actuales:", weight="bold"),
                usuarios_view,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        ),
        alignment=ft.alignment.center,
        expand=True,
    )