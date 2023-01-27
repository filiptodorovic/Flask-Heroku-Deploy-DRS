import pymongo

#OVO MORA ZBOG NEKIH SERTIFIKATA DA SE DODA
import certifi
ca = certifi.where()

#string sa kojim se registrujemo na nas cluster
# parametri koji se dodaju
# password: mile123
# ispred ?retry: naziv baze, u mom slucaju DRSDataBase, 
conn_str = "mongodb+srv://new-user-2:bPwxQvmK1ulLHGoL@cluster2.wtppceb.mongodb.net/userDataBase?retryWrites=true&w=majority"
try:
    #ovde se povezujemo ka nasoj bazi
    client = pymongo.MongoClient(conn_str, tlsCAFile=ca)
except Exception:
    print("Error: " + Exception)

#kreiranje database
db = client["userDataBase"]
collection = db["userCollection"]

user = {
    "name" : "Mile",
    "lastName" : "Zivkovic",
    "creditCard" : [
        {
            "cardNumber": 1233333,
            "emailSender": "mile@gmail.com",
            "emailReciever" : "zile@gmail.com"
        }
    ]
}
lastName = "Zivkovic"
collection.insert_one(user)
user = collection.find_one({"lastName" : lastName})
print(user)
client.close()











