import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def create_sym_key() -> bytes:
    return os.urandom(32)

def serialize_sym(key: bytes, path: str) ->None:
    try:
        with open(path, "wb") as file:
            file.write(key)
    except Exception as e:
        print("Возникла ошибка при сиреализации симетричного ключа: ", e)

def encrypt_sym_key(asym_key: dict, sym_key: bytes) -> bytes:
    return asym_key['public'].encrypt(sym_key,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))

def deserialize_sym(path: str) ->bytes:
    try:
        with open(path, "rb") as file:
            key=file.read()
        return key
    except Exception as e:
        print("Возникла ошибка при ltсиреализации симетричного ключа: ", e)

def decrypt_sym_key(asym_key: dict, key: bytes) -> bytes:
        un_key = asym_key['private'].decrypt(key,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
        return un_key

def encrypt_text(text:bytes, key: bytes) -> bytes:
    padder = padding.ANSIX923(32).padder()
    text = bytes('кто прочитал тот здохнет', 'UTF-8')
    padded_text = padder.update(text)+padder.finalize()
    iv = os.urandom(16) #случайное значение для инициализации блочного режима, должно быть размером с блок и каждый раз новым
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    c_text = encryptor.update(padded_text) + encryptor.finalize()
    return c_text
