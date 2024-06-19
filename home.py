from tkinter import *
from tkinter import ttk
from paths import PROJECT_ROOT

class HomeView(Frame):
    LOGO_PATH = PROJECT_ROOT / 'icons' / 'logo.png'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.configure(bg="white")

        self.logo_image = PhotoImage(file=self.LOGO_PATH).subsample(3,3)
        self.one_patient_image = PhotoImage(file = PROJECT_ROOT / 'icons' / 'one_patient.png').subsample(1,1)
        self.population_image = PhotoImage(file = PROJECT_ROOT / 'icons' / 'population.png').subsample(1,1)

        self.logo_label = Label(self, image=self.logo_image)
        self.logo_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="n")

        self.excess_label = Label(self, text= "", background="White")
        self.excess_label.grid(row=0, column=2,sticky='n')

        #self.header = ttk.Label(self, text="Home page", style="heading.TLabel")
        #self.header.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.greeting = ttk.Label(self, text="Welcome to use Cardio Guard!", style="design.TLabel")
        self.greeting.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="n")

        self.info = ttk.Label(self, text="Choose an action", style="design.TLabel")
        self.info.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="n")

        self.patientview_btn = ttk.Button(self, image=self.one_patient_image, style="image.TButton")
        self.patientview_btn.grid(row=3, column=0, rowspan=2, padx=0, pady=0, sticky="n")

        self.populationview_btn = ttk.Button(self, image=self.population_image, style="image.TButton")
        self.populationview_btn.grid(row=3, column=1, columnspan=2, rowspan=2, padx=(0,20), pady=0, sticky="n")

        self.log_out_btn = ttk.Button(self, text="Log out", style="image.TButton")
        self.log_out_btn.grid(row=0,column=2, pady=10, sticky="n")