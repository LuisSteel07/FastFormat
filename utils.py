from enum import Enum
import mimetypes

class Types(Enum):
    Video = 'video'
    Audio = 'audio'

def return_type_file(path: str) -> str | None:
    tipo_mime, _ = mimetypes.guess_type(path)
    return tipo_mime

def type_file(path: str) -> Types|None:
    mimetype = return_type_file(path)
    if mimetype.startswith('video'): return Types.Video
    elif mimetype.startswith('audio'): return Types.Audio

    return None