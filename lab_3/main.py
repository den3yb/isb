import argparse
import json
 
from asymetric import *
from simmetric import *
from const import WAY, SIZE

if __name__ == "__main__":

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
        sym_key = create_sym_key()
        asym_key = create_asym_key(SIZE)
        cyph_sym_key = encrypt_sym_key(asym_key, sym_key)
        serialize_private(asym_key, WAY[3])
        serialize_public(asym_key, WAY[2])
        serialize_sym(cyph_sym_key, WAY[1])
    elif args.encryption is not None:
        print('2')
        asym_key = deserylie_asym(WAY[3], WAY[2])
        sym_key = deserialize_sym(WAY[1])
        sym_key = decrypt_sym_key(asym_key, sym_key)
        
    else:
        print('3')