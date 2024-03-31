
from tkinter import BOTH, END, Button, Entry, Frame, filedialog, Label, \
                    StringVar, Text, Tk, X, Y
from functions import get_suggestions


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



        # ---------------------------------------------------------------------
        # Path 

        self.path_panel = Frame(self.main_window, STANDARD_FRAME_ATTRIBUTES)
        self.path_panel.pack()

        self.path_label = Label(self.path_panel, text="Documents Folder Path:")
        self.path_label.pack()

        self.directory_path = StringVar()
        self.path_entry = Entry(self.path_panel, width=100, 
                                textvariable=self.directory_path)
        self.path_entry.pack(expand=1)

        self.path_open_dialog_button = Button(self.path_panel, 
            text="Browse",
            command=self.open_path_select_dialog)
        self.path_open_dialog_button.pack()


        # ---------------------------------------------------------------------
        # Get autosuggest results

        self.autosuggest_panel = Frame(self.main_window, STANDARD_FRAME_ATTRIBUTES)
        self.autosuggest_panel.pack()

        self.enter_text_label = Label(self.autosuggest_panel, text="Enter text:")
        self.enter_text_label.pack()

        self.user_input_text = StringVar()
        self.text_entry = Entry(self.autosuggest_panel, width=40,
                                textvariable=self.user_input_text)
        self.text_entry.bind("<Key>", self.on_character_entered)
        self.text_entry.pack()

        self.results_text = Text(self.autosuggest_panel,
                                 width=50, height=20)
        self.results_text.pack()


    def open_path_select_dialog(self):
        self.directory_path = filedialog.askdirectory()
        self.path_entry.delete(0, END)
        self.path_entry.insert(0, self.directory_path)


    def on_character_entered(self, evt):
        text = self.user_input_text.get() + evt.char

        suggestions_list = get_suggestions(text, self.directory_path, ["h", "cpp", "py"], 3)

        print(suggestions_list)

        suggestions = '\n'.join(suggestions_list)

        print(suggestions)

        self.results_text.delete(1.0, END)
        self.results_text.insert(END, suggestions)



