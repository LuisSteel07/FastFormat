import flet as ft

from components.Activity import Activity
from components.AppBar import app_bar_component
from utils import type_file, Types

class PrincipalView(ft.View):
    def __init__(self, root: ft.Page):
        super().__init__()
        self.root = root
        self.route = "/"
        self.list_activities: list[Activity] = []
        self.tasks = ft.Column()
        self.results = ft.Column()
        self.add_activity = ft.FilePicker(on_result=self.create_activity)
        self.root.overlay.append(self.add_activity)

        self.controls = [
            app_bar_component,
            ft.Column(
                controls=[
                    ft.ElevatedButton(
                        "Buscar Archivos",
                        icon=ft.Icons.UPLOAD_FILE,
                        on_click=lambda _: self.add_activity.pick_files(allow_multiple=True),
                    ),
                    ft.Row(
                        [
                            self.tasks,
                            self.results
                        ]
                    )
                ],
                horizontal_alignment=ft.alignment.center
            )
        ]

    def create_activity(self, e: ft.FilePickerResultEvent):
        if len(e.files) > 1:
            for f in e.files:
                if type_file(f.path) == Types.Video or type_file(f.path) == Types.Audio:
                    activity = Activity(f.name, f.path, type_file(f.path))
                    self.list_activities.append(activity)
                    self.tasks.controls.append(activity.show_activity())
        else:
            if type_file(e.files[0].path) == Types.Video or type_file(e.files[0].path) == Types.Audio:
                activity = Activity(e.files[0].name, e.files[0].path, type_file(e.files[0].path))
                self.list_activities.append(activity)
                self.tasks.controls.append(activity.show_activity())

        self.root.update()