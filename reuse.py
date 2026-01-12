import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def detect_reuse(passwords):
    hashes = [hash_password(p) for p in passwords]
    return len(hashes) != len(set(hashes))
