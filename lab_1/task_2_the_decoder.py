import os
import json
import sys


def creat_dict(text: str) -> dict[str:float]:
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
    way={1: 'isb\\lab_1\\task_2_ways.json'}
    try:
        json_file = open( way[1], "r", encoding="utf-8")
        ways = json.load(json_file)
    except Exception as e:
        print("Ошибка при открытие файла json: ", e)

    try:
        file_in = open(ways[0], "r", encoding="utf-8")
        original_text = file_in.readline()
        file_in.close()
    except Exception as e:
        print("Ошибка открытия файла с оригинальным текстом: ", e)

    try:
        dictionary_frequency = creat_dict(original_text)
        print_dictionary(dictionary_frequency)
    except Exception as e:
        print("Ошибка при обработке словаря частот встреч", e)

    try:
        file_key = open(ways[1], "r", encoding="utf-8")
        dic_key=json.load(file_key)

        for k in dic_key.keys():
            print(k, " — ", dic_key[k])
            original_text = original_text.replace(k, dic_key[k])

        file_key.close()
    except Exception as e:
        print("Возникла ошибка при чтение ключа и/или дешифровки текста", e)

    try:
        file_out = open(ways[2], "w", encoding="utf-8")
        file_out.write(original_text)
        file_out.close()
    except Exception as e:
        print("Ошибка при записи расшифрованного текста", e)
