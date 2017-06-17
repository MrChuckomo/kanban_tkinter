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

def GetList(_Root, _BgColor=Color.s_LightWhite, _FgColor=Color.s_DarkBlack, _SelectColor=Color.s_LightBlack):
    return Listbox\
    (
        _Root,
        bg=_BgColor,
        fg=_FgColor,
        bd=0,
        font=s_DefaultFont,
        selectbackground=_SelectColor
    )

def GetLabelFrame(_Root, _Text, _BgColor=Color.s_LightWhite, _FgColor=Color.s_LightWhite):
    return LabelFrame\
    (
        _Root,
        text=_Text,
        bg=_BgColor,
        fg=_FgColor,
        font=s_DefaultFont
    )

def GetFrame(_Root):
    return Frame\
    (
        _Root,
        bg=Color.s_DarkBlack
    )

def GetEntry(_Root, _BgColor=Color.s_DarkWhite, _HighlightColor=Color.s_LightWhite, _FgColor=Color.s_DarkBlack):
    return Entry\
    (
        _Root,
        bg=_BgColor,
        fg=_FgColor,
        font=s_DefaultFont,
        highlightbackground=_HighlightColor
    )

def GetButton(_Root, _Text, _Command=0, _HighlightColor=Color.s_LightWhite):
    return Button\
    (
        _Root,
        text=_Text,
        command=_Command,
        bg=Color.s_DarkBlack,
        fg=Color.s_LightWhite,
        highlightbackground=_HighlightColor
    )