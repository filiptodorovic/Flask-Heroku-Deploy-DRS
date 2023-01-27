import MongoDBDRSProjekat.Common.Common as common

class User:
    def __init__(self):
        self.name = ""
        self.last_name = ""
        self.address = ""
        self.city = ""
        self.country = ""
        self.telephone_number = 0
        self.email = ""
        self.password = ""
        self.credit_card = []
        self.online_balance = []

    def __init__(self, name="", last_name="", address="", city="", country="",
                 telephone_number=0, email="", password="", credit_card=[], online_balance=[]):
        self.name = name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.country = country
        self.telephone_number = telephone_number
        self.email = email
        self.password = password
        self.credit_card = credit_card
        self.online_balance = online_balance 
        
    def __str__(self):
        print("User:")
        print("Name: ", self.name)
        print("Last name: ", self.last_name)
        print("Address: ", self.address)
        print("Country: ", self.country)
        print("Telephone number: ", self.telephone_number)
        print("Email: ", self.email)
        print("Password: ", self.password)
        for cc in self.credit_card:
            print(cc)
        for ob in self.online_balance:
            print(ob)

