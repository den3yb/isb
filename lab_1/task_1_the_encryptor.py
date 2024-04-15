import re
import os
import json
import io
import codecs
import sys


def clean_text(text: str) -> str:
    """Удаляет все символы кроме букв у входного текста, даже пробелы, делает все буквы маленькими"""
    text = re.sub("[^a-zа-яё]", "", text, flags=re.IGNORECASE)
    text = text.lower()
    return text


def text_to_cyphered(text: str) -> str:
    """Шифрует входной текст, врзвращает зафифрованный"""

    if os.path.exists(ways[2]):
        file_c = open(ways[2], "r", encoding="utf-8")
        try:
            const = int(file_c.readline())
            file_c.close()
        except ValueError:
            print("Неверно указана константа для шифрования")
            file_c.close()
            sys.exit()
    else:
        print("Неверно указан путь к файл константам")
        sys.exit()
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


def test(text: str) -> str:
    """Осуществляет проверку-дешифровку данного конкретного текста, с учётом знания параметров таблицы"""

    if os.path.exists(ways[1]):
        file_k = open(ways[1], "w", encoding="utf-8")
    else:
        print("Неверно указан путь к файл константам")
        sys.exit()

    uncyphered = ""
    for j in range(0, 8):
        for i in range(0, 63):
            uncyphered += text[9 * i + j]
            file_k.write(" " + text[9 * i + j])
        file_k.write("\n")
    file_k.write(
        "\n\n Записываем текст в строчку, когда заканчивается переходим на следующую, для шифровки после получение таблицы, выписывает столбцы"
    )
    file_k.close()
    return uncyphered


if __name__ == "__main__":
    if os.path.exists("C:\\Proganiy\\OiB\\isb\\lab_1\\task_1_way.json"):
        json_file = open(
            "C:\\Proganiy\\OiB\\isb\\lab_1\\task_1_way.json", "r", encoding="utf-8"
        )
        ways = json.load(json_file)
    else:
        print("Невверно указан путь к json файлу")
        sys.exit()

    if os.path.exists(ways[0]):
        file_in = open(ways[0], "r", encoding="utf-8")
        original_text = file_in.readline()
        if (original_text == ''):
            print("Заданный текст не прописан")
            sys.exit()
        file_in.close()
    else:
        print("Неверно указан путь к файлу с оригинальным текстом")
        sys.exit()

    if original_text != "":
        cyphered_text = clean_text(original_text)
        cyphered_text = text_to_cyphered(cyphered_text)
        test(cyphered_text)
    else:
        print("Текст не задан")
        sys.exit()


