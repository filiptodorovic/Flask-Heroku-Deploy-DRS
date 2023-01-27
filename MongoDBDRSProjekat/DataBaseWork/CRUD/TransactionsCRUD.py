from MongoDBDRSProjekat.Common.Common import transaction_collection
import MongoDBDRSProjekat.DataBaseWork.DataBase as db
from MongoDBDRSProjekat.Model.Transaction import Transaction

class TransactionCRUD:
    def __init__(self):
        self.collection = db.get_collectiont(transaction_collection)

    # function that creates json variable made of fields of Transaction clas
    def class_to_json(self, transaction):
        json_str = {
            "sender_email": transaction.sender_email,
            "reciever_email": transaction.reciever_email,
            "amount": transaction.amount,
            "transaction_state": transaction.transaction_state,
            "random_int": transaction.random_int,
            "transaction_ID": transaction.transaction_ID,
            "currency_name" : transaction.currency_name
        }
        return json_str

    # function that converts json to the class 
    def json_to_class(self, json_str):
        transaction = Transaction(
            json_str["sender_email"],
            json_str["reciever_email"],
            json_str["amount"],
            json_str["transaction_state"],
            json_str["random_int"],
            json_str["transaction_ID"],
            json_str["currency_name"])
        return transaction

    #function that adds new field to the transaction collection (tested)
    def add_transaction(self, transaction):
    
        #we need json format of object, because it takes ONLY json format
        # i tried to use build-in function of json package, but it didn't work
        json_str = self.class_to_json(transaction)
        try:   
            # insert one element to collection to the cluster
            self.collection.insert_one(json_str)
            return True
        except Exception:
            print("Exception(add_transaction): ", Exception) 
            return False 

    # this function deletes all transactions with forwarded email as sender_email (tested)
    def delete_all_by_sender_email(self, sender_email):
        try:
            self.collection.delete_many({"sender_email" : sender_email})
            return True
        except Exception as e:
            print("Exception: ", e.__str__())
            return False     

    # deletes all transactions with forwarded reciever email (tested)
    def delete_all_by_reciever_email(self, reciever_email):
        try:
            self.collection.delete_many({"reciever_email" : reciever_email})
            return True
        except Exception as e:
            print("Exception: ", e.__str__())
            return False    

    #deletes one transaction with transaction_id (tested)
    def delete_one_by_id(self, transaction_id):
        try:
            self.collection.delete_one({"transaction_ID" : transaction_id})
            return True
        except Exception as e:
            print("Exception: ", e.__str__())
            return False

    # returns all transactions those contain email as reciever email or sender email (tested)
    def find_all_by_email(self, email):
        try:
            #collection.find returns cursor and we will get elements by iterating trought cursor
            sender_cursor = self.collection.find({"sender_email" : email})
            reciever_cursor = self.collection.find({"reciever_email" : email})
            list = [] 
            for elem in sender_cursor: 
                list.append(elem)
            for elem in reciever_cursor:   
                list.append(elem)
            return list
        except Exception: 
            print("Exception: ", Exception)
            return None

    # find all instances that have a forwarded sender email (tested)
    def find_by_sender_email(self, sender_email):
        try:
            sender_cursor = self.collection.find({"sender_email" : sender_email})
            list = [] 
            for elem in sender_cursor: 
                list.append(self.json_to_class(elem))
            return list
        except Exception: 
            print("Exception: ", Exception)
            return None


    # this functions finds all transaction with forwarded currency_name (not tested)
    def find_by_currency_name(self, currency_name):
        try:
            currency_cursor = self.collection.find({"currency_name" : currency_name })
            list = []
            for elem in currency_cursor:
                list.append(self.json_to_class(elem))
            return list
        except Exception:
            print("Exception", Exception)
            return None


    # find all instances that have a reciever forwarded email (tested)
    def find_by_reciever_email(self, reciever_email):
        try:
            reciever_cursor = self.collection.find({"reciever_email" : reciever_email})
            list = [] 
            for elem in reciever_cursor: 
                list.append(self.json_to_class(elem))
            return list
        except Exception: 
            print("Exception: ", Exception)
            return None

    # find by transaction_ID (tested)
    def find_by_id(self, transaction_ID):
        try:
            transaction = self.collection.find_one({"transaction_ID" : transaction_ID})
            return self.json_to_class(transaction)
        except Exception: 
            print("Exception: ", Exception)
            return None

    # this function update ONE field which name is 'field_name' to 'field_value'
    # we need (tested)
    def update_transaction_field(self, transaction_ID, field_name, field_value):
        try: 
            self.collection.update_one({"transaction_ID" : transaction_ID},{"$set" : {field_name : field_value}})
            return True
        except Exception:
            print("Exception: ", Exception)
            return False
            
    # updates whole transaction. Need to send new transaction, or updated version of the same transaction
    # (tested)
    def update_whole_transaction(self, transaction):
        try: 
            updated_transaction = self.class_to_json(transaction)
            result = self.collection.update_one(
                {"transaction_ID" : transaction.transaction_ID}, 
                {"$set" : updated_transaction})
            print(result.matched_count, result.modified_count)
            return True
        except Exception:
            print("Exception: ", Exception)
            return False




    



