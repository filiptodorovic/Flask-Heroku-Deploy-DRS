# this is necessary because we cannot connect to base. Reason are some certificates that we
# created in SBES
import certifi
ca = certifi.where()

# name of our data base 
data_base_name = "DataBaseFrankfurt"
data_base_name_local = "DataBaseDRS"
# name of our user collection. In this collection, we will put informations about users
users_collection = "users"

# name of our transaction collection. In this collection, we will put informations about transactions
transaction_collection = "transactions"

# values of dictionary represent state of our transactions
#there can be intial state = none, and 3 other states: in process, processed, declined
transaction_state = ["none", "in process", "processed", "declined"]

#connection string that helps us to connect to our Cluster in Frankfurt  :)
conn_str = "mongodb+srv://Viki:viki123@frankfurtcluster.jlmugvo.mongodb.net/?retryWrites=true&w=majority"
conn_str_local = "mongodb://localhost:27017/"





