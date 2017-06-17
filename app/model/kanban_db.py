"""
__File__          = "kanban_db.py"
__Description__   = "Database handling for the whole Kanban board"
__Author__        = "MrChuckomo"
__Version__       = "v1.0.0"
__Creation_Date__ = "15-Jun-2017"
"""

import sqlite3 as Sql
import os

def InitDb():

    if not os.path.isfile("kanban.db"):

        KanbanConnetion = Sql.connect("kanban.db")
        KanbanCursor = KanbanConnetion.cursor()

        KanbanCursor.execute("CREATE TABLE todo(id INT PRIMARY KEY NOT NULL, todotask TEXT NOT NULL)")
        KanbanCursor.execute("CREATE TABLE inprogress(id INT PRIMARY KEY NOT NULL, inprogresstask TEXT NOT NULL)")
        KanbanCursor.execute("CREATE TABLE done(id INT PRIMARY KEY NOT NULL, donetask TEXT NOT NULL)")
        KanbanCursor.execute("CREATE TABLE archives(id INT PRIMARY KEY NOT NULL, archivetask TEXT NOT NULL)")

        KanbanConnetion.close()

def SelectData(_Table):

    KanbanConnetion = Sql.connect("kanban.db")
    KanbanCursor = KanbanConnetion.cursor()

    KanbanCursor.execute("SELECT * FROM " + _Table)

    Data = KanbanCursor.fetchall();

    KanbanConnetion.close()

    return Data

def InsertData(_Table, _Task):

    KanbanConnetion = Sql.connect("kanban.db")
    KanbanCursor = KanbanConnetion.cursor()

    _ExecuteInsertion(KanbanCursor, _Table, _GetLastId(_Table), _Task)

    KanbanConnetion.commit()
    KanbanConnetion.close()


def DeleteData(_Table, _Id):

    KanbanConnetion = Sql.connect("kanban.db")
    KanbanCursor = KanbanConnetion.cursor()

    _ExecuteDeletion(KanbanCursor, _Table, _Id)

    KanbanConnetion.commit()
    KanbanConnetion.close()


def _ExecuteInsertion(_Cursor, _Table, _Id, _Task):

    if _Table == "todo":
        _Cursor.execute("INSERT INTO todo (id, todotask) VALUES (?, ?)", (_Id, _Task,))
    elif _Table == "inprogress":
        _Cursor.execute("INSERT INTO inprogress (id, inprogresstask) VALUES (?, ?)", (_Id, _Task,))
    elif _Table == "done":
        _Cursor.execute("INSERT INTO done (id, donetask) VALUES (?, ?)", (_Id, _Task,))
    elif _Table == "archives":
        _Cursor.execute("INSERT INTO archives (id, archivetask) VALUES (?, ?)", (_Id, _Task,))


def _ExecuteDeletion(_Cursor, _Table, _Id):

    if _Table == "todo":
        _Cursor.execute("DELETE FROM todo WHERE id=" + _Id)
    elif _Table == "inprogress":
        _Cursor.execute("DELETE FROM inprogress WHERE id=" + _Id)
    elif _Table == "done":
        _Cursor.execute("DELETE FROM done WHERE id=" + _Id)
    elif _Table == "archives":
        _Cursor.execute("DELETE FROM archives WHERE id=" + _Id)


# TODO: helper methode for deletion to find id by taskname


def _GetLastId(_Table):

    KanbanConnetion = Sql.connect("kanban.db")
    KanbanCursor = KanbanConnetion.cursor()

    Data = SelectData(_Table)
    Id   = 1;

    if len(Data) > 0:
        Id = (Data[len(Data) - 1][0]) + 1

    KanbanCursor.close()

    return Id
