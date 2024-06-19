from tkinter import *
from tkinter import ttk
from paths import PROJECT_ROOT

class LoginView(Frame):
  LOGO_PATH = PROJECT_ROOT / 'icons' / 'logo.png'

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.grid_columnconfigure(0, weight=0)
    self.grid_columnconfigure(1, weight=1)
    self.configure(bg="white")

    self.logo_image = PhotoImage(file=self.LOGO_PATH).subsample(2,2)

    self.logo_label = Label(self, image=self.logo_image)
    self.logo_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    self.header = Label(self, text="Log in with existing account", font=("Arial", 15), bg="white")
    self.header.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    self.login_success = ttk.Label(self, text="", style="design.error.TLabel")
    #self.login_success.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    self.username_label = Label(self, text="Username", font=("Arial", 12), bg="white")
    self.username_input = ttk.Entry(self, width=20)
    self.username_label.grid(row=3, column=0, columnspan=2, padx=20, pady=(5,5))
    self.username_input.grid(row=4, column=0, columnspan=2, padx=(20, 20), pady=(5,5))

    self.password_label = Label(self, text="Password", font=("Arial", 12), bg="white")
    self.password_input = ttk.Entry(self, show="*", width=20)
    self.password_label.grid(row=5, column=0, columnspan=2, padx=10, pady=(5,5))
    self.password_input.grid(row=6, column=0, columnspan=2, padx=(20, 20), pady=(5,10))

    self.login_btn = ttk.Button(self, text="Log In", style="design.TButton")
    self.login_btn.grid(row=7, column=0, columnspan=2, padx=20, pady=10)

    


    
