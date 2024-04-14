import flet as ft


def main(page: ft.Page):

    def play(e):
        pass

    def pause(e):
        pass

    def stop(e):
        pass

    page.theme_mode = 'light'
    page.title = "Player"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(ft.Row(controls=[
        ft.TextButton(text='Play', icon=ft.icons.PLAY_ARROW, on_click=play),
        ft.TextButton(text='Pause', icon=ft.icons.PAUSE, on_click=pause),
        ft.TextButton(text='Stop', icon=ft.icons.STOP, on_click=stop)
    ],
        alignment=ft.MainAxisAlignment.CENTER, scale=2)
    )


ft.app(target=main)
