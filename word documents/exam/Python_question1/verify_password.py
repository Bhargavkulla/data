from hash_password import hash_password

def verify_password(stored_password: str, password: str) -> bool:
    return stored_password == hash_password(password)