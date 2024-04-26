import re
import os
import json
import io
import codecs
import sys


def clean(text: str) -> str:
    """Удаляет все символы кроме букв в входном тексте, даже пробелы, делает все буквы маленькими"""
    text = re.sub("[^a-zа-яё]", "", text, flags=re.IGNORECASE)
    text = text.lower()
    return text


def encrypt(text: str) -> str:
    """Шифрует входной текст, врзвращает зашифрованный"""

    try:
        file_c = open(ways[2], "r", encoding="utf-8")
        try:
            const = int(file_c.readline())
            file_c.close()
        except Exception as e:
            print("При чтение константы возникла ошибка: ", e)
            file_c.close()
    except Exception as e:
        print("При работе с файлом констант возникла ошибка: ", e)

    temp = len(text)
    while temp % const != 0:
        text = text + "а"
        temp += 1
    quantity = int(temp / const)
    print(quantity, "*", const, "=",len(text),"=",temp)
    cyphered = ""
    for j in range(0, const):
        for i in range(0, quantity):
            cyphered += text[const * i + j]
    print("Cyphered_text: ", cyphered)
    return cyphered


def writing(text: str) -> None:
    """Осуществляет запись в файл-ключ"""
    

    file_c = open(ways[2], "r", encoding="utf-8")
    try:
        const = int(file_c.readline())
        file_c.close()
    except Exception as e:
        print("При чтение константы возникла ошибка: ", e)
        file_c.close()

    c = int(len(text)/const)
    print(len(text),"=", const,"*",c)

    try:
        file_k = open(ways[1], "w", encoding="utf-8")
    except Exception as e:
        print("При попытке открытия файла c ключом возникла ошибка: ", e)

    for j in range(0, c):
        for i in range(0, const):
            file_k.write(" " + text[c * i + j])
        file_k.write("\n")
    file_k.write(
        "\n\n Записываем текст в строчку, когда заканчивается переходим на следующую, для шифровки после получение таблицы, выписывает столбцы"
    )
    file_k.close()



if __name__ == "__main__":
    way={1: 'isb\\lab_1\\task_1_way.json'}
    try:
        json_file = open(
            way[1], "r", encoding="utf-8"
        )
        ways = json.load(json_file)
    except Exception as e:
        print("При попытке открытия файла с путями возникла ошибка: ", e)

    try:
        file_in = open(ways[0], "r", encoding="utf-8")
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


