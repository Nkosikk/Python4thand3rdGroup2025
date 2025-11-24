import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/data.ini")


class ReadConfig_data():

    def getURLS(self):
        return config.get("URLS", "dev_url")

    def getUsername(self):
        return config.get("login data", "username")

    def getPassword(self):
        return config.get("login data", "password")

    def getName(self):
        return config.get("user information", "name")

    def getFirstName(self):
        return config.get("Registration Info","firstname")

    def getLastName(self):
        return config.get("Registration Info","lastname")

    def getEmail(self):
        return config.get("Registration Info","email")

    def getRegistrationPassword(self):
        return config.get("Registration Info", "password")

    def getConfirmRegistrationPassword(self):
        return config.get("Registration Info","confirm_password")


