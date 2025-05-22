import flet as ft

from components.FormatOption import FormatOption
from utils import Types, list_resolutions


class FormatPanel:
    def __init__(self, file_type: Types):
        self.file_type = file_type
        self.list_options_resolutions: list[FormatOption] = []

        for resolution in list_resolutions:
            self.list_options_resolutions.append(FormatOption(resolution))

    def show(self) -> ft.Container:
        return ft.Container(
            content=ft.Column(
                controls=[
                    self.create_options(),
                    ft.Button("Convertir", on_click=lambda _: self.print_options())
                ]
            )
        )

    def create_options(self) -> ft.Column:
        options_column =ft.Column()

        for option in self.list_options_resolutions:
            options_column.controls.append(option.show())

        return options_column
