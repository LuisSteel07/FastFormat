import flet as ft

from components.FormatPanel import FormatPanel
from utils import Types

fp_video = FormatPanel(Types.Video)
fp_audio = FormatPanel(Types.Audio)

class ConversionView(ft.View):
    def __init__(self, root: ft.Page, type_file: Types):
        super().__init__()
        self.root = root
        self.route = "/conversion_view"

        self.controls.append(ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda _: self.root.go("/")))

        if type_file == Types.Video:
            self.controls.append(fp_video.show())
        elif type_file == Types.Audio:
            self.controls.append(fp_audio.show())