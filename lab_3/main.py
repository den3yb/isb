import argparse
import json
 
from asymetric import *
from symetric import *
from const import WAY, SIZE

if __name__ == "__main__":

    print('start')
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required = True)
    group.add_argument('-gen','--generation',help='Запускает режим генерации ключей')
    group.add_argument('-enc','--encryption',help='Запускает режим шифрования')
    group.add_argument('-dec','--decryption',help='Запускает режим дешифрования')
    args = parser.parse_args()

    try:
        with open (WAY, "r",encoding="utf-8") as file:
            ways =json.load(file)
    except Exception as e:
        print("Возникла ошибка открытия файла с путями")

    if args.generation is not None:
        print('1')
        sym_key = create_sym_key()
        asym_key = create_asym_key(SIZE)
        cyph_sym_key = encrypt_sym_key(asym_key, sym_key)
        serialize_private(asym_key, ways[2])
        serialize_public(asym_key, ways[1])
        serialize_sym(cyph_sym_key, ways[0])
    elif args.encryption is not None:
        print('2')
        asym_key = deserylie_asym(ways[1], ways[2])
        sym_key = deserialize_sym(ways[0])
        sym_key = decrypt_sym_key(asym_key, sym_key)
        try:
            with open (ways[3], "r",encoding="utf-8") as file:
                text = file.read()
        except Exception as e:
            print("Возникла ошибка при чтении файла с текста: ", e)
        enc_text = encrypt_text(text, sym_key)
        try:
            with open (ways[4], "wb") as file:
                file.write(enc_text)
        except Exception as e:
            print("Возникла ошибка при чтении файла с текста: ", e)
    else:
        print('3')
        asym_key = deserylie_asym(ways[1], ways[2])
        sym_key = deserialize_sym(ways[0])
        sym_key = decrypt_sym_key(asym_key, sym_key)
        try:
            with open (ways[4], "rb") as file:
                text = file.read()
        except Exception as e:
            print("Возникла ошибка при чтении файла с текста: ", e)
        text = decode_text(text, sym_key)
        try:
            with open (ways[5], "w", encoding="utf-8") as file:
                file.write(text)
        except Exception as e:
            print("Возникла ошибка записи расшифрованного текста: ", e)


        
        
