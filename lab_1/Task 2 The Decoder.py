original_text = "36-w0n/e\s/e-ren\\05w2t-50n`i2\\0i21-im07e86w2`-/-2wpemq6f2ewwe1-703er6nweni2-noc0ni80wwe-23q0w2\\2ns-5e-w6k6\\6-d2me/e9e-2nre\\s3e86w2`-68ieq6i232me86ww;t-n2ni0q-e7m67ei/2-56ww;t-703er6nwenis-2wpemq6f22-5eni296\\6ns-2n/\\zk2i0\\swe-p232k0n/2q2-2-65q2w2nim6i28w;q2-q0m6q2-nre`8\\0w20q-/eqrszi0me8-ni6\\6-ek0825we1-w0e7te52qenis-2nre\\s3e86w2`-68ieq6i2k0n/2t-nm05ni8-36c2i;-p61\\e8-56ww;t-2-rme9m6qqwe1-nm05;n\\05ozc21-xi6r-m6382i2`-68ieq6i2k0n/2t-nm05ni8-36c2i;-n8`36w-n-re`8\\0w20qm6nrm050\\0ww;t-n2ni0q-e7m67ei/2-56ww;t-2-/eqrszi0mw;t-n0i01-8-/eiem;tnm05ni86-n0i08e1-703er6nweni2-2nre\\s3ozin`-8-r0m8oz-ek0m05s-5\\`-36c2i;-r0m056860q;t-re-n0i`q-56ww;t-8-w627e\\00-re\\we1-im6/ie8/0-re5-nm05ni86q2-n0i08e1-703er6nweni2-q;-7o50q-2q0is-8-825o-q0m;-rm05ei8m6c0w2`-w6mod0w21-703er6nweni2-/eiem;0-8e3w2/6zi-rm2-r0m056k0-2wpemq6f22-ren0i`q-6-i6/40-q0m;-re38e\\`zc20-erm050\\`is-kie-i6/20-w6mod0w2`-703er6nweni2-2q0\\2-q0nie?"

def creat_dict(text: str) -> dict:
    long = len(original_text)
    dictionary={}
    for symbol in text:
        if symbol in dictionary:
            dictionary[symbol] +=1/long*100
        else:
            dictionary[symbol] = 1/long*100

    return dictionary

def print_dictionary(dictionary: dict) -> None:
    for key,value in dictionary.items(): print(key, ':', value)


dictionary_chastot = creat_dict(original_text)
print_dictionary(dictionary_chastot)

print(original_text)
