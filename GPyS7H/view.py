import os
import re
import time
import controller
import model

clear = lambda: os.system('clear')
exit_to_menu=lambda x: menu() if x=='0' else 0

def menu():
    while(True):
        header('Меню')
        print('1 - Поиск по номеру')
        print('2 - Поиск по имени')
        print('3 - Добавить номер')
        print('4 - Просмотреть все контакты')
        print('5 - Экспорт данных')
        print('6 - Импорт данных'+'\n')
        a=input('Введите действие:')
        if a=='0':exit()
        elif a=='1':find_by(1)
        elif a=='2':find_by(2)
        elif a=='3':add()
        elif a=='4':show_all()
        elif a=='5':upload()
        elif a=='6':import_data()

def add():
    re_tel =r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$'
    while(True):
        header('Добавление')
        while(True):
            number=input('Введите номер телефона: ')
            if(number=='0' or re.match(re_tel,number)):break
        exit_to_menu(number)
        firstname=input('Введите имя: ')
        exit_to_menu(number)
        lastname=input('Введите фамилию: ')
        exit_to_menu(number)
        description=input('Введите описание: ')
        exit_to_menu(number)
        con=model.Record(number,firstname,lastname,description)
        model.write_file(con)
        print('\x1b[1;32;40m' + 'Добавлено!' + '\x1b[0m')
        time.sleep(0.7)
        add() 

def find_by(val):
    while(True):
        clear()
        if val==1: title,desc="номеру","номер телефона"
        elif val==2: title,desc="имени","имя абонента"
        print('0 - Назад')
        print('\x1b[0;33;40m' + '       Поиск по '+f'{title}'+'\x1b[0m')
        number=input('Введите '+f'{desc}'+': ')
        model.print_find_results(model.find_by(val,number))
        number=input('->: ')
        exit_to_menu(number)
        find_by(val)

def upload():
    while(True):
        header('Экспорт')
        print('1 - Экспорт в json')
        print('2 - Экспорт в xml')
        number=input('Выберите пункт: ')
        if(number in '012'):
            if number=='1': model.upload_to_json()
            elif number=='2': model.upload_to_xml()
            menu()
            break

def show_all():
    while(True):
        header('Контакты')
        model.print_contacts()
        number=input('->: ')
        exit_to_menu(number)
        show_all()
    
def import_data():
    while(True):
        header('Импорт')
        print('1 - Импорт из json')
        print('2 - Импорт из xml')
        number=input('Выберите пункт: ')
        exit_to_menu(number)
        if(number=='1'):
            model.import_from_json()
            menu()
        elif(number=='2'):
            model.import_from_xml()
            menu()
        break

def header(headername):
        clear()
        print('0 - Назад')
        print('\x1b[0;33;40m' + '       '+f'{headername}'+'\x1b[0m')