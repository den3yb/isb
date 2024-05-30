import os

def create_sym_key() -> bytes:
    return os.urandom(32)

def serialize_sym(key: bytes, path: str) ->None:
    try:
        with open(path, "wb") as file:
            file.write(key)
    except Exception as e:
        print("Возникла ошибка при сиреализации симетричного ключа: ", e)
