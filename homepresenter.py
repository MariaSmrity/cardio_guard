class HomePresenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["home"]
        self._bind()

    def _bind(self):
        self.frame.patientview_btn.config(command=self.switch_patient_view)
        self.frame.populationview_btn.config(command=self.switch_population_view)
        self.frame.log_out_btn.config(command=self.log_out)

    def switch_patient_view(self):
        self.view.switch("singlepatient")

    def switch_population_view(self):
        self.view.switch("population")
    
    def log_out(self):
        self.view.switch("login")
