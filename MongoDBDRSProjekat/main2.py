
from Model.Transaction import Transaction
from Model.User import User
from Model.CreditCard import CreditCard
from Model.Valute import Valute
from DataBaseWork.CRUD.TransactionsCRUD import TransactionCRUD
from DataBaseWork.CRUD.UsersCRUD import UserCRUD
from Common.Common import transaction_state
import json
import datetime

def check(input):
    if(input):
        print("Succesfully")
    else:
        print("Not successfully")

transCRUD = TransactionCRUD()
'''
transaction1 = Transaction("miloje@gmail.com", "zika@gmail.com", 3000, transaction_id="2233")
transaction2 = Transaction("stojan@gmail.com", "zika@gmail.com", 20000, transaction_id="1122")
transaction3 = Transaction("djox@gmail.com", "stojan@gmail.com", 24000, transaction_id="112222")
transaction4 = Transaction("stojan@gmail.com", "djox@gmail.com", 200500, transaction_id="11")
transaction5 = Transaction("miloje@gmail.com", "djox@gmail.com", 20200, transaction_id="12")
check(transCRUD.add_transaction(transaction1))
check(transCRUD.add_transaction(transaction2))
check(transCRUD.add_transaction(transaction3))
check(transCRUD.add_transaction(transaction4))
check(transCRUD.add_transaction(transaction5))

list = transCRUD.find_all_by_email("stojan@gmail.com")
for elem in list:
    print(elem)

check(transCRUD.delete_one_by_id("112222"))

check(transCRUD.delete_all_by_reciever_email("djox@gmail.com"))

check(transCRUD.delete_all_by_sender_email("miloje@gmail.com"))

list = transCRUD.find_by_sender_email("miloje@gmail.com")
for elem in list:
    elem.__str__()

list = transCRUD.find_by_reciever_email("djox@gmail.com")
for elem in list:
    elem.__str__()

check(transCRUD.update_transaction_field("12", "amount", 30))

trans = transCRUD.find_by_id("12")
trans.__str__()

trans = transCRUD.find_by_id("11")
trans.amount = 432.32
trans.reciever_email = "AAAAA@gmail.com"
trans.transaction_state = transaction_state[1]

check(transCRUD.update_whole_transaction(trans))

card = CreditCard(1234124, "Mile", datetime.datetime(2023, 1, 1), 123123)
bitcoin = Valute("Bitcoin", 2000)
dollars = Valute("Dollar", 500000)
euro = Valute("Euro", 3000)
user1 = User("Slobodan", "Zivkovic", "Brzi Brod BB", "Nis", "Serbia", 69696969, "polupoljoprivrednik@gmail.com", "polucovek", [card], [bitcoin, dollars, euro])

#user = userCRUD.class_to_json(user1)
#print(user)

#check(userCRUD.add_user(user1))

find_user = userCRUD.find_user_by_email("polupoljoprivrednik@gmail.com")
find_user.__str__()
'''
userCRUD = UserCRUD()
email_slobodan = "polupoljoprivrednik@gmail.com"
email_stojan = "stojandragica@gmail.com"

'''dinar = Valute("Dinar", 50)
check(userCRUD.add_new_valute(email, dinar))'''
'''
card = CreditCard(1234124, "Mile", datetime.datetime(2023, 1, 1), 123123)
bitcoin = Valute("Bitcoin", 2000)
dollars = Valute("Dollar", 500000)
euro = Valute("Euro", 3000)
user1 = User("Slobodan", "Zivkovic", "Brzi Brod BB", "Nis", "Serbia", 69696969, "polupoljoprivrednik@gmail.com", "polucovek", [card], [bitcoin, dollars, euro])
userCRUD.add_user(user1)

check(userCRUD.update_amount(email, "Euro", 10000))
check(userCRUD.add_user(user))

card = CreditCard(14333124, "Stojan", datetime.datetime(2025, 1, 1), 123222)
bitcoin = Valute("Bitcoin", 2)
dollars = Valute("Dollar", 503)
euro = Valute("Euro", 30)

user = User("Stojan", "Simic", "Jezero Celije BB", "Krusevac", "Serbia", 636363636, "stojandragica@gmail.com",
    "stojanmolim", [card], [bitcoin, dollars, euro])

user.online_balance.append(Valute("Kuwait dinar", 20000))
user.city = "Kraljevo"
user.telephone_number = 222333222
user.address = "Dositejeva 29"

check(userCRUD.update_user(user))

list = userCRUD.find_user_valutes(email_slobodan)
for elem in list:
    print(elem.__str__())

valute = userCRUD.find_one_valute(email_slobodan, "Dollar")
print("Valute of " + email_slobodan + " " + valute.__str__())
'''

#check(userCRUD.delete_valute(email_slobodan, "Dollar"))
'''list = userCRUD.find_user_valutes(email_stojan)
for elem in list:
    print(elem.__str__())
'''

'''user1 = User("Djokica", "Djokic", "Rajkova 22", "Blace", "Serbia", 222333444, "djole@gmail.com", "djole", [], [])
userCRUD.add_user(user1)'''
check(userCRUD.add_new_card("djole@gmail.com", CreditCard(1233322234, "Djokica", datetime.datetime(2055, 1, 1), 4422341)))

t = Transaction(email_slobodan, email_stojan, 2000,random_int=4, transaction_id="444555333", currency_name="Bitcoin")
transCRUD.add_transaction(t)
