
from tkinter import BOTH, Button, Entry, Frame, Label, Tk, X, Y


COLOR_LIGHT_GRAY = "#DDDDDD"

STANDARD_FRAME_ATTRIBUTES = {
    "borderwidth":5,
    "relief":"ridge",
    "bg":COLOR_LIGHT_GRAY
}


class MainWindow(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master 

        # ---------------------------------------------------------------------
        # Main Window - Contains top control panel, filters panel, and doc list
        
        self.main_window = Frame(self.master,
            STANDARD_FRAME_ATTRIBUTES,
            # width=400, height=400
            )
        self.main_window.pack(fill=BOTH, expand=1, side="left")


        # Path 
        self.path_panel = Frame(self.main_window, STANDARD_FRAME_ATTRIBUTES)

        self.path_label = Label(self.path_panel, text="Documents Folder Path:")
        self.path_label.

