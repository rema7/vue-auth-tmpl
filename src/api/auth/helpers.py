import secrets

from passlib.hash import pbkdf2_sha256


def generate_token():
    return secrets.token_hex(16)


def generate_password_hash(password):
    return pbkdf2_sha256.encrypt(password, rounds=200000, salt_size=16)


def verify_password(password, password_hash):
    try:
        return pbkdf2_sha256.verify(password, password_hash)
    except:
        return False
