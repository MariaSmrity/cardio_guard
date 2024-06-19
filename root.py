from tkinter import Tk
from tkinter import ttk

class Root(Tk):
    def __init__(self):
        super().__init__()

        start_width = 600
        min_width = 400
        start_height = 500
        min_height = 450

        self.geometry(f"{start_width}x{start_height}")
        self.minsize(width=min_width, height=min_height)
        self.title("CardioGuard")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        #Style definitions for different components
        style=ttk.Style()
        cg_pink = "#E88684"
        cg_blue = "#388DD8"
        style.configure("design.TButton",background=cg_pink,foreground='white',font="Arial 16", padding=10)
        style.configure("image.TButton",background="white",font="Arial 16", padding=0)
        style.configure("design.TLabel",background="white", foreground="black",font="Arial 16", padding=10)
        style.configure("heading.TLabel", foreground=cg_blue,font="Arial 12", padding=10)
        style.configure("error.TLabel", background="white", foreground="red", font="Arial 12")