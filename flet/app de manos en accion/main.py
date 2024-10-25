import flet as ft 

conteiner=ft.Container(
    ft.Column([
        ft.Container(
            ft.Text(
                "Iniciar Sesión",
                width=320,
                size=25,
                text_align="center",
                weight="w900",
            ),
            padding=ft.padding.only(20,20)
        ),
        ft.Container(
            ft.TextField(
            hint_text="user",
            read_only="Usuario",
            width=200,
            ),
        ),
    ],
    alignment=ft.MainAxisAlignment.SPACE_EVENLY
    ),

    border_radius=20,
    width=350,
    height=600,
    bgcolor='#ff0000',
)

def main(page:ft.page):
    page.vertical_alignment="center"
    page.horizontal_alignment="center"
    page.add(conteiner)
    

ft.app(target=main)