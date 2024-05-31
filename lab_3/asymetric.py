from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key

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
            file.write(key.private_bytes(encoding=serialization.Encoding.PEM,
              format=serialization.PrivateFormat.TraditionalOpenSSL,
              encryption_algorithm=serialization.NoEncryption()))
    except Exception as e:
        print("Возникла ошибка при сиреализации симетричного ключа: ", e)

def serialize_public(key: dict, path: str) ->None:
    try:
        with open(path, "wb") as file:
            file.write(key.public_bytes(encoding=serialization.Encoding.PEM,
             format=serialization.PublicFormat.SubjectPublicKeyInfo))

    except Exception as e:
        print("Возникла ошибка при сиреализации симетричного ключа: ", e)

def deserylie_asym(public_path: str, private_path: str) -> dict:
    with open(public_path, 'rb') as pem_in:
        public_bytes = pem_in.read()
        d_public_key = load_pem_public_key(public_bytes)
    with open(private_path, 'rb') as pem_in:
        private_bytes = pem_in.read()
        d_private_key = load_pem_private_key(private_bytes,password=None,)
    asym ={
        'private': d_private_key,
        'public': d_public_key
    }
    return asym