import os
import json
import math
import mpmath

from const import PATH, P


def frequency_bit_test(seq: str) -> float:
    s = seq.count("1")
    temp = seq.count("0")
    s = s - temp
    sn = s / (math.sqrt(len(seq)))
    sn = abs(sn)
    return math.erfc(sn / math.sqrt(2))


def same_bit_test(seq: str) -> float:
    lenght = len(seq)
    count = seq.count("1")
    s = count / lenght
    if abs(s - 0.5) >= 2 / math.sqrt(lenght):
        return 0
    vn = 0
    for i in range(1, lenght):
        if seq[i - 1] != seq[i]:
            vn += 1
    temp = abs(vn - 2 * lenght * s * (1 - s))
    temp = temp / (2 * math.sqrt(2 * lenght) * s * (1 - s))
    return math.erfc(temp)


def longest_bit_seq(seq: str) -> float:
    length = len(seq)
    v = [0] * 4
    for i in range(0, length, 8):
        maximum = 0
        temp = 0
        for bit in seq[i : (i + 8)]:
            if bit == "1":
                temp += 1
                maximum = max(temp, maximum)
            else:
                temp = 0
        match maximum:
            case _ if maximum <= 1:
                v[0] += 1
            case 2:
                v[1] += 1
            case 3:
                v[2] += 1
            case _:
                v[3] += 1
    x = 0
    for i in range(0, 4):
        x += (v[i] - 16 * P[i]) ** 2 / (16 * P[i])
    return mpmath.gammainc(3 / 2, x / 2)


if __name__ == "__main__":

    try:
        with open(PATH, "r", encoding="utf-8") as json_file:
            ways = json.load(json_file)
    except Exception as e:
        print("Ошибка при открытие файла json: ", e)

    try:
        with open(ways[0], "r", encoding="utf-8") as file_in:
            cpp_seq = file_in.readline()
    except Exception as e:
        print("Ошибка открытия файла с последовательностью с++: ", e)

    try:
        with open(ways[1], "r", encoding="utf-8") as file_in:
            java_seq = file_in.readline()
    except Exception as e:
        print("Ошибка открытия файла с последовательностью java: ", e)

    try:
        cpp_res_freq = frequency_bit_test(cpp_seq)
        java_res_freq = frequency_bit_test(java_seq)
    except Exception as e:
        print("Ошибка расчёта частотного побитового теста: ", e)

    try:
        cpp_res_same = same_bit_test(cpp_seq)
        java_res_same = same_bit_test(java_seq)
    except Exception as e:
        print("Ошибка расчёта теста на одинаковые подряд идущие биты: ", e)

    try:
        cpp_res_long = longest_bit_seq(cpp_seq)
        java_res_long = longest_bit_seq(java_seq)
    except Exception as e:
        print(
            "Ошибка расчёта теста на самую длинную последовательность единиц в блоке: ",
            e,
        )

    try:
        with open(ways[2], "w", encoding="utf-8") as file_out:
            file_out.write("Отчёт по лабараторной работе:")
            file_out.write(
                "\n\nС помощью генератора на с++ была сгенерирована последовательность: "
                + str(cpp_seq)
            )
            file_out.write(
                "\n\nС помощью генератора на Java была сгенерирована последовательность: "
                + str(java_seq)
            )
            file_out.write(
                "\n\nРезультаты Побитового частотного теста: \nДля генератора с++: "
                + str(cpp_res_freq)
                + "\nДля джавы: "
                + str(java_res_freq)
            )
            file_out.write(
                "\n\nРезультаты Теста на одинаковые подряд идущие биты: \nДля генератора с++: "
                + str(cpp_res_same)
                + "\nДля джавы: "
                + str(java_res_same)
            )
            file_out.write(
                "\n\nРезультаты Теста на самую длинную последовательность единиц в блоке: \nДля генератора с++: "
                + str(cpp_res_long)
                + "\nДля джавы: "
                + str(java_res_long)
            )
            file_out.write(
                "\n\nВывод: на основе проведённых тестов обе последовательности можно признать случайными, "
                + "однако с побитовым частотным тестом и тестом\n на самую длинную последовательность в списке с++ справляется "
                + "лучше, хотя и чуть не заваливает тест на подряд идущие биты"
            )
    except Exception as e:
        print("Ошибка при записи результатов тестов", e)
