import customtkinter as ctk
from tkinter import filedialog, Canvas
from settings import *

class ImageImporter(ctk.CTkFrame):
    def __init__(self, parent, import_func):
        super().__init__(master = parent)
        self.grid(column = 0, columnspan = 2, row = 0, sticky = 'nsew')
        self.import_func = import_func

        ctk.CTkButton(self, text="Open Image", command = self.open_dialog).pack(expand = True)
    
    def open_dialog(self):
        path = filedialog.askopenfile().name
        self.import_func(path)


class ImageOutput(Canvas):
    def __init__(self, parent, resize_image):
        super().__init__(master = parent, background= BACKGROUND_COLOR, bd=0, highlightthickness= 0, relief = 'ridge')
        self.grid(row = 0, column = 1, sticky = 'nsew')
        self.bind("<Config>", resize_image)
        

class CloseOutput(ctk.CTkButton):
    def __init__(self, parent):
        super().__init__(master = parent, text = 'x')
        self.place(relx = 0.99, rely= 0.01, anchor = 'ne')