from model import Model
from homepresenter import HomePresenter
from singlepatientpresenter import SinglePatientPresenter
from populationpresenter import PopulationPresenter
from loginpresenter import Loginpresenter
from loginmodel import Loginmodel

class Presenter:
    def __init__(self, view):
        self.view = view
        self.model = Model()
        self.loginmodel = Loginmodel()
        self.home_presenter = HomePresenter(self.model, view)
        self.single_patient_presenter = SinglePatientPresenter(self.model, view)
        self.population_presenter = PopulationPresenter(self.model, view)
        self.login_presenter =  Loginpresenter(self.model, view, self.loginmodel)
        self.view.switch("login") #Here we can do if statement for if the user is logged in
        self.view.start_mainloop()