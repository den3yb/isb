from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def create_asym_key(size: int) -> dict:
    keys = rsa.generate_private_key(
    public_exponent=65537,
    key_size=size
    )
    asym ={
        'private': keys,
        'public': keys.public_key()
    }
    print(type(keys))
    print(type(keys.public_key()))
    return asym

def serialize_private(key: dict, path: str) ->None:
    try:
        with open(path, "wb") as file:
            file.write(key['private'])
    except Exception as e:
        print("Возникла ошибка при сиреализации симетричного ключа: ", e)

def serialize_public(key: dict, path: str) ->None:
    try:
        with open(path, "wb") as file:
            file.write(key['public'])
    except Exception as e:
        print("Возникла ошибка при сиреализации симетричного ключа: ", e)

