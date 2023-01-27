class CreditCard:
    def __init__(self):
        self.card_number
        self.name_of_user
        self.expiration_date
        self.security_code
    
    def __init__(self, card_number=0, name_of_user="", expiration_date=None, security_code=0):
        self.card_number = card_number
        self.name_of_user = name_of_user
        self.expiration_date = expiration_date
        self.security_code = security_code

    def __str__(self): 
        str = f""" Information about Credit Card
    Credit Card: {self.card_number}
    Name: {self.name_of_user}
    Expiration Date: {self.expiration_date}
    Security Code: {self.security_code}
    """
        return str

    def card_to_json(self):
        card = {
            "card_number" : self.card_number,
            "name_of_user" : self.name_of_user,
            "expiration_date" : self.expiration_date,
            "security_code" : self.security_code
        }
        return card
        
