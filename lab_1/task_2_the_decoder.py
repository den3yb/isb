import os
import json
import sys


def creat_dict(text: str) -> dict:
    """Создаёт словарь из входной строки,  в качестве ключа - слово, в качестве значения - частота встречи"""
    long = len(original_text)
    dictionary = {}
    for symbol in text:
        if symbol in dictionary:
            dictionary[symbol] += 1 / long * 100
        else:
            dictionary[symbol] = 1 / long * 100

    return dictionary


def print_dictionary(dictionary: dict) -> None:
    """Красиво выводит входной словарь"""
    for key, value in dictionary.items():
        print(key, ":", value)


if __name__ == "__main__":
    if os.path.exists("C:\\Proganiy\\OiB\\isb\\lab_1\\task_2_ways.json"):
        json_file = open(
            "C:\\Proganiy\\OiB\\isb\\lab_1\\task_2_ways.json", "r", encoding="utf-8"
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

    dictionary_chastot = creat_dict(original_text)
    print_dictionary(dictionary_chastot)

    file_key = open("isb\lab_1\Task 2 Key.txt", "w", encoding="utf-8")
    dic_key={
        '-': ' ',
        '/': 'К',
        '2': 'И',
        'n': 'С',
        '8': 'В',
        '6': 'А',
        's': 'Ь',
        '5': 'Д',
        'e': 'О',
        'r': 'П',
        '3': '3',
        '0': 'Е',
        'i': 'Т',
        'w': 'Н',
        'm': 'Р',
        'q': 'М',
        '\\': 'Л',
        ';': 'Ы',
        '`': 'Я',
        '7': 'Б',
        't': 'Х',
        '1': 'Й',
        'k': 'Ч',
        'o': 'У',
        'z': 'Ю',
        'c': 'Щ',
        'p': 'Ф',
        '9': 'Г',
        'f': 'Ц',
        'd': 'Ш',
        '4': 'Ж',
        '?': 'Ъ',
        'x': 'Э'
    }

    for k in dic_key.keys():
        print(k, " — ", dic_key[k])
        file_key.write(k + " — " + dic_key[k] + "\n")
        original_text = original_text.replace(k, dic_key[k])

    file_key.close()

    if os.path.exists(ways[2]):
        file_out = open(ways[2], "w", encoding="utf-8")
        file_out.write(original_text)
        file_out.close()
    else:
        print("Неверно указан путь к файлу с оригинальным текстом")
        sys.exit()
