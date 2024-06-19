import requests

class FhirAdapter():
    # Constructor, initializes the object with given parameters
    # parameters:
        # self
        # url: FHIR server url
        # username: username to the FHIR server
        # password: password to the FHIR server
    # return: none
    def __init__(self, url, username, password):
        self.address = url
        self.username = username
        self.password = password

    # Function makes a request to the FHIR server to get all patients
    # parameters:
        # self: server url
    # return: list of all Patient resources
    def get_patients(self):
        print('Connecting to FHIR server')
        request_url = self.address + '/Patient?_format=json'
        response = self._make_server_request(request_url)
        entries = response["entry"]
        print(str(len(entries)) + ' Patient resources found')
        patients = {}
        patient_index = 0
        print('Retrieving data for each patient')
        bar = ['-'] * len(entries)
        for item in entries:
            bar[patient_index] = '#'
            print(''.join(bar), end="\r")
            patient_index += 1
            resource = item["resource"]
            id = resource["id"]
            firstName = ""
            for i in range(len(resource["name"][0]["given"])):
                name = resource["name"][0]["given"][i]
                if i == 0:
                    firstName += name
                else:
                    firstName = firstName + ' ' + name
            lastName = ""
            for i in range(len(resource["name"][0]["family"])):
                name = resource["name"][0]["family"][i]
                if i == 0:
                    lastName += name
                else:
                    lastName = lastName + ' ' + name
            name = firstName + ' ' + lastName
            gender = resource["gender"]
            birth_date = resource["birthDate"]
            lab_values = self._getAllDataPatient(id)
            patients[id] = {
                "name": name,
                "dob": birth_date,
                "gender": gender,
                "lab values": lab_values  
            }
        
        return patients
    
    def _getAllDataPatient(self, patient_id):
        request_url = self.address + '/Patient/' + patient_id + '$everything?_format=json'
        response = self._make_server_request(request_url)
        entries = response["entry"]
        lab_values = {}
        for item in entries:
            resource = item["resource"]
            if resource["resourceType"] == "Observation":
                if resource["code"]["text"] == "bmi":
                    value = resource["valueQuantity"]["value"]
                    date = resource["effectiveDateTime"]
                    if date in lab_values.keys():
                        lab_values[date]["bmi"] = value
                    else:
                        lab_values[date] = {}
                        lab_values[date]["bmi"] = value
                if resource["code"]["text"] == "Diastolic blood pressure":
                    value = resource["valueQuantity"]["value"]
                    date = resource["effectiveDateTime"]
                    if date in lab_values.keys():
                        lab_values[date]["bp_dia"] = value
                    else:
                        lab_values[date] = {}
                        lab_values[date]["bp_dia"] = value
                if resource["code"]["text"] == "Systolic blood pressure":
                    value = resource["valueQuantity"]["value"]
                    date = resource["effectiveDateTime"]
                    if date in lab_values.keys():
                        lab_values[date]["bp_sys"] = value
                    else:
                        lab_values[date] = {}
                        lab_values[date]["bp_sys"] = value

        return lab_values
        

    # Function makes a request to the given url and checks for errors
    # parameters:
        # self: username and password for authentication
        # url: where to make the request
    # return: response in JSON format
    def _make_server_request(self, url):
        response = requests.get(url, auth=(self.username, self.password))

        # if error has occured
        response.raise_for_status()
        
        return response.json()

    


