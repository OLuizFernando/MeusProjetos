import flet as ft


def main(page: ft.Page):

    page.title = 'Teste'
    page.theme_mode = 'light'

    def criar_tarefa(e):
        page.add(ft.Checkbox(label=caixa_texto.value))
        caixa_texto.value = ''
        caixa_texto.focus()
        page.update()

    caixa_texto = ft.TextField(label='Nova Tarefa')
    botao = ft.ElevatedButton(text='Adicionar', icon=ft.icons.ADD, height=50, on_click=criar_tarefa)

    page.add(
        ft.Row(controls=[
            caixa_texto, botao
        ], height=70)
    )


ft.app(target=main)