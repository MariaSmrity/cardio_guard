import risk

class SinglePatientPresenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["singlepatient"]
        self._bind()

    def _bind(self):
        self.frame.exit_button.config(command=self.exit)
        self.frame.search_button.config(command=self.search_patient)

    def exit(self):
        self.reset_view()
        self.frame.info_label.config(text = "")
        self.view.switch("home")
    
    def search_patient(self):
        id = self.frame.patient_entry.get()
        if id in self.model.patient_dict.keys():
            patient = self.model.patient_dict[id]
            name = patient.get_name()
            dob = patient.get_dob()
            lab_values = patient.get_lab_values()
            defaults = {"bmi": 0, "bp_sys": 0, "bp_dia": 0}
            if len(lab_values) != 0:
                last_key = list(lab_values)[-1]
                bmi = lab_values[last_key].get("bmi", defaults["bmi"])
                sys = lab_values[last_key].get("bp_sys", defaults["bp_sys"])
                dia = lab_values[last_key].get("bp_dia", defaults["bp_dia"])
                self.populate_view(name, dob, bmi, sys, dia)
            else:
                self.populate_view(name, dob, 0, 0, 0)
        else:
            self.reset_view()
            self.frame.info_label.config(text = "Invalid id. Try again.")

    def reset_view(self):
        self.frame.name_label.config(text = "")
        self.frame.dob_label.config(text = "")
        self.frame.bmi_label.config(text = "")
        self.frame.bp_label.config(text = "")
        self.frame.risk_label.config(text = "")
        self.frame.patient_identifier.set("")
    
    def populate_view(self, name, dob, bmi, sys, dia):
        self.frame.info_label.config(text = "")
        self.frame.name_label.config(text = name)
        self.frame.dob_label.config(text = "Date of birth: " + dob)
        if bmi != 0:
            self.frame.bmi_label.config(text = "BMI: " + str(bmi))
        if sys != 0 and dia != 0:
            self.frame.bp_label.config(text = "Blood pressure (sys/dia): " + str(sys) + "/" + str(dia) + " mmHg")
        if bmi != 0 and sys != 0 and dia != 0:
            total_risk = risk.calculate_risk(bmi, sys, dia)
            self.frame.risk_label.config(text = "Patient total risk level: " + str(total_risk))
        self.frame.patient_identifier.set("")