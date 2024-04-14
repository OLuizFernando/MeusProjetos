import flet as ft


def main(page: ft.Page):

    def mostrar_cadastro(e):
        if email.value != '' and senha.value != '':
            print(f'E-mail: {email.value}')
            print(f'Senha:  {senha.value}')
        else:
            print('Cadastro Inválido')

    page.theme_mode = 'light'
    page.title = 'Cadastro'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    email = ft.TextField(label='E-mail:')
    senha = ft.TextField(label='Senha', password=True, can_reveal_password=True)

    botao = ft.FilledTonalButton(text='Cadastrar', height=50, on_click=mostrar_cadastro)

    page.add(email, senha, botao)


ft.app(target=main)