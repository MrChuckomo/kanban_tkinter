"""
__File__          = "components.py"
__Description__   = ""
__Author__        = "MrChuckomo"
__Version__       = "v1.0.0"
__Creation_Date__ = "16-Jun-2017"
"""

from Tkinter  import * 
from view import color as Color

s_DefaultFont = ("Helvetica", "16")

def GetList(_Root, _FgColor=Color.s_LightWhite):
    return Listbox\
    (
        _Root,
        bg=Color.s_DarkBlack,
        fg=_FgColor,
        bd=0,
        font=s_DefaultFont
    )

def GetLabelFrame(_Root, _Text, _FgColor=Color.s_LightWhite):
    return LabelFrame\
    (
        _Root,
        text=_Text,
        bg=Color.s_DarkBlack,
        fg=_FgColor,
        font=s_DefaultFont
    )

def GetFrame(_Root):
    return Frame\
    (
        _Root,
        bg=Color.s_DarkBlack
    )

def GetEntry(_Root):
    return Entry\
    (
        _Root,
        bg=Color.s_DarkBlack,
        fg=Color.s_LightWhite,
        font=s_DefaultFont
    )

def GetButton(_Root, _Text, _Command=0):
    return Button\
    (
        _Root,
        text=_Text,
        command=_Command,
        bg=Color.s_DarkBlack,
        fg=Color.s_LightWhite,

    )