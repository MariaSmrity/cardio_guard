class Loginpresenter:
    def __init__(self, model, view, loginmodel):
        self.loginmodel = loginmodel
        self.model = model
        self.view = view
        self.frame = self.view.frames["login"]
        self._bind()
        #self.register_new_user("testi", "Testi1234578!?")
        #self.login("testi", "Testi1234578!?")
        #print(self.model.current_user)
  
    def login(self):
        username = self.frame.username_input.get()
        password = self.frame.password_input.get()
        success = self.loginmodel.login("testi", "Testi1234578!?")
        if success:
            self.model.current_user = username
            self.frame.username_input.delete('0', 'end')
            self.frame.username_input.insert('0', '')
            self.frame.password_input.delete('0', 'end')
            self.frame.password_input.delete('0', '')
            self.view.switch("home")
            self.frame.login_success.config(text="")
        else:
            self.frame.login_success.config(text="Incorrect username or password!")
            self.frame.login_success.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
            #print("Incorrect username or pasword!")
    
    # Just to make the test user
    def register_new_user(self, username, password):
        self.loginmodel.signup(username, password)

    def _bind(self):
        self.frame.login_btn.config(command=self.login)