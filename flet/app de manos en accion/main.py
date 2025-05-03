import flet as ft
from db import conectar_mariadb  # Importar la conexión a la base de datos
from home import home_page  # Importar la página principal
from categoria import categoria_page  # Importar la página de categorías

def main(page: ft.Page):  
    def route_change(event):
        print(f"Ruta actual: {event.route}")  # Depuración
        if event.route.startswith("/categoria/"):
            categoria = event.route.split("/categoria/")[1]
            print(f"Categoría seleccionada: {categoria}")  # Depuración
            page.views.clear()
            page.views.append(ft.View(route=event.route, controls=[categoria_page(page, categoria)]))
        elif event.route == "/home":
            print("Navegando a la página principal")  # Depuración
            page.views.clear()
            page.views.append(ft.View(route="/home", controls=[home_page(page)]))
        else:
            print("Navegando a la página de inicio de sesión")  # Depuración
            page.views.clear()
            page.views.append(ft.View(route="/", controls=[
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Iniciar Sesión", size=25, weight="bold", text_align="center"),
                            usuario_input,
                            contrasena_input,
                            ft.ElevatedButton(
                                "Iniciar Sesión",
                                on_click=verificar_credenciales,
                                width=300,
                                bgcolor="blue",
                                color="white",
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    alignment=ft.alignment.center,
                    expand=True,
                )
            ]))
        page.update()

    def verificar_credenciales(e):
        usuario = usuario_input.value
        contrasena = contrasena_input.value

        try:
            # Conectar a la base de datos
            conexion = conectar_mariadb()
            if conexion is None:
                page.snack_bar = ft.SnackBar(ft.Text("No se pudo conectar a la base de datos"), bgcolor="red")
                page.snack_bar.open = True
                page.update()
                return

            cursor = conexion.cursor()

            # Consulta para verificar las credenciales
            consulta = "SELECT * FROM usuarios WHERE usuario = %s AND contrasena = %s"
            cursor.execute(consulta, (usuario, contrasena))
            resultado = cursor.fetchone()

            if resultado:
                print("Inicio de sesión exitoso")  # Depuración
                page.go("/home")
            else:
                print("Credenciales incorrectas")  # Depuración
                page.snack_bar = ft.SnackBar(ft.Text("Usuario o contraseña incorrectos"), bgcolor="red")
                page.snack_bar.open = True
                page.update()

            # Cerrar la conexión
            cursor.close()
            conexion.close()
        except mysql.connector.Error as err:
            print(f"Error de conexión: {err}")
            page.snack_bar = ft.SnackBar(ft.Text(f"Error de conexión: {err}"), bgcolor="red")
            page.snack_bar.open = True
            page.update()

    # Campos de entrada
    usuario_input = ft.TextField(
        hint_text="Usuario",
        width=300,
    )
    contrasena_input = ft.TextField(
        hint_text="Contraseña",
        width=300,
        password=True,
        can_reveal_password=True,
    )

    # Configurar el manejador de rutas
    page.on_route_change = route_change
    page.go("/")  # Ruta inicial
    page.update()

ft.app(target=main)