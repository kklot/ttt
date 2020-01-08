import hashlib

def gen_hash_tt(a, b):
    return hashlib.sha256(str.encode(a+b)).hexdigest()