"""
__File__          = "theme.py"
__Description__   = ""
__Author__        = "MrChuckomo"
__Version__       = "v1.0.0"
__Creation_Date__ = "25-Jun-2017"
"""


# / ----------------------------------------------------------------------------


s_Light = "theme/macos_light.csv"
s_Dark  = "theme/macos_dark.csv"


# / ----------------------------------------------------------------------------


"""@package docstring
    Function: GetTheme

    Get one of the defined themes as a python dictionary.
    The dictionary gives you easy access to the values by using keywords.

    Parameter:

        _Theme = file path

    Return:

        Return a theme file as dictionary array.
"""


def GetTheme(_Theme=s_Light):

    File = open(_Theme, "r")

    FileContent = str(File.read()).split("\n")
    ThemeDictionary = {}

    for Line in FileContent:

        if Line != "":

            SplitLine = str(Line).split("=")

            Key   = SplitLine[0].strip()
            Value = SplitLine[1].strip()

            ThemeDictionary[str(Key)] = str(Value)

    File.close()

    return ThemeDictionary

# / ----------------------------------------------------------------------------
