import flet as ft


class FormatOption:
    def __init__(self, option: int):
        self.option = option
        self.checkbox_option = ft.Checkbox()

    def show(self) -> ft.Row:
        return ft.Row(
            controls=[
                self.checkbox_option,
                ft.Text(f"{self.option}")
            ]
        )
