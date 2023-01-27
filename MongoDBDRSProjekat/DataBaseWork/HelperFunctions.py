from Crypto.Hash import keccak
import random
# function that returns hash value, and we will use it as value of transaction_id
# used keccak256
def get_hash_transaction_id(sender_email, reciever_email, amount, random_int):
    hash_value = keccak.new(digest_bits=256)  # 256 represents 256 bites of hash values
    hash_string = sender_email + reciever_email + str(amount) + str(random_int)
    
    # update function takes bytes of strings, so we must convert our string to bytes
    string_bytes = bytes(hash_string, 'utf-8')
    hash_value.update(string_bytes)
    
    # there is our hash value
    return hash_value.hexdigest()

# function that return random int in range of 1 to 1000000    
def get_random_int():
    return random.randint(1, 1000000)


def get_hash_password(password):
    hash_value = keccak.new(digest_bits=256)  # 256 represents 256 bites of hash values

    # update function takes bytes of strings, so we must convert our string to bytes
    string_bytes = bytes(password, 'utf-8')
    hash_value.update(string_bytes)

    # there is our hash value
    return hash_value.hexdigest()