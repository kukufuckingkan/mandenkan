from __future__ import division
import scipy.constants as const
import scipy
from scipy.io import wavfile
from IPython.core.display import HTML

def player(filePath:str,env:str) -> None:
    path = getPath(filePath,env)
    """ will display html 5 player for compatible browser

    Parameters :
    ------------
    filepath : relative filepath with respect to the notebook directory ( where the .ipynb are not cwd)
               of the file to play

    The browser need to know how to play wav through html5.

    there is no autoplay to prevent file playing when the browser opens
    """
    
    src = """
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>Simple Test</title>
    </head>
    
    <body>
    <audio controls="controls" style="width:250px" >
      <source src="files/%s" type="audio/wav" />
      Your browser does not support the audio element.
    </audio>
    </body>
    """%(path)
    display(HTML(src))


def getPath(path:str,env: str) -> str:
    PATH_RESOURCE = '/resource'
    
    if PATH_RESOURCE in path and 'DEV' == env:
        return path.replace(PATH_RESOURCE,'')
    return path

    
    
    