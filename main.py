"""
__File__          = "main.py"
__Description__   = ""
__Author__        = "MrChuckomo"
__Version__       = "v1.0.0"
__Creation_Date__ = "15-Jun-2017"
"""

from tkanban.view import board as BoardGui
from tkanban.model import kanban_db as Db

Db.InitDb()

BoardGui.drawWindow()
