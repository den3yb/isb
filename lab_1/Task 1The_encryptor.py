import re


def clean_text(text: str) -> str:
    """Удаляет все символы кроме букв у входного текста, даже пробелы, делает все буквы маленькими"""
    text = re.sub("[^a-zа-яё]", "", text, flags=re.IGNORECASE)
    text = text.lower()
    return text


def text_to_cyphered(text: str) -> str:
    """Шифрует входной текст, врзвращает зафифрованный"""
    temp = len(text)
    while len(text) % 8 != 0:
        text = text + "а"
    quantity = int(temp / 8)
    cyphered = ""
    for j in range(0, 8):
        for i in range(0, quantity):
            cyphered += text[8 * i + j]
    print("Cyphered_text: ", cyphered)
    return cyphered


def test(text: str) -> str:
    """Осуществляет проверку-дешифровку данного конкретного текста, с учётом знания параметров таблицы"""
    cyphered = ""
    for j in range(0, 63):
        for i in range(0, 8):
            cyphered += text[64 * i + j]
    print("Unyphered_text: ", cyphered)


file_in = open("isb\lab_1\Task 1 Original text.txt", "r", encoding="utf-8")
original_text = file_in.readline()
file_in.close()

cyphered_text = clean_text(original_text)
cyphered_text = text_to_cyphered(cyphered_text)

file_out = open("isb\lab_1\Task 1 Cyphered text.txt", "w", encoding="utf-8")
file_out.write(cyphered_text)
file_out.close()


