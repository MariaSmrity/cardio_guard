from tkinter import *
from tkinter import ttk

class PopulationView(Frame):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.grid_columnconfigure(0, weight=1)

    heading_label=ttk.Label(self,text = f"Population view", style="heading.TLabel")
    heading_label.grid(row=0, column=0, padx=5,pady=5)

    info_label=ttk.Label(self,text = f"Choose the view:", style="design.TLabel")
    info_label.grid(row=1, column=0, padx=5,pady=5)

    
    self.bmi_option = ttk.Button(self, text='BMI', style = "design.TButton")
    self.bmi_option.grid(row=2,column=0,padx=5,pady=5)
    self.bp_option = ttk.Button(self, text='Blood pressure', style = "design.TButton")
    self.bp_option.grid(row=3,column=0,padx=5,pady=5)
    self.risk_option = ttk.Button(self, text='Risk', style = "design.TButton")
    self.risk_option.grid(row=4,column=0,padx=5,pady=5)

    self.back_button=ttk.Button(self,text = "Back", style = "design.TButton")
    self.back_button.grid(row=5,column=1,padx=5,pady=5)
