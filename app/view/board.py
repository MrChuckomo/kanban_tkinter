"""
__File__          = "board.py"
__Description__   = ""
__Author__        = "MrChuckomo"
__Version__       = "v1.0.0"
__Creation_Date__ = "15-Jun-2017"
"""
# / --------------------------------------------------------------------------------------------------------------------

from tkinter import Tk, OptionMenu, StringVar, END, ACTIVE, BOTH, BOTTOM, LEFT, RIGHT, X, TOP
from view import components as TkComponents
from view import color as Color
from model import kanban_db as Db

import sys
sys.path.append("../")


# / --------------------------------------------------------------------------------------------------------------------

s_List = ["todo", "in_progress", "done", "archives"]


def drawWindow():

    def LoadData():

        ToDoList.delete(0, END)
        InProgressList.delete(0, END)
        DoneList.delete(0, END)

        for Row in Db.SelectData("todo"):
            ToDoList.insert(END, Row[1])
        for Row in Db.SelectData("inprogress"):
            InProgressList.insert(END, Row[1])
        for Row in Db.SelectData("done"):
            DoneList.insert(END, Row[1])

    def Add(_List):

        if _List == s_List[0] and ToDoEntry.get() != "":
            Db.InsertData(_Table="todo", _Task=ToDoEntry.get())
            ToDoEntry.delete(0, END)
        elif _List == s_List[1] and InProgressEntry.get() != "":
            Db.InsertData(_Table="inprogress", _Task=InProgressEntry.get())
            InProgressEntry.delete(0, END)
        elif _List == s_List[2] and DoneEntry.get() != "":
            Db.InsertData(_Table="done", _Task=DoneEntry.get())
            DoneEntry.delete(0, END)

        LoadData()

    def Delete(_List):

        if _List == s_List[0]:
            Db.DeleteDataByTask(_Table="todo", _Task=ToDoList.get(ACTIVE))
        elif _List == s_List[1]:
            Db.DeleteDataByTask(_Table="inprogress", _Task=InProgressList.get(ACTIVE))
        elif _List == s_List[2]:
            Db.DeleteDataByTask(_Table="done", _Task=DoneList.get(ACTIVE))

        LoadData()

    def MoveForward(_List):

        if _List == s_List[1] and ToDoList.get(ACTIVE) != "":
            Db.InsertData(_Table="inprogress", _Task=ToDoList.get(ACTIVE))
            Db.DeleteDataByTask(_Table="todo", _Task=ToDoList.get(ACTIVE))
            InProgressList.focus()
        elif _List == s_List[2] and InProgressList.get(ACTIVE) != "":
            Db.InsertData(_Table="done", _Task=InProgressList.get(ACTIVE))
            Db.DeleteDataByTask(_Table="inprogress", _Task=InProgressList.get(ACTIVE))
            DoneList.focus()
        elif _List == s_List[3] and DoneList.get(ACTIVE) != "":
            Db.InsertData(_Table="archives", _Task=DoneList.get(ACTIVE))
            Db.DeleteDataByTask(_Table="done", _Task=DoneList.get(ACTIVE))

        LoadData()

    def MoveBackward(_List):

        if _List == s_List[0] and InProgressList.get(ACTIVE) != "":
            Db.InsertData(_Table="todo", _Task=InProgressList.get(ACTIVE))
            Db.DeleteDataByTask(_Table="inprogress", _Task=InProgressList.get(ACTIVE))
            ToDoList.focus()
        elif _List == s_List[1] and DoneList.get(ACTIVE) != "":
            Db.InsertData(_Table="inprogress", _Task=DoneList.get(ACTIVE))
            Db.DeleteDataByTask(_Table="done", _Task=DoneList.get(ACTIVE))
            InProgressList.focus()
        LoadData()

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

    # / ----------------------------------------------------------------------------------------------------------------

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

    def _FocusList(_List):
        if _List == s_List[0]:
            ToDoList.focus()
        elif _List == s_List[1]:
            InProgressList.focus()
        elif _List == s_List[2]:
            DoneList.focus()

    def _FocusTodo(_Self=0):
        _FocusList(s_List[0])

    def _FocusInProgress(_Self=0):
        _FocusList(s_List[1])

    def _FocusDone(_Self=0):
        _FocusList(s_List[2])

    def _FocusEntry(_Self=0):
        ToDoEntry.focus()

    def _ExportToCsv(_Self=0):

        File = open("kanban_export.csv", "w")

        for Row in ToDoList.get(0, END):
            File.write(str(Row) + ";to_do\n")

        for Row in InProgressList.get(0, END):
            File.write(str(Row) + ";in_progress\n")

        for Row in DoneList.get(0, END):
            File.write(str(Row) + ";done\n")

        File.close()

    # / ----------------------------------------------------------------------------------------------------------------

    Widget = TkComponents.CTkComponents("LIGHT")

    # / ----------------------------------------------------------------------------------------------------------------

    Window = Tk()
    Window.title("Kanban (tkinter)")
    Window.minsize(width=1200, height=600)

    # / ----------------------------------------------------------------------------------------------------------------

    # / Projects

    ProjectFrame = Widget.GetFrame(Window)
    ProjectFrame.pack(side=TOP, fill=X)

    Option = StringVar()
    Option.set("General Tasks")
    ProjectMenu = OptionMenu(ProjectFrame, Option, "General Tasks", "Others")
    ProjectMenu.configure(bg=Color.s_LightGrey)
    ProjectMenu.pack(side=LEFT)

    CreateProjectButton = Widget.GetButton(ProjectFrame, "Create Project")
    CreateProjectButton.pack(side=RIGHT, padx=10)

    DeleteProjectButton = Widget.GetButton(ProjectFrame, "Delete Project")
    DeleteProjectButton.pack(side=RIGHT)

    # / To Do

    ToDoFrame = Widget.GetLabelFrame(Window, _Text="To Do")
    ToDoFrame.pack(side=LEFT, fill=BOTH, expand=1)

    ToDoList = Widget.GetList(ToDoFrame)
    ToDoList.pack(fill=BOTH, expand=1, padx=5, pady=10)
    ToDoList.bind("<BackSpace>", _DeleteToDo)
    ToDoList.bind("<Delete>", _DeleteToDo)
    ToDoList.bind("<Command-Right>", _MoveToInProgress)
    ToDoList.bind("<Right>", _FocusInProgress)
    # ToDoList.bind("<Down>", _FocusDownToDo)

    ToDoButton = Widget.GetButton(ToDoFrame, _Text="In Progress", _Command=lambda: MoveForward(s_List[1]))
    ToDoButton.pack(side=BOTTOM, fill=X)

    ToDoEntry = Widget.GetEntry(ToDoFrame)
    ToDoEntry.pack(side=BOTTOM, fill=X)
    ToDoEntry.bind("<Return>", _AddToToDo)
    # ToDoEntry.bind("<Up>", _FocusUpToDo)

    # / In Progress

    InProgressFrame = Widget.GetLabelFrame(Window, _Text="In Progress")
    InProgressFrame.pack(side=LEFT, fill=BOTH, expand=1)

    InProgressList = Widget.GetList(InProgressFrame)
    InProgressList.pack(fill=BOTH, expand=1, padx=5, pady=10)
    InProgressList.bind("<BackSpace>", _DeleteInProgress)
    InProgressList.bind("<Delete>", _DeleteInProgress)
    InProgressList.bind("<Command-Right>", _MoveToDone)
    InProgressList.bind("<Command-Left>", _BackToToDo)
    InProgressList.bind("<Right>", _FocusDone)
    InProgressList.bind("<Left>", _FocusTodo)
    # InProgressList.bind("<Down>", _FocusDownInProgress)

    InProgressButton = Widget.GetButton(InProgressFrame, _Text="Done", _Command=lambda: MoveForward(s_List[2]))
    InProgressButton.pack(side=BOTTOM, fill=X)

    InProgressEntry = Widget.GetEntry(InProgressFrame)
    InProgressEntry.pack(side=BOTTOM, fill=X)
    InProgressEntry.bind("<Return>", _AddToProgress)
    # InProgressEntry.bind("<Up>", _FocusUpInProgress)

    # / Done

    DoneFrame = Widget.GetLabelFrame(Window, _Text="Done")
    DoneFrame.pack(side=LEFT, fill=BOTH, expand=1)

    DoneList = Widget.GetList(DoneFrame)
    DoneList.pack(fill=BOTH, expand=1, padx=5, pady=10)
    DoneList.bind("<BackSpace>", _DeleteDone)
    DoneList.bind("<Delete>", _DeleteDone)
    DoneList.bind("<Command-Right>", _MoveToArchives)
    DoneList.bind("<Command-Left>", _BackToInProgress)
    DoneList.bind("<Left>", _FocusInProgress)
    # DoneList.bind("<Down>", _FocusDownDone)

    DoneButton = Widget.GetButton(DoneFrame, _Text="Archive", _Command=lambda: MoveForward(s_List[3]))
    DoneButton.pack(side=BOTTOM, fill=X)

    DoneEntry = Widget.GetEntry(DoneFrame)
    DoneEntry.pack(side=BOTTOM, fill=X)
    DoneEntry.bind("<Return>", _AddToDone)
    # DoneEntry.bind("<Up>", _FocusUpDone)

    # / ----------------------------------------------------------------------------------------------------------------

    LoadData()

    Window.bind("<Command-e>", _ExportToCsv)
    Window.bind("<Command-i>", _FocusEntry)
    Window.mainloop()
