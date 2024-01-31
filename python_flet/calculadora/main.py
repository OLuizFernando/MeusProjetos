import flet as ft


def main(page: ft.Page):

    page.title = 'Calculadora'
    page.theme_mode = 'light'
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.window_height = 600
    page.window_width = 400

    display = ft.TextField(read_only=True, value=0, text_align='right', height=100)

    page.add(
        display,
        ft.Row(controls=[
            ft.ElevatedButton(text=7, height=100, width=100),
            ft.ElevatedButton(text=8, height=100, width=100),
            ft.ElevatedButton(text=9, height=100, width=100)
        ], alignment=ft.MainAxisAlignment.SPACE_AROUND),

        ft.Row(controls=[
            ft.ElevatedButton(text=4, height=100, width=100),
            ft.ElevatedButton(text=5, height=100, width=100),
            ft.ElevatedButton(text=6, height=100, width=100)
        ], alignment=ft.MainAxisAlignment.SPACE_AROUND),

        ft.Row(controls=[
            ft.ElevatedButton(text=1, height=100, width=100),
            ft.ElevatedButton(text=2, height=100, width=100),
            ft.ElevatedButton(text=3, height=100, width=100)
        ], alignment=ft.MainAxisAlignment.SPACE_AROUND),

        ft.Row(controls=[
            ft.FilledTonalButton(text='-', height=100, width=100),
            ft.ElevatedButton(text=0, height=100, width=100),
            ft.FilledTonalButton(text='+', height=100, width=100)
        ], alignment=ft.MainAxisAlignment.SPACE_AROUND)
    )


ft.app(target=main)