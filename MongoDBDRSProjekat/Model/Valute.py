class Valute:  
    def __init__(self):
        self.name = ""
        self.amount = 0
    
    def __init__(self, name="", amount=0):
        self.name = name
        self.amount = amount

    def __str__(self):
        str = f"""Information about your valutes
            Name: {self.name}
            Amount: {self.amount}
        """
        return str

    def valute_to_json(self):
        valute = {
            "name" : self.name,
            "amount" : self.amount
        }
        return valute
