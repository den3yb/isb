import os
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def create_sym_key() -> bytes:
    return os.urandom(16)

def serialize_sym(key: bytes, path: str) ->None:
    try:
        with open(path, "wb") as file:
            file.write(key)
    except Exception as e:
        print("Возникла ошибка при сиреализации симетричного ключа: ", e)



def deserialize_sym(path: str) ->bytes:
    try:
        with open(path, "rb") as file:
            key=file.read()
        return key
    except Exception as e:
        print("Возникла ошибка при десиреализации симетричного ключа: ", e)

def encrypt_text(text:bytes, key: bytes) -> bytes:
    iv = os.urandom(8) 
    cipher = Cipher(algorithms.IDEA(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(64).padder()
    text = bytes('кто прочитал тот здохнет', 'UTF-8')
    padded_text = padder.update(text)+padder.finalize()
    c_text = encryptor.update(padded_text) + encryptor.finalize()
    return c_text
