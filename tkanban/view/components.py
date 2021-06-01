"""
File          : components.py
Description   : 

Author        : MrChuckomo
Version       : v1.0.0
Creation Date : 16-Jun-2017
"""

from tkanban.view import color as Color
from tkanban.view.color import EColor
from tkinter import Listbox, LabelFrame, Frame, Entry, Button


# ---------------------------------------------------------------------------------------------------------------------

class CTkComponents():

    def __init__(self, theme):
        self.default_font = ('Helvetica', '16')
        self.theme = theme

    def GetList(self, root, bg_color=EColor.LIGHTGREY, fg_color=EColor.DARKBLACK, select_color=EColor.DARKGREY):
        return Listbox(
            root,
            bg=bg_color.value,
            fg=fg_color.value,
            bd=0,
            font=self.default_font,
            selectbackground=select_color.value
        )

    def GetLabelFrame(self, root, _Text, bg_color=EColor.LIGHTGREY, fg_color=EColor.DARKBLACK):
        return LabelFrame(
            root,
            text=_Text,
            bg=bg_color.value,
            fg=fg_color.value,
            font=self.default_font
        )

    def GetFrame(self, root, bg_color=EColor.LIGHTGREY):
        return Frame(
            root,
            bg=bg_color.value
        )

    def GetEntry(self, root, bg_color=EColor.LIGHTWHITE, fg_color=EColor.DARKBLACK, highlight_color=EColor.LIGHTGREY):
        return Entry(
            root,
            bg=bg_color.value,
            fg=fg_color.value,
            font=self.default_font,
            highlightbackground=highlight_color.value
        )

    def GetButton(self, root, text, cmd=0, highlight_color=EColor.LIGHTGREY):
        return Button(
            root,
            text=text,
            command=cmd,
            bg=EColor.DARKBLACK.value,
            fg=EColor.LIGHTWHITE.value,
            highlightbackground=highlight_color.value
        )
