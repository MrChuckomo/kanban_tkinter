"""
__File__          = "components.py"
__Description__   = ""
__Author__        = "MrChuckomo"
__Version__       = "v1.0.0"
__Creation_Date__ = "16-Jun-2017"
"""


from tkinter import Listbox, LabelFrame, Frame, Entry, Button
from view import color as Color

# / --------------------------------------------------------------------------------------------------------------------


class CTkComponents:

    def __init__(self, _Theme):
        self.m_DefaultFont = ("Helvetica", "16")
        self.m_Theme = _Theme

    def GetList(self, _Root, _BgColor=Color.s_LightGrey, _FgColor=Color.s_DarkBlack, _SelectColor=Color.s_DarkGrey):
        return Listbox(_Root,
                       bg=_BgColor,
                       fg=_FgColor,
                       bd=0,
                       font=self.m_DefaultFont,
                       selectbackground=_SelectColor)

    def GetLabelFrame(self, _Root, _Text, _BgColor=Color.s_LightGrey, _FgColor=Color.s_DarkBlack):
        return LabelFrame(_Root,
                          text=_Text,
                          bg=_BgColor,
                          fg=_FgColor,
                          font=self.m_DefaultFont)

    def GetFrame(self, _Root, _BgColor=Color.s_LightGrey):
        return Frame(_Root,
                     bg=_BgColor)

    def GetEntry(self, _Root, _BgColor=Color.s_LightWhite, _HighlightColor=Color.s_LightGrey, _FgColor=Color.s_DarkBlack):
        return Entry(_Root,
                     bg=_BgColor,
                     fg=_FgColor,
                     font=self.m_DefaultFont,
                     highlightbackground=_HighlightColor)

    def GetButton(self, _Root, _Text, _Command=0, _HighlightColor=Color.s_LightGrey):
        return Button(_Root,
                      text=_Text,
                      command=_Command,
                      bg=Color.s_DarkBlack,
                      fg=Color.s_LightWhite,
                      highlightbackground=_HighlightColor)
