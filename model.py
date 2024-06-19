from fhir_adapter import FhirAdapter
from patient import Patient
import risk

class Model:
    def __init__(self):
        self.adapter = FhirAdapter("http://18.195.221.24", "tutfhir", "tutfhir1")
        self.patients = self.adapter.get_patients()
        # A mock patient list until adapter's API is ready 
        """
        self.patients = {
            "1234": {"name": "Test Patient", 
                   "dob": "01.01.2000",
                   "lab values": {"3.3.2024" : {"bmi": 20, "bp_sys": 120, "bp_dia": 80},
                                  "6.2.2021" : {"bmi": 25, "bp_sys": 130}}
                },
            "1235": {"name": "Test Person", 
                   "dob": "01.01.2001",
                   "lab values": {"1.1.2024" : {"bmi": 25, "bp_sys": 130, "bp_dia": 90},
                                  "2.5.2024" : {"bmi": 30, "bp_sys": 140, "bp_dia": 100}}
            }
        }"""
        self.current_user = "Essi"
        self.patient_dict = {}
        self.populate_patients() # Here will be all the patients. Key: ssn, Value: Patient object

    # Calculate the risk values for each patient and add to the lab values
    def add_risk(self, data):
        defaults = {"bmi": 20, "bp_sys": 120, "bp_dia": 80}

        # Calculate risk values for each test date
        for date in data:
            # Get the lab values but assign a default value if they don't exist
            bmi = data[date].get("bmi", defaults["bmi"])
            bp_sys = data[date].get("bp_sys", defaults["bp_sys"])
            bp_dia = data[date].get("bp_dia", defaults["bp_dia"])
            
            # Calculate and add the risk value
            calculated_risk = risk.calculate_risk(bmi, bp_sys, bp_dia)
            data[date]["risk"] = calculated_risk
      
        return data
    
    # Populate the patient dictionary with patient objects
    def populate_patients(self):
        for ssn, data in self.patients.items():
            self.patient_dict[ssn] = Patient(ssn, data["name"], data["dob"])    
            self.patient_dict[ssn].set_lab_values(self.add_risk(data["lab values"]))
          
