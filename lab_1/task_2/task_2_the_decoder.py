import os
import json
import sys

from the_json_way_2 import WAY


def create_dict(text: str) -> dict[str:float]:
    """Создаёт словарь из входной строки,  в качестве ключа - слово, в качестве значения - частота встречи"""
    long = len(original_text)
    dictionary = {}
    for symbol in text:
        if symbol in dictionary:
            dictionary[symbol] += 1 / long 
        else:
            dictionary[symbol] = 1 / long 

    return dictionary


def print_dictionary(dictionary: dict) -> None:
    """Красиво выводит входной словарь"""
    for key, value in dictionary.items():
        print(key, ":", value)


if __name__ == "__main__":
    try:
        with open( WAY, "r", encoding="utf-8") as json_file:
            ways = json.load(json_file)
    except Exception as e:
        print("Ошибка при открытие файла json: ", e)

    try:
        with open(ways[0], "r", encoding="utf-8") as file_in:
            original_text = file_in.readline()
            file_in.close()
    except Exception as e:
        print("Ошибка открытия файла с оригинальным текстом: ", e)

    try:
        dictionary_frequency = create_dict(original_text)
        print_dictionary(dictionary_frequency)
    except Exception as e:
        print("Ошибка при обработке словаря частот встреч", e)

    try:
        with open(ways[1], "r", encoding="utf-8") as file_key:
            dic_key=json.load(file_key)
            for k in dic_key.keys():
                print(k, " — ", dic_key[k])
                original_text = original_text.replace(k, dic_key[k])
    except Exception as e:
        print("Возникла ошибка при чтение ключа и/или дешифровки текста", e)

    try:
        with open(ways[2], "w", encoding="utf-8") as  file_out:
            file_out.write(original_text)
            file_out.close()
    except Exception as e:
        print("Ошибка при записи расшифрованного текста", e)
