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


file_in = open("isb\lab_1\cod9.txt", "r", encoding="utf-8")
original_text = file_in.readline()
file_in.close()


dictionary_chastot = creat_dict(original_text)
print_dictionary(dictionary_chastot)

original_text = original_text.replace("-", " ")
original_text = original_text.replace("/", "К")
original_text = original_text.replace("2", "И")
original_text = original_text.replace("n", "С")
original_text = original_text.replace("8", "В")
original_text = original_text.replace("6", "А")
original_text = original_text.replace("s", "Ь")
original_text = original_text.replace("5", "Д")
original_text = original_text.replace("e", "О")
original_text = original_text.replace("r", "П")
original_text = original_text.replace("3", "3")
original_text = original_text.replace("0", "Е")
original_text = original_text.replace("i", "Т")
original_text = original_text.replace("w", "Н")
original_text = original_text.replace("m", "Р")
original_text = original_text.replace("q", "М")
original_text = original_text.replace("\\", "Л")
original_text = original_text.replace(";", "Ы")
original_text = original_text.replace("`", "Я")
original_text = original_text.replace("7", "Б")
original_text = original_text.replace("t", "Х")
original_text = original_text.replace("1", "Й")
original_text = original_text.replace("k", "Ч")
original_text = original_text.replace("o", "У")
original_text = original_text.replace("z", "Ю")
original_text = original_text.replace("c", "Щ")
original_text = original_text.replace("p", "Ф")
original_text = original_text.replace("9", "Г")
original_text = original_text.replace("f", "Ц")
original_text = original_text.replace("d", "Ш")
original_text = original_text.replace("4", "Ж")
original_text = original_text.replace("?", "Ъ")
original_text = original_text.replace("x", "Э")


file_out = open("isb\lab_1\Task 2 Uncyphered text.txt", "w", encoding="utf-8")
file_out.write(original_text)
file_out.close()
