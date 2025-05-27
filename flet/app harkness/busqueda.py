import flet as ft
from db import obtener_categorias

def filtrar_categorias(lista, texto):
    texto = texto.lower()
    return [cat for cat in lista if texto in cat.lower()]

def busqueda_page(page: ft.Page, texto_busqueda: str):
    listaCategorias = obtener_categorias()
    resultados = filtrar_categorias(listaCategorias, texto_busqueda)
    resultados_ordenados = sorted(resultados, key=lambda x: x.lower())
    return ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.IconButton(
                            icon=ft.icons.CLOSE,
                            icon_color="red",
                            tooltip="Regresar",
                            on_click=lambda _: page.go("/home"),
                        )
                    ],
                    alignment=ft.MainAxisAlignment.END,
                ),
                ft.Text(f'Resultados para: "{texto_busqueda}"', size=20, weight="bold"),
                *(
                    [
                        ft.Text("No se encontró ese país.", color="red", size=18, weight="bold")
                    ] if not resultados_ordenados else [
                        ft.ElevatedButton(
                            content=ft.Row([
                                ft.Icon(ft.icons.ARROW_FORWARD, color="white"),
                                ft.Text(cat, color="white", weight="bold"),
                            ]),
                            bgcolor="#FF6F00",
                            color="white",
                            width=300,
                            on_click=lambda e, categoria=cat: page.go(f"/categoria/{categoria}"),
                        )
                        for cat in resultados_ordenados
                    ]
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        ),
        alignment=ft.alignment.center,
        expand=True,
    )