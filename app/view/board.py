"""
__File__          = "board.py"
__Description__   = ""
__Author__        = "MrChuckomo"
__Version__       = "v1.0.0"
__Creation_Date__ = "15-Jun-2017"
"""

from Tkinter import *
from view import components as Widget
from view import color as Color

s_List = ["todo", "in_progress", "done", "archives"]

def drawWindow():

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
        elif _List == s_List[2] and InProgressList.get(ACTIVE) != "":
            DoneList.insert(END, InProgressList.get(ACTIVE))
            InProgressList.delete(ACTIVE)
        elif _List == s_List[3] and DoneList.get(ACTIVE) != "":
            DoneList.delete(ACTIVE)

    def MoveBackward(_List):

        if _List == s_List[0] and InProgressList.get(ACTIVE) != "":
            ToDoList.insert(END, InProgressList.get(ACTIVE))
            InProgressList.delete(ACTIVE)
        elif _List == s_List[1] and DoneList.get(ACTIVE) != "":
            InProgressList.insert(END, DoneList.get(ACTIVE))
            DoneList.delete(ACTIVE)

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

    # / ---------------------------------------------------------------------------------------------------

    Window = Tk()
    Window.title("tkinter Kanban")
    Window.minsize(width=1200, height=600)
    
    # / ---------------------------------------------------------------------------------------------------

    # / To Do 

    ToDoFrame = Widget.GetLabelFrame(Window, _Text="To Do", _FgColor=Color.s_LightRed)
    ToDoFrame.pack(side=LEFT, fill=BOTH, expand=1)

    ToDoList = Widget.GetList(ToDoFrame, _FgColor=Color.s_LightRed)
    ToDoList.pack(fill=BOTH, expand=1)
    ToDoList.bind("<BackSpace>", _DeleteToDo)
    ToDoList.bind("<Delete>", _DeleteToDo)
    ToDoList.bind("<Right>", _MoveToInProgress)

    ToDoButton = Widget.GetButton(ToDoFrame, _Text="In Progress", _Command=lambda:MoveForward(s_List[1]))
    ToDoButton.pack(side=BOTTOM, fill=X)
    
    ToDoEntry = Widget.GetEntry(ToDoFrame)
    ToDoEntry.pack(side=BOTTOM, fill=X)
    ToDoEntry.bind("<Return>", _AddToToDo)

    # / In Progress

    InProgressFrame = Widget.GetLabelFrame(Window, _Text="In Progress", _FgColor=Color.s_LightYellow)
    InProgressFrame.pack(side=LEFT, fill=BOTH, expand=1)

    InProgressList = Widget.GetList(InProgressFrame, _FgColor=Color.s_LightYellow)
    InProgressList.pack(fill=BOTH, expand=1)
    InProgressList.bind("<BackSpace>", _DeleteInProgress)
    InProgressList.bind("<Delete>", _DeleteInProgress)
    InProgressList.bind("<Right>", _MoveToDone)
    InProgressList.bind("<Left>", _BackToToDo)

    InProgressButton = Widget.GetButton(InProgressFrame, _Text="Done", _Command=lambda:MoveForward(s_List[2]))
    InProgressButton.pack(side=BOTTOM, fill=X)

    InProgressEntry = Widget.GetEntry(InProgressFrame)
    InProgressEntry.pack(side=BOTTOM, fill=X)
    InProgressEntry.bind("<Return>", _AddToProgress)

    # / Done

    DoneFrame = Widget.GetLabelFrame(Window, _Text="Done", _FgColor=Color.s_LightGreen)
    DoneFrame.pack(side=LEFT, fill=BOTH, expand=1)

    DoneList = Widget.GetList(DoneFrame, _FgColor=Color.s_LightGreen)
    DoneList.pack(fill=BOTH, expand=1)
    DoneList.bind("<BackSpace>", _DeleteDone)
    DoneList.bind("<Delete>", _DeleteDone)
    DoneList.bind("<Right>", _MoveToArchives)
    DoneList.bind("<Left>", _BackToInProgress)

    DoneButton = Widget.GetButton(DoneFrame, _Text="Archives", _Command=lambda:MoveForward(s_List[3]))
    DoneButton.pack(side=BOTTOM, fill=X)

    DoneEntry = Widget.GetEntry(DoneFrame)
    DoneEntry.pack(side=BOTTOM, fill=X)
    DoneEntry.bind("<Return>", _AddToDone)

    # / ---------------------------------------------------------------------------------------------------

    Window.mainloop()
