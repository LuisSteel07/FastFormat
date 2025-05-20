import flet as ft
from components.Activity import Activity
from utils import type_file, Types


def main(page: ft.Page):
    page.title = "FastFormat"

    page.appbar = ft.AppBar(
        title=ft.Text("PyTraductor"),
        center_title=False,
        bgcolor=ft.Colors.BLUE_GREY_800,
        actions=[
            ft.IconButton(ft.Icons.WB_SUNNY_OUTLINED),
            ft.IconButton(ft.Icons.PLUS_ONE),
            ft.IconButton(ft.Icons.LIST),
            ft.IconButton(ft.Icons.SAVE_AS),
        ],
    )

    list_activities: list[Activity] = []
    def create_activity(e: ft.FilePickerResultEvent):
        if len(e.files) > 1:
            for f in e.files:
                if type_file(f.path) == Types.Video or type_file(f.path) == Types.Audio:
                    activity = Activity(f.name, f.path, type_file(f.path))
                    list_activities.append(activity)
                    tasks.controls.append(activity.show_activity())
        else:
            if type_file(e.files[0].path) == Types.Video or type_file(e.files[0].path) == Types.Audio:
                activity = Activity(e.files[0].name, e.files[0].path, type_file(e.files[0].path))
                list_activities.append(activity)
                tasks.controls.append(activity.show_activity())

        page.update()

    add_activity = ft.FilePicker(on_result=create_activity)
    tasks = ft.Column()
    results = ft.Column()

    page.overlay.append(add_activity)

    principal_main = ft.Column(
        controls=[
            ft.ElevatedButton(
                "Buscar Archivos",
                icon=ft.Icons.UPLOAD_FILE,
                on_click=lambda _: add_activity.pick_files(allow_multiple=True),
            ),
            ft.Row(
                [
                    tasks,
                    results
                ]
            )
        ],
        horizontal_alignment=ft.alignment.center
    )

    page.add(principal_main)
    page.update()

ft.app(main)