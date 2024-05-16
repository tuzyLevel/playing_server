import hashlib





def get_hashed_password(password: str, salt: str):
    data = password.encode('utf-8')

    data_with_salt = salt + data

    sha256_hash = hashlib.sha256()
    sha256_hash.update(data_with_salt)
    hashed_data = sha256_hash.hexdigest()

    return hashed_data
