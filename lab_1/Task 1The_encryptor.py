import re

original_text = "Роман армянской писательницы и художницы Мериам Петросян, 'Дом, в котором...', повествует об доме-интернате для детей инвалидов с более чем столетней историей. Главный герой попал сюда совсем недавно, и с трудом приспосабливается к новому месту. В Доме полно своих тайн и странностей, необычных порядков и традиций, которые необходимо соблюдать. Например, тут не используют имён, всех без исключения, даже преподавателей и директора, зовут по кличкам таких как Сфинкс, Стервятник, Лорд, Слепой, Горбач. Дают их сами воспитанники за отличительные черты, которые, как правило, полностью описывают характер человека или его особенности."

def clean_text (text: str) -> str:
    text=re.sub('[^a-zа-яё]', '', text, flags=re.IGNORECASE)
    text=text.lower()
    return text

def text_to_cyphered (text: str) -> str:
    temp = len (text)
    while (len(text)%8!=0):
        text =text+'а'
    quantity = int(temp/8)
    cyphered =''
    for j in range(0,8):
        for i in range(0,quantity):
            cyphered += text[8*i+j]
    print("Cyphered_text: ",cyphered)
    return cyphered

def test (text: str) -> str:
    cyphered =''
    for j in range(0,63):
        for i in range(0,8):
            cyphered += text[64*i+j]
    print("Unyphered_text: ",cyphered)


cyphered_text = clean_text(original_text)
cyphered_text =text_to_cyphered(cyphered_text)
test(cyphered_text)

