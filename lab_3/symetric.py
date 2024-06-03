import os
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def create_sym_key() -> bytes:
    return os.urandom(16)


def serialize_sym(key: bytes, path: str) -> None:
    try:
        with open(path, "wb") as file:
            file.write(key)
    except Exception as e:
        print("Возникла ошибка при сиреализации симетричного ключа: ", e)


def deserialize_sym(path: str) -> bytes:
    try:
        with open(path, "rb") as file:
            key = file.read()
        return key
    except Exception as e:
        print("Возникла ошибка при десиреализации симетричного ключа: ", e)


def encrypt_text(text: str, key: bytes) -> bytes:
    padder = padding.PKCS7(64).padder()
    bi_text = bytes(text, "UTF-8")
    iv = os.urandom(8)
    cipher = Cipher(algorithms.IDEA(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    padded_text = padder.update(bi_text) + padder.finalize()
    c_text = iv + encryptor.update(padded_text) + encryptor.finalize()
    return c_text


def decode_text(c_text: bytes, key: bytes) -> str:
    iv = c_text[:8]
    cipher_text = c_text[8:]
    cipher = Cipher(algorithms.IDEA(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    dc_text = decryptor.update(cipher_text) + decryptor.finalize()
    unpadder = padding.PKCS7(64).unpadder()
    unpadded_dc_text = unpadder.update(dc_text) + unpadder.finalize()
    return unpadded_dc_text.decode("UTF-8")
