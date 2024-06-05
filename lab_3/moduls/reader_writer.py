import json

class Texting:

    def read_json_file(path: str) -> list:
        try:
            with open(path, "r", encoding="UTF-8") as file:
                return json.loads(file.read())
        except Exception as e:
            print("Возникла ошибка открытия файла с путями")

    def write_bytes( path: str, key: bytes) -> None:
        try:
            with open(path, 'wb') as key_file:
                key_file.write(key)
        except Exception as e:
            print("Возникла ошибка при записи байтов: ", e)

    def read_bytes(path: str) -> bytes:
        try:
            with open(path, 'rb') as file:
                return file.read()
        except Exception as e:
            print("Возникла ошибка при чтении байтов: ", e)   
    
    def read_file(source_file_path: str) -> str:
        try:
            with open(source_file_path, "r", encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            print("Возникла ошибка при чтении файла: ", e)

    def write_file(path: str, text: str) -> None:
        try:
            with open(path,"w", encoding='utf-8') as file:
                file.write(text)
        except Exception as e:
            print("Возникла ошибка при записи файла: ", e)