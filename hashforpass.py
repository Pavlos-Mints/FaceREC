import hashlib

def hashing(password) :
    hash = hashlib.sha256(password)

    return hash