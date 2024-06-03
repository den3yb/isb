import argparse
import json

from asymetric import *
from symetric import *
from const import WAY, SIZE


def generation_proc(private_way: str, public_way: str, symm_way: str):
    print("Запуск процедкры генерации и сериализации ключей")
    sym_key = create_sym_key()
    print("Произошло создание симметричного ключа")
    asym_key = create_asym_key()
    print("Произогло создание асимметричного ключа")
    cyph_sym_key = encrypt_sym_key(asym_key, sym_key)
    print("Произошла шифровка симметричного ключа")
    serialize_private(asym_key, private_way)
    print("Произошла сериализация приватного ключа")
    serialize_public(asym_key, public_way)
    print("Произошла сериализация пкбличчного ключа")
    serialize_sym(cyph_sym_key, symm_way)
    print("Произошла сериализация симметричного ключа")


def encryption_proc(
    encr_way: str, orig_way: str, private_way: str, public_way: str, symm_way: str
):
    print("Запуск процедуры шифровки текста")
    asym_key = deserylie_asym(public_way, private_way)
    print("Произошла десериализация асимметричного ключа")
    sym_key = deserialize_sym(symm_way)
    print("Произошла десериализация симметричного ключа")
    sym_key = decrypt_sym_key(asym_key, sym_key)
    print("Произошло дешифрование симметричного ключа")
    try:
        with open(orig_way, "r", encoding="utf-8") as file:
            text = file.read()
        print("Произошло чтение оригинального текста")
    except Exception as e:
        print("Возникла ошибка при чтении файла с текста: ", e)
    enc_text = encrypt_text(text, sym_key)
    print("Произошло шифрование оригинального текста")
    try:
        with open(encr_way, "wb") as file:
            file.write(enc_text)
        print("Произошла запись зашифрованного текста")
    except Exception as e:
        print("Возникла ошибка при чтении файла с текста: ", e)


def decryption_proc(
    uncyph_way: str, encr_way: str, private_way: str, public_way: str, symm_way: str
):
    print("Запуск процедуры дешифровки текста")
    asym_key = deserylie_asym(public_way, private_way)
    print("Произошла десериализация асимметричного ключа")
    sym_key = deserialize_sym(symm_way)
    print("Произошла десериализация симметричного ключа")
    sym_key = decrypt_sym_key(asym_key, sym_key)
    print("Произошло дешифрование симметричного ключа")
    try:
        with open(encr_way, "rb") as file:
            text = file.read()
        print("Произошло чтение зашифрованного текста")
    except Exception as e:
        print("Возникла ошибка при чтении файла с текста: ", e)
    text = decode_text(text, sym_key)
    print("Произошла дешифровка текста")
    try:
        with open(uncyph_way, "w", encoding="utf-8") as file:
            file.write(text)
        print("Произошла запись расшифрованного текста")
    except Exception as e:
        print("Возникла ошибка записи расшифрованного текста: ", e)


if __name__ == "__main__":

    print("start program")
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-gen", "--generation", help="Запускает режим генерации ключей")
    group.add_argument("-enc", "--encryption", help="Запускает режим шифрования")
    group.add_argument("-dec", "--decryption", help="Запускает режим дешифрования")
    args = parser.parse_args()

    try:
        with open(WAY, "r", encoding="utf-8") as file:
            ways = json.load(file)
    except Exception as e:
        print("Возникла ошибка открытия файла с путями")

    match args:
        case args if args.generation:
            generation_proc(ways[2], ways[1], ways[0])
        case args if  args.encryption:
            encryption_proc(ways[4], ways[3], ways[2], ways[1], ways[0])
        case args if args.decryption:
            decryption_proc(ways[5], ways[4], ways[2], ways[1], ways[0])


        
        
