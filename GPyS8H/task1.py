import os
#Написать функцию num_translate(), переводящую числительные 
# от 0 до 10 c английского на русский язык. Например:
#num_translate("one") "один"

class Dictionary:
    def __init__(self,en_word,ru_word):
        self.en_word=en_word
        self.ru_word=ru_word

def get_list_words():
    dictionary=[]
    dictionary.append(Dictionary("one","один"))
    dictionary.append(Dictionary("two","два"))
    dictionary.append(Dictionary("three","три"))
    dictionary.append(Dictionary("four","четыре"))
    dictionary.append(Dictionary("five","пять"))
    dictionary.append(Dictionary("six","шесть"))
    dictionary.append(Dictionary("seven","семь"))
    dictionary.append(Dictionary("eight","восемь"))
    dictionary.append(Dictionary("nine","девять"))
    dictionary.append(Dictionary("ten","десять"))
    return dictionary

def translate(data):
    while(True):
        os.system("clear")
        stat=True
        number=input("enter number: ")
        for i in data:
            if number in i.en_word:
                print(i.ru_word)
                stat=False
                break
        if stat: print(f"'{number}' has no translation" )
        action=input("press any key(0 - exit)")
        if action == "0": exit()
        
translate(get_list_words())