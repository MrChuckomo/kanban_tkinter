"""
__File__          = "board.py"
__Description__   = ""
__Author__        = "MrChuckomo"
__Version__       = "v1.0.0"
__Creation_Date__ = "15-Jun-2017"
"""

from Tkinter import *

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



    # / ---------------------------------------------------------------------------------------------------

    def _AddToToDo(_Self=0):
        Add(s_List[0])

    def _AddToProgress(_Self=0):
        Add(s_List[1])

    def _AddToDone(_Self=0):
        Add(s_List[2])

    def _DeleteToDo(_Self=0):
        Delete(s_List[0])

    # / ---------------------------------------------------------------------------------------------------

    Window = Tk()
    Window.title("tkinter Kanban")
    Window.minsize(width=1200, height=600)

    # / ---------------------------------------------------------------------------------------------------

    # / To Do 

    ToDoFrame = LabelFrame(Window, text="To Do")
    ToDoFrame.pack(side=LEFT, fill=BOTH, expand=1)

    ToDoList = Listbox(ToDoFrame)
    ToDoList.pack(fill=BOTH, expand=1)
    ToDoList.bind("<BackSpace>", _DeleteToDo)
    ToDoList.bind("<Delete>", _DeleteToDo)

    ToDoButton = Button(ToDoFrame, text="In Progress", command=lambda:MoveForward(s_List[1]))
    ToDoButton.pack(side=BOTTOM, fill=X)
    
    ToDoEntry = Entry(ToDoFrame)
    ToDoEntry.pack(side=BOTTOM, fill=X)
    ToDoEntry.bind("<Return>", _AddToToDo)

    # / In Progress

    InProgressFrame = LabelFrame(Window, text="In Progress")
    InProgressFrame.pack(side=LEFT, fill=BOTH, expand=1)

    InProgressList = Listbox(InProgressFrame)
    InProgressList.pack(fill=BOTH, expand=1)

    InProgressButton = Button(InProgressFrame, text="Done", command=lambda:MoveForward(s_List[2]))
    InProgressButton.pack(side=BOTTOM, fill=X)

    InProgressEntry = Entry(InProgressFrame)
    InProgressEntry.pack(side=BOTTOM, fill=X)
    InProgressEntry.bind("<Return>", _AddToProgress)

    # / Done

    DoneFrame = LabelFrame(Window, text="Done")
    DoneFrame.pack(side=LEFT, fill=BOTH, expand=1)

    DoneList = Listbox(DoneFrame)
    DoneList.pack(fill=BOTH, expand=1)

    DoneButton = Button(DoneFrame, text="Archives", command=lambda:MoveForward(s_List[3]))
    DoneButton.pack(side=BOTTOM, fill=X)

    DoneEntry = Entry(DoneFrame)
    DoneEntry.pack(side=BOTTOM, fill=X)
    DoneEntry.bind("<Return>", _AddToDone)

    # / ---------------------------------------------------------------------------------------------------

    Window.mainloop()
