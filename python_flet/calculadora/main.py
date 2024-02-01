import flet as ft


class Calculadora(ft.UserControl):

    def build(self):

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
                        ft.ElevatedButton(text='×', height=100, width=100, elevation=5, data='×', on_click=self.click)
                    ], alignment=ft.MainAxisAlignment.SPACE_AROUND),

                    ft.Row(controls=[
                        ft.FilledButton(text='C', height=100, width=100, data='C', on_click=self.click),
                        ft.FilledTonalButton(text='0', height=100, width=100, data='0', on_click=self.click),
                        ft.ElevatedButton(text='.', height=100, width=100, elevation=5, data='.', on_click=self.click),
                        ft.ElevatedButton(text='÷', height=100, width=100, elevation=5, data='÷', on_click=self.click)
                    ], alignment=ft.MainAxisAlignment.SPACE_AROUND)
                ]
            )
        )

    def click(self, e):
        if e.control.data == 'C':
            self.display.value = '0'
            self.parte1 = self.parte2 = 0

        elif e.control.data in ['+', '-', '×', '÷']:
            self.operacao = e.control.data
            try:
                self.parte1 = int(self.display.value)
            except ValueError:
                self.parte1 = float(self.display.value)
            self.display.value = '0'

        elif self.display.value == '0':
            self.display.value = e.control.data

        elif e.control.data == '=':
            try:
                self.parte2 = int(self.display.value)
            except ValueError:
                self.parte2 = float(self.display.value)

            if self.operacao == '+':
                self.display.value = str(self.parte1 + self.parte2)
            elif self.operacao == '-':
                self.display.value = str(self.parte1 - self.parte2)
            elif self.operacao == '×':
                self.display.value = str(self.parte1 * self.parte2)
            elif self.operacao == '÷':
                self.display.value = str(self.parte1 / self.parte2)

        else:
            self.display.value += e.control.data
        self.update()


def main(page: ft.Page):
    page.title = 'Calculadora'
    page.theme_mode = 'light'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_height = 600
    page.window_width = 500

    calculadora = Calculadora()
    page.add(calculadora)


ft.app(target=main)