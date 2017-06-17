"""
__File__          = "main.py"
__Description__   = ""
__Author__        = "MrChuckomo"
__Version__       = "v1.0.0"
__Creation_Date__ = "15-Jun-2017"
"""

from view import board as BoardGui
from model import kanban_db as Db

Db.InitDb()

# Db.InsertData(_Table="todo", _Task="Use SQLite to save data")
# Db.InsertData(_Table="todo", _Task="Change color scheme")
# Db.InsertData(_Table="inprogress", _Task="Develop pyhton Kanban board")

BoardGui.drawWindow()
