import os

clear = lambda: os.system('clear')

def header(headername):
    clear()
    print('0 - Назад')
    show_yellow_string(headername)

def get_input_value(text):
    return input(f'{text}:')

def show_yellow_string(text):
    print('\x1b[1;33;40m' + '       '+f'{text}'+'\x1b[0m')

def show_red_string(text):
    print('\x1b[1;31;40m' + f'{text}'+'\x1b[0m')

def show_green_string(text):
    print('\x1b[1;32;40m'+f'{text}'+'\x1b[0m')

def menu_view():
    header('Меню')
    print('1 - Поиск по номеру')
    print('2 - Поиск по имени')
    print('3 - Добавить номер')
    print('4 - Просмотреть все контакты')
    print('5 - Экспорт данных')
    print('6 - Импорт данных'+'\n')

def add_view():
     header('Добавление')

def find_view(val):
    clear()
    if val==1: title,desc="номеру","номер телефона"
    elif val==2: title,desc="имени","имя абонента"
    print('0 - Назад')
    show_yellow_string('Поиск по '+f'{title}')
    return get_input_value('Введите '+f'{desc}')

def upload_view():
    header('Экспорт')
    print('1 - Экспорт в json')
    print('2 - Экспорт в xml')

def show_all_view():
    header('Контакты')

def import_view():
    header('Импорт')
    print('1 - Импорт из json')
    print('2 - Импорт из xml')