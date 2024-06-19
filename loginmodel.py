import argon2
import json
from paths import PROJECT_ROOT

class Loginmodel:
    USRCHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    SPECIALS = "!@#$%^&*()_+-=[]}{;':\",./<>?\\|`~"
    ACCINFO_PATH = PROJECT_ROOT / 'accinfo.json'

    def __init__(self):
        self.hasher = argon2.PasswordHasher()

    def hash_password(self, password):
        hashed_password = self.hasher.hash(password)
        return hashed_password


    # Check if input password matches stored password
    def check_password(self, input_password, hashed_password):
        try:
            self.hasher.verify(hashed_password, input_password)
            return True
        except argon2.exceptions.VerifyMismatchError:
            return False


    # Store new credentials
    def store_credentials(self, username, password):
      try:
        with open(self.ACCINFO_PATH, "r") as file:
          data = json.load(file)
      except FileNotFoundError:
        print("Internal error.")
        return

      # Add or update the new credentials
      data[username] = password

      # Write the updated data back to the JSON file
      with open(self.ACCINFO_PATH, "w") as file:
        json.dump(data, file)
        

    def signup(self, username, password):
      # Create username
      usr = username.lower() 
      if any(c not in self.USRCHARS for c in usr):
        print("Invalid username.")
      elif self.check_user(usr, True) == "exists":
        print("Username already exists.")
      
      # Create password      
      pwd = password
      if len(pwd) < 8:
        print("Password must be at least 8 characters long.")
      elif len(pwd) > 64:
        print("Password must be no more than 64 characters long.")
      elif not any(c in self.SPECIALS for c in pwd):
        print("Password must contain at least one special character.")
      

      # Hash the password and store new user
      self.store_credentials(usr, self.hash_password(pwd))


    # Check if user exists. Return password if so, else return empty string
    def check_user(self, username, new_user=False):
      f = open(self.ACCINFO_PATH, 'r')
      data = json.load(f)
      hash = ""
      try:
        for user in data.keys():
          if user == username:
            if not new_user:
              hash = data[user]
            else:
              hash ="exists"
        f.close()      
        return hash
      except Exception as e:
        print(e)
        f.close()
        return ""


    # Attempt to login
    def login(self, username, input_password):

      # Check if user exists
      hash = self.check_user(username)
      if hash != "":
        if self.check_password(input_password, hash):
          return True
      
      return False
        