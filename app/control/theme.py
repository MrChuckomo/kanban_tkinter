"""
File          : theme.py
Description   : 

Author        : MrChuckomo
Version       : v1.0.0
Creation Date : 25-Jun-2017
"""

s_Light = 'theme/macos_light.csv'
s_Dark  = 'theme/macos_dark.csv'


# ---------------------------------------------------------------------------------------------------------------------

def get_theme(theme=s_Light) -> dict:
    """
    Get one of the defined themes as a python dictionary.
    The dictionary gives you easy access to the values by using keywords.

    Args:
    - theme (str) - file path

    Return (dict) a theme file as dictionary.
    """
    File = open(theme, 'r')
    FileContent = str(File.read()).split('\n')
    ThemeDictionary = {}

    for Line in FileContent:
        if Line != '':
            SplitLine = str(Line).split('=')

            Key   = SplitLine[0].strip()
            Value = SplitLine[1].strip()

            ThemeDictionary[str(Key)] = str(Value)

    File.close()

    return ThemeDictionary
