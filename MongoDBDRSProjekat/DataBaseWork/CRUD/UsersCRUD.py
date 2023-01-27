from MongoDBDRSProjekat.Common.Common import users_collection
import MongoDBDRSProjekat.DataBaseWork.DataBase as db
from MongoDBDRSProjekat.Model.Valute import Valute
from MongoDBDRSProjekat.Model.CreditCard import CreditCard
from MongoDBDRSProjekat.Model.User import User


class UserCRUD:
    def __init__(self):
        self.collection = db.get_collectiont(users_collection) 

    # converts user to json (tested)
    def class_to_json(self, user):
        json_card = user.credit_card.card_to_json()
        json_online_balance = []
        
        for valute in user.online_balance:
            val_json = valute.valute_to_json()
            json_online_balance.append(val_json)

        json_user = {
            "name" : user.name,
            "last_name" : user.last_name,
            "address" : user.address,
            "city" : user.city,
            "country" : user.country,
            "telephone_number" : user.telephone_number,
            "email" : user.email,
            "password" : user.password,
            "credit_card" : json_card,
            "online_balance" : json_online_balance
        }
        return json_user

    # converts json to user
    def json_to_class(self, json_user):
        user = User()
        json_valute = json_user["online_balance"]

        for elem in json_valute:
            valute = Valute(elem["name"], elem["amount"])
            user.online_balance.append(valute)
        
        json_card = json_user["credit_card"]
        card = CreditCard(json_card["card_number"], json_card["name_of_user"], json_card["expiration_date"], json_card["security_code"])
        
        user.credit_card = card
        user.name = json_user["name"]
        user.last_name = json_user["last_name"]
        user.address = json_user["address"]
        user.city = json_user["city"]
        user.country = json_user["country"]
        user.telephone_number = json_user["telephone_number"]
        user.email = json_user["email"]
        user.password = json_user["password"]

        return user

    # add new user (tested)
    def add_user(self, user):
        #we need json format of object, because it takes ONLY json format
        # i tried to use build-in function of json package, but it didn't work
        json_str = self.class_to_json(user)
        try:   
            # insert one element to collection to the cluster
            self.collection.insert_one(json_str)
            return True
        except Exception:
            print("Exception: ", Exception) 
            return False 

    #find user by email (tested)
    def find_user_by_email(self, email):
        try:
            cursor = self.collection.find_one({"email" : email})
            user = self.json_to_class(cursor)
            return user
        except: 
            print("Exception: ", Exception)
            return None

    # update user(user cannot change email address!!!!!!!!!!!!) (tested)
    def update_user(self, user):
        try:
            updated_user = self.class_to_json(user)
            result = self.collection.update_one({"email" : user.email}, {"$set" : updated_user})
            print(result.matched_count, result.modified_count)
            return True
        except Exception:
            print("Exception: ", Exception)
            return False

    # add new valute (tested)
    def add_new_valute(self, email, new_valute):
        try:
            val_json = new_valute.valute_to_json()
            result = self.collection.update_one({"email" : email}, {"$push" : {"online_balance" : val_json}})
            return True
        except Exception:
            print("Exception: ", Exception)
            return False
    
    # update amount (tested)
    def update_amount(self, email, valute_name, amount):
        try:
            result = self.collection.update_one({"email" : email, "online_balance.name" : valute_name}, 
            {"$set" : {"online_balance.$.amount" : amount}})
            print(result.matched_count, result.modified_count)
            return True
        except Exception:
            print("Exception: ", Exception)
            return False;

    #delete valute
    def delete_valute(self, email, valute_name):
        try:
            result = self.collection.update_many({"email" : email},
            {"$pull" : {"online_balance" : {"name" : valute_name}}})
            print(result.matched_count, result.modified_count)
            return True
        except Exception:
            print("Exception: ", Exception)
            return False


    #find all user's valutes (tested)
    # 2 solution:
    # 1.) Get whole user and parse him to class than return his online_balance field
    '''
        def find_user_valutes(self, email):
            try: 
            result = self.collection.find_one({"email" : email})
            user = self.json_to_class(result)
            return user.online_balance 
        except Exception:
            print("Exception: ", Exception)
            return None
    '''
    # i think this is not optimal solution, because we have to take whole user. What if 
    # we have a lot of datas about user, that would be slow and it would take a lot of memory

    # 2.) Through query take only online_balance field and covert it to list (i did this solution)
    # if you need more explanations, call me 
    def find_user_valutes(self, email):
        try: 
            user_valutes = []
            result = self.collection.find({"email" : email}, 
            {"online_balance" : 1, "_id" : 0}) # this _id = 0 writes because we don't want to return _id
            # print(result) gives memory addres
            for elem in result: # we must iterate through result, we cannot write valutes = result["online_balance"]
                valutes = elem["online_balance"] # than mapping array to variable
                # print(valutes) gives array of objects in json format
                # valutes variable is now our array of json valute objects 
                for val in valutes: # val is ONE json object in array
                    valute = Valute(val["name"], val["amount"]) # parse json object to valute object
                    user_valutes.append(valute) # add valute to array
            return user_valutes
        except Exception:
            print("Exception: ", Exception)
            return None

    #find one user's valute (tested)
    def find_one_valute(self, email, valute_name):
        try:
            result = self.collection.find_one({"email" : email})
            user = self.json_to_class(result)
            for elem in user.online_balance:
                if elem.name == valute_name:
                    return elem
            return None
        except Exception:
            print("Exception: ", Exception)
            return None

    # add new card we will see about this, may one user can have only one card
    def add_new_card(self, email, new_card):
        try:
            val_json = new_card.card_to_json()
            result = self.collection.update_one({"email": email}, {"$push": {"credit_card": val_json}})
            return True
        except Exception:
            print("Exception: ", Exception)
            return False

    

    #delete card we will see about this, may we cannot delete card, because user have to have only one card

    # find user's cards


