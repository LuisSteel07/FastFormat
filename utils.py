from enum import Enum
import mimetypes

class Types(Enum):
    Video = 'video'
    Audio = 'audio'

list_resolutions: list[int] = [4320, 2160, 1440, 1080, 720, 480, 360, 240]

def return_type_file(path: str) -> str | None:
    tipo_mime, _ = mimetypes.guess_type(path)
    return tipo_mime

def type_file(path: str) -> Types|None:
    mimetype = return_type_file(path)
    if mimetype.startswith('video'): return Types.Video
    elif mimetype.startswith('audio'): return Types.Audio

    return None