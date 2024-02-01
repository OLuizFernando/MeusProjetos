import flet as ft


class Calculadora(ft.UserControl):

    def build(self):

        self.reset()
        self.display = ft.TextField(read_only=True, value='0', text_align=ft.TextAlign.RIGHT, height=70, width=330)

        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(controls=[
                        self.display,
                        ft.FilledButton(text='=', height=100, width=100, data='=', on_click=self.click)
                    ], alignment=ft.MainAxisAlignment.SPACE_AROUND),

                    ft.Row(controls=[
                        ft.FilledTonalButton(text='7', height=100, width=100, data='7', on_click=self.click),
                        ft.FilledTonalButton(text='8', height=100, width=100, data='8', on_click=self.click),
                        ft.FilledTonalButton(text='9', height=100, width=100, data='9', on_click=self.click),
                        ft.ElevatedButton(text='+', height=100, width=100, elevation=5, data='+', on_click=self.click)
                    ], alignment=ft.MainAxisAlignment.SPACE_AROUND),

                    ft.Row(controls=[
                        ft.FilledTonalButton(text='4', height=100, width=100, data='4', on_click=self.click),
                        ft.FilledTonalButton(text='5', height=100, width=100, data='5', on_click=self.click),
                        ft.FilledTonalButton(text='6', height=100, width=100, data='6', on_click=self.click),
                        ft.ElevatedButton(text='-', height=100, width=100, elevation=5, data='-', on_click=self.click)
                    ], alignment=ft.MainAxisAlignment.SPACE_AROUND),

                    ft.Row(controls=[
                        ft.FilledTonalButton(text='1', height=100, width=100, data='1', on_click=self.click),
                        ft.FilledTonalButton(text='2', height=100, width=100, data='2', on_click=self.click),
                        ft.FilledTonalButton(text='3', height=100, width=100, data='3', on_click=self.click),
                        ft.ElevatedButton(text='×', height=100, width=100, elevation=5, data='*', on_click=self.click)
                    ], alignment=ft.MainAxisAlignment.SPACE_AROUND),

                    ft.Row(controls=[
                        ft.FilledButton(text='C', height=100, width=100, data='C', on_click=self.click),
                        ft.FilledTonalButton(text='0', height=100, width=100, data='0', on_click=self.click),
                        ft.ElevatedButton(text='.', height=100, width=100, elevation=5, data='.', on_click=self.click),
                        ft.ElevatedButton(text='÷', height=100, width=100, elevation=5, data='/', on_click=self.click)
                    ], alignment=ft.MainAxisAlignment.SPACE_AROUND)
                ]
            )
        )

    def click(self, e):
        data = e.control.data
        if data == 'C' or self.display.value == 'Erro':
            self.display.value = '0'
            self.reset()

        elif data in ['+', '-', '*', '/']:
            self.display.value = self.calcular(
                self.parte1, float(self.display.value), self.operacao
            )
            self.operacao = data
            if self.display.value == 'Erro':
                self.parte1 = '0'
            else:
                self.parte1 = float(self.display.value)
            self.nova_parte = True

        elif data == '=':
            self.display.value = self.calcular(
                self.parte1, float(self.display.value), self.operacao
            )
            self.reset()

        else:
            if self.display.value == '0' or self.nova_parte == True:
                self.display.value = data
                self.nova_parte = False
            else:
                self.display.value += data

        self.update()

    def formatar(self, num):
        try:
            return int(num)
        except ValueError:
            return float(num)

    def calcular(self, parte1, parte2, operacao):
        if operacao == '+':
            return self.formatar(parte1 + parte2)
        elif operacao == '-':
            return self.formatar(parte1 - parte2)
        elif operacao == '*':
            return self.formatar(parte1 * parte2)
        elif operacao == '/':
            if parte2 == 0:
                return 'Erro'
            else:
                return self.formatar(parte1 / parte2)

    def reset(self):
        self.operacao = '+'
        self.parte1 = 0
        self.nova_parte = True


def main(page: ft.Page):
    page.title = 'Calculadora'
    page.theme_mode = 'light'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_height = 600
    page.window_width = 500

    calculadora = Calculadora()
    page.add(calculadora)


ft.app(target=main)