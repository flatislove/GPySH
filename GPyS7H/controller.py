import re
import time
import view
import model

exit_to_menu=lambda x: menu() if x=='0' else 0

def menu():
    while(True):
        view.menu_view()
        action=view.get_input_value('Введите действие')
        if action=='0':exit()
        elif action=='1':find_by(1)
        elif action=='2':find_by(2)
        elif action=='3':add()
        elif action=='4':show_all()
        elif action=='5':upload()
        elif action=='6':import_data()

def add():
    re_tel =r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$'
    while(True):
        view.add_view()
        while(True):
            number=view.get_input_value('Введите номер телефона')
            if(number=='0' or re.match(re_tel,number)):break
        exit_to_menu(number)
        firstname=view.get_input_value('Введите имя')
        exit_to_menu(number)
        lastname=view.get_input_value('Введите фамилию')
        exit_to_menu(number)
        description=view.get_input_value('Введите описание')
        exit_to_menu(number)
        con=model.Record(number,firstname,lastname,description)
        r=model.write_file(con)
        if r==-1: view.show_red_string('Ошибка записи в файл')
        else: view.show_green_string('Контакт добавлен')
        time.sleep(0.7)
        add() 

def find_by(val):
    while(True):
        number=view.find_view(val)
        model.print_find_results(model.find_by(val,number))
        number=view.get_input_value('->')
        exit_to_menu(number)
        find_by(val)

def upload():
    while(True):
        view.upload_view()
        number=view.get_input_value('Выберите пункт')
        if(number in '012'):
            if number=='1': 
                jsonr=model.upload_to_json()
                if jsonr==1: view.show_green_string('Создан файл contacts.json')
                elif jsonr==-1: view.show_red_string('Ошибка записи в файл') 
                time.sleep(1.2)
            elif number=='2': 
                xmlr=model.upload_to_xml()
                if xmlr==1: view.show_green_string('Создан файл contacts.xml')
                elif xmlr==-1: view.show_red_string('Ошибка записи в файл')
                time.sleep(1.2)
            menu()

def show_all():
    while(True):
        view.show_all_view()
        model.print_contacts()
        number=view.get_input_value('->')
        exit_to_menu(number)
        show_all()
    
def import_data():
    while(True):
        view.import_view()
        number=view.get_input_value('Выберите пункт')
        exit_to_menu(number)
        if(number=='1'):
            rjson=model.import_from_json()
            if rjson==1: view.show_green_string('Контакты успешно испортированы')
            elif rjson==-1: view.show_red_string('Ошибка импорта')
            time.sleep(1.2)
            menu()
        elif(number=='2'):
            rxml=model.import_from_xml()
            if rxml==1: view.show_green_string('Контакты успешно испортированы')
            elif rxml==-1: view.show_red_string('Ошибка импорта')
            time.sleep(1.2)
            menu()
        break