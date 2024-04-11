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

file_key = open("isb\lab_1\Task 2 Key.txt", "w", encoding="utf-8")

original_text = original_text.replace("-", " ")
file_key.write("- —  \n")
original_text = original_text.replace("/", "К")
file_key.write("/ — К\n")
original_text = original_text.replace("2", "И")
file_key.write("2 — И\n")
original_text = original_text.replace("n", "С")
file_key.write("n — С\n")
original_text = original_text.replace("8", "В")
file_key.write("8 — В\n")
original_text = original_text.replace("6", "А")
file_key.write("6 — А\n")
original_text = original_text.replace("s", "Ь")
file_key.write("s — Ь\n")
original_text = original_text.replace("5", "Д")
file_key.write("5 — Д\n")
original_text = original_text.replace("e", "О")
file_key.write("e — О\n")
original_text = original_text.replace("r", "П")
file_key.write("r — П\n")
original_text = original_text.replace("3", "3")
file_key.write("3 — 3\n")
original_text = original_text.replace("0", "Е")
file_key.write("0 — Е\n")
original_text = original_text.replace("i", "Т")
file_key.write("i — Т\n")
original_text = original_text.replace("w", "Н")
file_key.write("/ — К\n")
original_text = original_text.replace("m", "Р")
file_key.write("m — Р\n")
original_text = original_text.replace("q", "М")
file_key.write("q — М\n")
original_text = original_text.replace("\\", "Л")
file_key.write("\\ — Л\n")
original_text = original_text.replace(";", "Ы")
file_key.write("; — Ы\n")
original_text = original_text.replace("`", "Я")
file_key.write("` — Я\n")
original_text = original_text.replace("7", "Б")
file_key.write("7 — Б\n")
original_text = original_text.replace("t", "Х")
file_key.write("t — Х\n")
original_text = original_text.replace("1", "Й")
file_key.write("1 — Й\n")
original_text = original_text.replace("k", "Ч")
file_key.write("k — Ч\n")
original_text = original_text.replace("o", "У")
file_key.write("o — У\n")
original_text = original_text.replace("z", "Ю")
file_key.write("z — Ю\n")
original_text = original_text.replace("c", "Щ")
file_key.write("c — Щ\n")
original_text = original_text.replace("p", "Ф")
file_key.write("p — Ф\n")
original_text = original_text.replace("9", "Г")
file_key.write("9 — Г\n")
original_text = original_text.replace("f", "Ц")
file_key.write("f — Ц\n")
original_text = original_text.replace("d", "Ш")
file_key.write("d — Ш\n")
original_text = original_text.replace("4", "Ж")
file_key.write("4 — Ж\n")
original_text = original_text.replace("?", "Ъ")
file_key.write("? — Ъ\n")
original_text = original_text.replace("x", "Э")
file_key.write("x — Э\n")

file_key.close()


file_out = open("isb\lab_1\Task 2 Uncyphered text.txt", "w", encoding="utf-8")
file_out.write(original_text)
file_out.close()
