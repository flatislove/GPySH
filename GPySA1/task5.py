#Написать программу, которая будет ввыводит в консоль заданный текст 
# (Python - один из самых популярных языков программирования в мире), 
# затем принимать из консоли шаблон подстроки и удалять в задданом 
# тексте все слова в которых присутствует введенный шаблон
# Пример:
# Python - один из самых популярных языков программирования в мире
# Введите подстроку: ам
# Python - один из популярных языков в мире

text="Python - один из самых популярных языков программирования в мире"

def remove_words_by_substring(text,substring):
    words=text.split()
    for _,value in enumerate(words):
        if substring in value: words.remove(value)
    return " ".join(map(str, words))

def get_input_string():
    while(True):
        substring=input("Введите подстроку: ")
        if len(substring)>0:return substring
        else: print("Некорректный ввод")

print(remove_words_by_substring(text,get_input_string()))