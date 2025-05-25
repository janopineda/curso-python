import flet as ft
from db import obtener_categorias
from busqueda import filtrar_categorias

def home_page(page: ft.Page):
    listaCategorias = obtener_categorias()
    # Manejo seguro de la sesión
    if hasattr(page, "session") and page.session is not None:
        rol = page.session.get("rol")
        if rol is None:
            rol = "usuario"
    else:
        rol = "usuario"
    print("ROL ACTUAL:", rol)  # Depuración

    search_field = ft.TextField(
        hint_text="Buscar categoría...",
        dense=True,
        expand=True,  # Hace el campo responsivo
        on_change=lambda e: page.update(),
    )

    def ir_a_busqueda(e):
        page.go(f"/busqueda/{search_field.value}")

    # Botón menú admin (solo para admins)
    admin_menu_button = None
    if rol == "admin":
        admin_menu_button = ft.IconButton(
            icon=ft.icons.MENU,
            icon_color="white",
            bgcolor="#FF9800",  # Naranja
            tooltip="Panel de administración",
            on_click=lambda _: page.go("/admin"),
            style=ft.ButtonStyle(shape=ft.CircleBorder()),
        )

    return ft.Column(
        [
            ft.Row(
                [
                    ft.Container(expand=True),  # Empuja el botón a la derecha
                    *( [admin_menu_button] if admin_menu_button else [] ),
                ],
                alignment=ft.MainAxisAlignment.END,
            ),
            ft.Container(
                content=ft.Image(
                    src="imagenes/logo.png",
                    width=250,
                    fit=ft.ImageFit.CONTAIN,
                ),
                alignment=ft.alignment.center,
            ),
            ft.Container(
                content=ft.Row(
                    [
                        search_field,
                        ft.IconButton(
                            icon=ft.icons.SEARCH,
                            icon_color="white",
                            bgcolor="#FF6F00",
                            tooltip="Buscar",
                            on_click=ir_a_busqueda,
                            style=ft.ButtonStyle(shape=ft.CircleBorder()),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    expand=True,  # Hace la fila responsiva
                ),
                alignment=ft.alignment.center,
                padding=ft.padding.only(bottom=10),
            ),
            ft.Container(
                content=ft.ListView(
                    [
                        ft.ElevatedButton(
                            content=ft.Row(
                                [
                                    ft.Icon(ft.icons.ARROW_FORWARD, color="white"),
                                    ft.Text(f"{coleccion}", color="white", weight="bold"),
                                ],
                                alignment=ft.MainAxisAlignment.START,
                            ),
                            bgcolor="#FF6F00",
                            color="white",
                            width=300,
                            on_click=lambda e, categoria=coleccion: page.go(f"/categoria/{categoria}"),
                        )
                        for coleccion in sorted(
                            filtrar_categorias(listaCategorias, search_field.value),
                            key=lambda x: x.lower()
                        )
                    ],
                    expand=True,
                    spacing=10,
                ),
                expand=True,
            ),
            ft.IconButton(
                icon=ft.icons.LOGOUT,
                icon_color="red",
                tooltip="Cerrar sesión",
                on_click=lambda _: page.go("/"),
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )