import sha512_crypt

def encrypt_password(password: str) -> str:
    return sha512_crypt.encrypt(password)

def verify_password(encrypt_password: str, password: str) -> bool:
    return sha512_crypt.verify(password, encrypt_password)


if __name__ == '__main__':
    print(encrypt_password('register_key'))