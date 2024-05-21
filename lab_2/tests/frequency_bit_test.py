import os
import json
import math

from const import PATH

def frequency_bit_test(seq: str) -> float:
    s = 0
    for bit in seq:
        if bit == "1":
            s += 1
        elif bit == "0":
            s += -1
    sn = s/(math.sqrt(len(seq)))
    sn = abs(sn)
    return math.erfc(sn / math.sqrt(2))



if __name__ == "__main__":

    try:
        with open( PATH, "r", encoding="utf-8") as json_file:
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
        cpp_res = frequency_bit_test(cpp_seq)
        java_res = frequency_bit_test(java_seq)
    except Exception as e:
        print("Ошибка расчёта теста для с++: ", e) 

    try:
        with open(ways[2], "w", encoding="utf-8") as  file_out:
            file_out.write("Результаты Побитового частотного теста: \nДля генератора с++: " + str(cpp_res) + "\nДля джавы: "+ str(java_res))
    except Exception as e:
        print("Ошибка при записи результатов теста", e)