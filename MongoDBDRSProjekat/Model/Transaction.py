import MongoDBDRSProjekat.Common.Common as common

class Transaction:   
    def __init__(self):
        self.sender_email = ""
        self.reciever_email = ""
        self.amount = 0
        self.transaction_state = common.transaction_state[1]
        self.random_int = 0
        self.transaction_ID = ""
        self.currency_name = ""
    
    def __init__(self, sender_email="", 
                       reciever_email="",
                       amount=0,
                       transaction_state=common.transaction_state[0],
                       random_int=0,
                       transaction_id="",
                       currency_name=""):
        self.sender_email = sender_email
        self.reciever_email = reciever_email
        self.amount = amount
        self.transaction_state = transaction_state
        self.random_int = random_int
        self.transaction_ID = transaction_id
        self.currency_name = currency_name

    def __str__(self):
        print("Transaction")
        print("ID: ", self.transaction_ID)
        print("Sender email: ", self.sender_email)
        print("Reciever email: ", self.reciever_email)
        print("Amount: ", self.amount)
        print("State: ", self.transaction_state)
        print("Random int: ", self.random_int)
        print("Currency name: ", self.currency_name)
     
        






