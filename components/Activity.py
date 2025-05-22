import flet as ft
from utils import Types


class Activity:
    def __init__(self, name: str, path: str, file_type: Types|None):
        self.name = name
        self.path = path
        self.type = file_type

        if self.type is not None:
            if self.type.value == 'video': self.icon = ft.Icon(name=ft.Icons.VIDEO_FILE)
            if self.type.value == 'audio': self.icon = ft.Icon(name=ft.Icons.AUDIO_FILE)

    def show_activity(self) -> ft.Row:
        return ft.Row(
            [
                self.icon,
                ft.Text(self.name),
            ]
        )
