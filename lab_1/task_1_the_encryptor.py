import re
import os
import json
import io
import codecs
import sys

from the_json_way_1 import WAY


def clean(text: str) -> str:
    """Удаляет все символы кроме букв в входном тексте, даже пробелы, делает все буквы маленькими"""
    text = re.sub("[^a-zа-яё]", "", text, flags=re.IGNORECASE)
    text = text.lower()
    return text


def encrypt(text: str) -> str:
    """Шифрует входной текст, врзвращает зашифрованный"""

    try:
        with open(ways[2], "r", encoding="utf-8") as file_c:
            const = int(file_c.readline())
    except Exception as e:
        print("При работе с файлом констант возникла ошибка: ", e)

    temp = len(text)
    while temp % const != 0:
        text = text + "а"
        temp += 1
    quantity = int(temp / const)
    cyphered = ""
    for j in range(0, const):
        for i in range(0, quantity):
            cyphered += text[const * i + j]
    print("Cyphered_text: ", cyphered)
    return cyphered


def writing(text: str) -> None:
    """Осуществляет запись в файл-ключ"""
    

    
    try:
        with open(ways[2], "r", encoding="utf-8") as file_c:
            const = int(file_c.readline())
    except Exception as e:
        print("При чтение константы возникла ошибка: ", e)

    c = int(len(text)/const)

    try:
        with open(ways[1], "w", encoding="utf-8") as file_k: 
            for j in range(0, c):
                for i in range(0, const):
                    file_k.write(" " + text[c * i + j])
                file_k.write("\n")
            file_k.write(
                "\n\n Записываем текст в строчку, когда заканчивается переходим на следующую, для шифровки после получение таблицы, выписывает столбцы"
            )
    except Exception as e:
        print("При попытке открытия файла c ключом возникла ошибка: ", e)

    



if __name__ == "__main__":
    try:
        with open( WAY, "r", encoding="utf-8") as json_file:
            ways = json.load(json_file)
    except Exception as e:
        print("При попытке открытия файла с путями возникла ошибка: ", e)

    try:
        with open(ways[0], "r", encoding="utf-8") as file_in:
            original_text = file_in.readline()
            if (original_text == ''):
                print("Заданный текст не прописан")
            file_in.close()
    except Exception as e:
        print("При попытке открытия файла с путями возникла ошибка: ", e)
        

    try:
        cyphered_text = clean(original_text)
        cyphered_text = encrypt(cyphered_text)
        writing(cyphered_text)
    except Exception as e:
        print("При попытке работы с текстом возникла ошибка: ", e)


