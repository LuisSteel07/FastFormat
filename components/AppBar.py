import flet as ft

app_bar_component = ft.AppBar(
        title=ft.Text("FastFormat"),
        center_title=False,
        bgcolor=ft.Colors.BLUE_GREY_800,
        actions=[
            ft.IconButton(ft.Icons.WB_SUNNY_OUTLINED),
            ft.IconButton(ft.Icons.PLUS_ONE),
            ft.IconButton(ft.Icons.LIST),
            ft.IconButton(ft.Icons.SAVE_AS),
        ],
    )