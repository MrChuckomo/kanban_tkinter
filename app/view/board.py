"""
__File__          = "board.py"
__Description__   = ""
__Author__        = "MrChuckomo"
__Version__       = "v1.0.0"
__Creation_Date__ = "15-Jun-2017"
"""
# / ---------------------------------------------------------------------------------------------------

import sys
sys.path.append("../")

from Tkinter import *
from view import components as Widget
from view import color as Color
from model import kanban_db as Db

# / ---------------------------------------------------------------------------------------------------

s_List = ["todo", "in_progress", "done", "archives"]

def drawWindow():

    def LoadData():

        for Row in Db.SelectData("todo"):
            ToDoList.insert(END, Row[1])
        for Row in Db.SelectData("inprogress"):
            InProgressList.insert(END, Row[1])
        for Row in Db.SelectData("done"):
            DoneList.insert(END, Row[1])

    def Add(_List):

        if _List == s_List[0] and ToDoEntry.get() != "":
            ToDoList.insert(END, ToDoEntry.get())
            ToDoEntry.delete(0, END)
        elif _List == s_List[1] and InProgressEntry.get() != "":
            InProgressList.insert(END, InProgressEntry.get())
            InProgressEntry.delete(0, END)
        elif _List == s_List[2] and DoneEntry.get() != "":
            DoneList.insert(END, DoneEntry.get())
            DoneEntry.delete(0, END)

    def Delete(_List):

        if _List == s_List[0]:
            ToDoList.delete(ACTIVE)
        elif _List == s_List[1]:
            InProgressList.delete(ACTIVE)
        elif _List == s_List[2]:
            DoneList.delete(ACTIVE)

    def MoveForward(_List):

        if _List == s_List[1] and ToDoList.get(ACTIVE) != "":
            InProgressList.insert(END, ToDoList.get(ACTIVE))
            ToDoList.delete(ACTIVE)
            InProgressList.focus()
        elif _List == s_List[2] and InProgressList.get(ACTIVE) != "":
            DoneList.insert(END, InProgressList.get(ACTIVE))
            InProgressList.delete(ACTIVE)
            DoneList.focus()
        elif _List == s_List[3] and DoneList.get(ACTIVE) != "":
            DoneList.delete(ACTIVE)

    def MoveBackward(_List):

        if _List == s_List[0] and InProgressList.get(ACTIVE) != "":
            ToDoList.insert(END, InProgressList.get(ACTIVE))
            InProgressList.delete(ACTIVE)
            ToDoList.focus()
        elif _List == s_List[1] and DoneList.get(ACTIVE) != "":
            InProgressList.insert(END, DoneList.get(ACTIVE))
            DoneList.delete(ACTIVE)
            InProgressList.focus()

    def FocusDown(_List):

        if _List == s_List[0] and ToDoList.get(ACTIVE) == ToDoList.get(END):
            ToDoEntry.focus()
            ToDoEntry.delete(0, END)
        elif _List == s_List[1] and InProgressList.get(ACTIVE) == InProgressList.get(END):
            InProgressEntry.focus()
            InProgressEntry.delete(0, END)
        elif _List == s_List[2] and DoneList.get(ACTIVE) == DoneList.get(END):
            DoneEntry.focus()
            DoneEntry.delete(0, END)

    def FocusUp(_List):

        if _List == s_List[0]:
            ToDoList.focus()
            ToDoEntry.delete(0, END)
        elif _List == s_List[1]:
            InProgressList.focus()
            InProgressEntry.delete(0, END)
        elif _List == s_List[2]:
            DoneList.focus()
            DoneEntry.delete(0, END)

    # / ---------------------------------------------------------------------------------------------------

    def _AddToToDo(_Self=0):
        Add(s_List[0])

    def _AddToProgress(_Self=0):
        Add(s_List[1])

    def _AddToDone(_Self=0):
        Add(s_List[2])

    def _DeleteToDo(_Self=0):
        Delete(s_List[0])

    def _DeleteInProgress(_Self=0):
        Delete(s_List[1])

    def _DeleteDone(_Self=0):
        Delete(s_List[2])

    def _MoveToInProgress(_Self=0):
        MoveForward(s_List[1])

    def _MoveToDone(_Self=0):
        MoveForward(s_List[2])

    def _MoveToArchives(_Self=0):
        MoveForward(s_List[3])

    def _BackToToDo(_Self=0):
        MoveBackward(s_List[0])

    def _BackToInProgress(_Self=0):
        MoveBackward(s_List[1])

    def _FocusDownToDo(_Self=0):
        FocusDown(s_List[0])

    def _FocusDownInProgress(_Self=0):
        FocusDown(s_List[1])

    def _FocusDownDone(_Self=0):
        FocusDown(s_List[2])

    def _FocusUpToDo(_Self=0):
        FocusUp(s_List[0])

    def _FocusUpInProgress(_Self=0):
        FocusUp(s_List[1])

    def _FocusUpDone(_Self=0):
        FocusUp(s_List[2])

    def _ExportToCsv(_Self=0):

        File = open("kanban_export.csv", "w")

        for Row in ToDoList.get(0, END):
            File.write(str(Row) + ";to_do\n")

        for Row in InProgressList.get(0, END):
            File.write(str(Row) + ";in_progress\n")

        for Row in DoneList.get(0, END):
            File.write(str(Row) + ";done\n")

        File.close()

    # / ---------------------------------------------------------------------------------------------------

    Window = Tk()
    Window.title("Kanban (tkinter)")
    Window.minsize(width=1200, height=600)

    # / ---------------------------------------------------------------------------------------------------

    # / To Do

    ToDoFrame = Widget.GetLabelFrame(Window, _Text="To Do", _FgColor=Color.s_LightRed, _BgColor=Color.s_DarkBlack)
    ToDoFrame.pack(side=LEFT, fill=BOTH, expand=1)

    ToDoList = Widget.GetList(ToDoFrame, _FgColor=Color.s_LightRed, _BgColor=Color.s_DarkBlack)
    ToDoList.pack(fill=BOTH, expand=1, padx=5, pady=10)
    ToDoList.bind("<BackSpace>", _DeleteToDo)
    ToDoList.bind("<Delete>", _DeleteToDo)
    ToDoList.bind("<Right>", _MoveToInProgress)
    ToDoList.bind("<Down>", _FocusDownToDo)

    ToDoButton = Widget.GetButton(ToDoFrame, _Text="In Progress", _Command=lambda:MoveForward(s_List[1]), _HighlightColor=Color.s_DarkBlack)
    ToDoButton.pack(side=BOTTOM, fill=X)

    ToDoEntry = Widget.GetEntry(ToDoFrame, _HighlightColor=Color.s_DarkBlack)
    ToDoEntry.pack(side=BOTTOM, fill=X)
    ToDoEntry.bind("<Return>", _AddToToDo)
    # ToDoEntry.bind("<Up>", _FocusUpToDo)

    # / In Progress

    InProgressFrame = Widget.GetLabelFrame(Window, _Text="In Progress", _FgColor=Color.s_LightYellow, _BgColor=Color.s_DarkBlack)
    InProgressFrame.pack(side=LEFT, fill=BOTH, expand=1)

    InProgressList = Widget.GetList(InProgressFrame, _FgColor=Color.s_LightYellow, _BgColor=Color.s_DarkBlack)
    InProgressList.pack(fill=BOTH, expand=1, padx=5, pady=10)
    InProgressList.bind("<BackSpace>", _DeleteInProgress)
    InProgressList.bind("<Delete>", _DeleteInProgress)
    InProgressList.bind("<Right>", _MoveToDone)
    InProgressList.bind("<Left>", _BackToToDo)
    InProgressList.bind("<Down>", _FocusDownInProgress)

    InProgressButton = Widget.GetButton(InProgressFrame, _Text="Done", _Command=lambda:MoveForward(s_List[2]), _HighlightColor=Color.s_DarkBlack)
    InProgressButton.pack(side=BOTTOM, fill=X)

    InProgressEntry = Widget.GetEntry(InProgressFrame, _HighlightColor=Color.s_DarkBlack)
    InProgressEntry.pack(side=BOTTOM, fill=X)
    InProgressEntry.bind("<Return>", _AddToProgress)
    # InProgressEntry.bind("<Up>", _FocusUpInProgress)

    # / Done

    DoneFrame = Widget.GetLabelFrame(Window, _Text="Done", _FgColor=Color.s_LightGreen, _BgColor=Color.s_DarkBlack)
    DoneFrame.pack(side=LEFT, fill=BOTH, expand=1)

    DoneList = Widget.GetList(DoneFrame, _FgColor=Color.s_LightGreen, _BgColor=Color.s_DarkBlack)
    DoneList.pack(fill=BOTH, expand=1, padx=5, pady=10)
    DoneList.bind("<BackSpace>", _DeleteDone)
    DoneList.bind("<Delete>", _DeleteDone)
    DoneList.bind("<Right>", _MoveToArchives)
    DoneList.bind("<Left>", _BackToInProgress)
    DoneList.bind("<Down>", _FocusDownDone)

    DoneButton = Widget.GetButton(DoneFrame, _Text="Archive", _Command=lambda:MoveForward(s_List[3]), _HighlightColor=Color.s_DarkBlack)
    DoneButton.pack(side=BOTTOM, fill=X)

    DoneEntry = Widget.GetEntry(DoneFrame, _HighlightColor=Color.s_DarkBlack)
    DoneEntry.pack(side=BOTTOM, fill=X)
    DoneEntry.bind("<Return>", _AddToDone)
    # DoneEntry.bind("<Up>", _FocusUpDone)

    # / ---------------------------------------------------------------------------------------------------

    LoadData()

    Window.bind("<Command-e>", _ExportToCsv)
    Window.mainloop()
