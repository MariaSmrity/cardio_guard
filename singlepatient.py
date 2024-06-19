from tkinter import *
from tkinter import ttk
from paths import PROJECT_ROOT

class SinglePatientView(Frame):
  ICON_PATH = PROJECT_ROOT / 'icons' / 'search.png'
  LOGO_PATH = PROJECT_ROOT / 'icons' / 'logo.png'

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    
    self.configure(bg="white")

    #self.grid_rowconfigure(0, weight=1)
    self.grid_rowconfigure(9, weight=1)
    self.grid_columnconfigure(0, weight=1)
    self.grid_columnconfigure(3, weight=1)

    self.logo_image = PhotoImage(file=self.LOGO_PATH).subsample(4,4)

    self.logo_label = Label(self, image=self.logo_image)
    self.logo_label.grid(row=0, column=3, padx=10, pady=10)

    search_label=ttk.Label(self,text = f"Search patient by id: ", style="design.TLabel")
    search_label.grid(row=1, column=1, columnspan=2, padx=5,pady=5)

    self.patient_identifier = StringVar()
    self.patient_entry = ttk.Entry(self, textvariable=self.patient_identifier, font="Arial 16")
    self.patient_entry.grid(row=2, column=1, padx=5,pady=5)

    self.search_icon = PhotoImage(file = self.ICON_PATH).subsample(17, 17)
      
    self.search_button = ttk.Button(self, text = "Search", image=self.search_icon, 
                                    style = 'design.TButton', compound=RIGHT)
    self.search_button.grid(row=2, column=2, padx=5,pady=5, sticky="w")

    self.info_label = ttk.Label(self, text=f"", style="error.TLabel", anchor="w")
    self.info_label.grid(row=3, column=1)
    self.name_label = ttk.Label(self, text=f"", style="design.TLabel", anchor="w")
    self.name_label.grid(row=4, column=1)
    self.dob_label = ttk.Label(self, text=f"", style="design.TLabel", anchor="w")
    self.dob_label.grid(row=5, column=1)
    self.bmi_label = ttk.Label(self, text=f"", style="design.TLabel", anchor="w")
    self.bmi_label.grid(row=6, column=1)
    self.bp_label = ttk.Label(self, text=f"", style="design.TLabel", anchor="w")
    self.bp_label.grid(row=7, column=1)
    self.risk_label = ttk.Label(self, text=f"", style="design.TLabel", anchor="w")
    self.risk_label.grid(row=8, column=1)

    self.exit_button=ttk.Button(self,text = "Exit", style = "design.TButton")
    self.exit_button.grid(row=0,column=0,padx=5,pady=5)
    
