import flet as ft

def admin_page(page: ft.Page):
    return ft.Column(
        [
            ft.Text("Panel de administración", size=25, weight="bold"),
            ft.ElevatedButton(
                "Alta/Baja Usuario",
                icon=ft.icons.PERSON_ADD,
                bgcolor="#FF9800",
                color="white",
                on_click=lambda _: page.go("/admin/usuarios"),
            ),
            # Aquí puedes agregar más botones para otras páginas del admin
            ft.ElevatedButton("Regresar", on_click=lambda _: page.go("/home")),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )