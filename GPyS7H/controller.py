import re
import time
import view
import model

exit_to_menu=lambda x: menu() if x=='0' else 0

def menu():
    while(True):
        view.menu_view()
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
        view.add_view()
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
        number=view.find_view(val)
        model.print_find_results(model.find_by(val,number))
        number=input('->: ')
        exit_to_menu(number)
        find_by(val)

def upload():
    while(True):
        view.upload_view()
        number=input('Выберите пункт: ')
        if(number in '012'):
            if number=='1': model.upload_to_json()
            elif number=='2': model.upload_to_xml()
            menu()
            break

def show_all():
    while(True):
        view.show_all_view()
        model.print_contacts()
        number=input('->: ')
        exit_to_menu(number)
        show_all()
    
def import_data():
    while(True):
        view.import_view()
        number=input('Выберите пункт: ')
        exit_to_menu(number)
        if(number=='1'):
            model.import_from_json()
            menu()
        elif(number=='2'):
            model.import_from_xml()
            menu()
        break