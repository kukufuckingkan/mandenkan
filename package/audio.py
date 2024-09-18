
from IPython.core.display import HTML
import pandas as pd
from IPython.display import HTML
from package import audio

def player(filePath: str, env: str) -> str:
    path = getPath(filePath, env)
    
    # HTML for the audio player without newlines
    audio_html = '''<audio controls style="width:150px">
                      <source src="{}" type="audio/mpeg">
                      Your browser does not support the audio element.
                    </audio>'''.format(path)
    
    return audio_html


def getPath(path:str,env: str) -> str:
    PATH_RESOURCE = '/resource'
    
    if PATH_RESOURCE in path and 'DEV' == env:
        return path.replace(PATH_RESOURCE,'')
    return path

    
    
    