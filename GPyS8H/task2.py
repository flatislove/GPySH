import task1
import os
#2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv():
#  реализовать корректную работу с числительными, начинающимися с 
# заглавной буквы — результат тоже должен быть с заглавной. 
# Например:num_translate_adv("One") "Один"

def translate_adv(data):
    while(True):
        os.system("clear")
        stat=True
        number=input("enter number: ")
        for i in data:
            if number.lower() == i.en_word.lower():
                print(i.ru_word.capitalize()) if number.capitalize()==number else print(i.ruword)
                stat=False
                break
        if stat: print(f"'{number}' has no translation" )
        action=input("press any key(0 - exit)")
        if action == "0": exit()
        
translate_adv(task1.get_list_words())