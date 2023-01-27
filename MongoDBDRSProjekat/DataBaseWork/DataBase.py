import pymongo

from MongoDBDRSProjekat.Common.Common import ca, conn_str, data_base_name
# we use this function to connect to our cloud or cluster
def connect_to_cluster(): 
    try: 
        # we get instance of cluster with MongoClient method
        # we forwarded tslCAFile because of certificates that we made in SBES
        cluster = pymongo.MongoClient(conn_str, tlsCAFile=ca)
        return cluster
    except Exception:
        print("Error: ", Exception)
        return None
        
#function that closes connection to cluster
def close_connection(cluster):  
    cluster.close()

# function that gets data base from our cluster
def get_data_base(cluster): 
    return cluster[data_base_name]

# function that gets our collections, users or transactions
def get_collectiont(collection_name):
    cluster = connect_to_cluster()
    base = get_data_base(cluster)
    collection = base[collection_name]
    return collection
