import flet as ft
from components.AppBar import app_bar_component
from utils import Types
from views.ConversionView import ConversionView
from views.PrincipalView import PrincipalView


def main(page: ft.Page):
    page.title = "FastFormat"
    page.appbar = app_bar_component
    principal_view = PrincipalView(page)
    conversion_view = ConversionView(page, Types.Video)

    def route_change(e: ft.RouteChangeEvent):
        page.views.clear()
        page.views.append(principal_view)
        if page.route == "/conversion_view":
            page.views.append(conversion_view)
        page.update()

    def view_pop():
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    page.add()
    page.update()

ft.app(main)