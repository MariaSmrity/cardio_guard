class Patient:
  
  # Constructor for the patient class
  # Params: a dictionary of patient information
  def __init__(self, ssn, name, dob):
    self.__ssn = ssn
    self.__name = name
    self.__dob = dob
    self.__lab_values = {}
  
  # Return the ssn of the patient
  def get_ssn(self):
    return self.__ssn
  
  # Return the name of the patient
  def get_name(self):
    return self.__name
  
  # Return the pateint's date of birth
  def get_dob(self):
    return self.__dob
  
  # Upadate the lab values of the patient
  def set_lab_values(self, lab_values):
    self.__lab_values.update(lab_values)

  # Return the laboratory values of the patient
  def get_lab_values(self): 
    return self.__lab_values

