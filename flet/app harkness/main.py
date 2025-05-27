import flet as ft
import mysql.connector
from db import conectar_mariadb
from home import home_page
from categoria import categoria_page
from busqueda import busqueda_page
from admin import admin_page
from admin_usuarios import admin_usuarios_page
from admin_categorias import admin_categorias_page  # <-- Importa la nueva sección

def main(page: ft.Page):
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

    def verificar_credenciales(e):
        usuario = usuario_input.value
        contrasena = contrasena_input.value

        if not usuario or not contrasena:
            page.snack_bar = ft.SnackBar(ft.Text("Completa ambos campos"), bgcolor="red")
            page.snack_bar.open = True
            page.update()
            return

        try:
            conexion = conectar_mariadb()
            if conexion is None:
                page.snack_bar = ft.SnackBar(ft.Text("No se pudo conectar a la base de datos"), bgcolor="red")
                page.snack_bar.open = True
                page.update()
                return

            cursor = conexion.cursor()
            consulta = "SELECT usuario, rol FROM usuarios WHERE usuario = %s AND contrasena = %s"
            cursor.execute(consulta, (usuario, contrasena))
            resultado = cursor.fetchone()

            if resultado:
                usuario_log, rol = resultado
                page.session.set("usuario", usuario_log)
                page.session.set("rol", rol)
                print(f"Inicio de sesión exitoso como {rol}")
                page.go("/home")
            else:
                print("Credenciales incorrectas")
                page.snack_bar = ft.SnackBar(ft.Text("Usuario o contraseña incorrectos"), bgcolor="red")
                page.snack_bar.open = True
                page.update()

            cursor.close()
            conexion.close()
        except mysql.connector.Error as err:
            print(f"Error de conexión: {err}")
            page.snack_bar = ft.SnackBar(ft.Text(f"Error de conexión: {err}"), bgcolor="red")
            page.snack_bar.open = True
            page.update()

    def route_change(event):
        print(f"Ruta actual: {event.route}")
        if event.route.startswith("/categoria/"):
            categoria = event.route.split("/categoria/")[1]
            print(f"Categoría seleccionada: {categoria}")
            page.views.clear()
            page.views.append(ft.View(route=event.route, controls=[categoria_page(page, categoria)]))
        elif event.route == "/home":
            print("Navegando a la página principal")
            page.views.clear()
            page.views.append(ft.View(route="/home", controls=[home_page(page)]))
        elif event.route.startswith("/busqueda/"):
            texto = event.route.split("/busqueda/")[1]
            page.views.clear()
            page.views.append(ft.View(route=event.route, controls=[busqueda_page(page, texto)]))
        elif event.route == "/admin":
            page.views.clear()
            page.views.append(ft.View(route="/admin", controls=[admin_page(page)]))
        elif event.route == "/admin/usuarios":
            page.views.clear()
            page.views.append(ft.View(route="/admin/usuarios", controls=[admin_usuarios_page(page)]))
        elif event.route == "/admin/categorias":  # <-- Nueva ruta para categorías
            page.views.clear()
            page.views.append(ft.View(route="/admin/categorias", controls=[admin_categorias_page(page)]))
        else:
            print("Navegando a la página de inicio de sesión")
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

    page.on_route_change = route_change
    page.go("/")
    page.update()

ft.app(target=main)