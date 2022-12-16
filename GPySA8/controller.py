import re
import time
import view
import model


re_tel = r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$'


def exit_to_menu(x): return menu() if x == '0' else 0


def menu():
    while (True):
        view.menu_view()
        action = view.get_input_value('Введите действие')
        match(action):
            case '0': exit()
            case '1': find_contacts_by(1)
            case '2': find_contacts_by(2)
            case '3': add_contact()
            case '4': edit_contact()
            case '5': remove_contact()
            case '6': show_all()
            case '7': upload()
            case '8': import_data()


def find_contacts_by(val):
    while (True):
        number = view.find_view(val)
        model.print_find_results(model.find_by(val, number))
        number = view.get_input_value('->')
        exit_to_menu(number)
        find_contacts_by(val)


def add_contact():

    while (True):
        view.add_view()
        while (True):
            number = view.get_input_value('Введите номер телефона')
            if (number == '0' or re.match(re_tel, number)):
                break
            else:
                view.show_red_string("Такого номера не существует")
        exit_to_menu(number)
        firstname = view.get_input_value('Введите имя')
        exit_to_menu(number)
        lastname = view.get_input_value('Введите фамилию')
        exit_to_menu(number)
        description = view.get_input_value('Введите описание')
        exit_to_menu(number)
        con = model.Record("0", number, firstname, lastname, description)
        r = model.add_contact(con)
        if r == -1:
            view.show_red_string('Ошибка записи в файл')
        else:
            view.show_green_string('Контакт добавлен')
        time.sleep(0.7)
        add_contact()


def edit_contact():
    while (True):
        view.header("Редактирование")
        view.show_all_view()
        model.print_contacts()
        id = view.get_input_value("Введите ID записи для редактирования")
        if id == '0':
            menu()
        r = model.get_contact_for_edit(id)
        if r == -1:
            view.show_red_string('ID не найден')
        else:
            view.print_contact(r)
            view.show_yellow_string(
                "Если поле не нужно изменять - нажмите Enter")
            number = ''
            while (True):
                inp_number = view.get_input_value('Введите номер телефона')
                if (inp_number == '0' or inp_number == "" or re.match(re_tel, inp_number)):
                    number = inp_number
                    break
                else:
                    view.show_red_string("Такого номера не существует")
            if number == '':
                number = r.number
            fname = view.get_input_value("Введите имя: ")
            if fname == "":
                fname = r.firstname
            lname = view.get_input_value("Введите фамилию: ")
            if lname == "":
                lname = r.lastname
            desc = view.get_input_value("Введите описание: ")
            if desc == "":
                desc = r.description
            model.edit_contact(model.Record(r.id, number, fname, lname, desc))
            view.show_green_string('Контакт отредактирован')
        time.sleep(0.7)
        edit_contact()


def remove_contact():
    while (True):
        view.show_all_view()
        model.print_contacts()
        id = view.get_input_value("Введите ID контакта для удаления")
        if id == '0':
            menu()
        r = model.remove_contact(id)
        if r == -1:
            view.show_red_string('ID не найден')
        else:
            view.show_green_string('Контакт удален')
        time.sleep(0.7)
        remove_contact()


def show_all():
    while (True):
        view.show_all_view()
        model.print_contacts()
        number = view.get_input_value('->')
        exit_to_menu(number)
        show_all()


def upload():
    while (True):
        view.upload_view()
        number = view.get_input_value('Выберите пункт')
        if (number in '012'):
            if number == '1':
                jsonr = model.upload_to_json()
                if jsonr == 1:
                    view.show_green_string('Создан файл contacts.json')
                elif jsonr == -1:
                    view.show_red_string('Ошибка записи в файл')
                time.sleep(1.2)
            elif number == '2':
                xmlr = model.upload_to_xml()
                if xmlr == 1:
                    view.show_green_string('Создан файл contacts.xml')
                elif xmlr == -1:
                    view.show_red_string('Ошибка записи в файл')
                time.sleep(1.2)
            menu()


def import_data():
    while (True):
        view.import_view()
        number = view.get_input_value('Выберите пункт')
        exit_to_menu(number)
        if (number == '1'):
            rjson = model.import_from_json()
            if rjson == 1:
                view.show_green_string('Контакты успешно испортированы')
            elif rjson == -1:
                view.show_red_string('Ошибка импорта')
            time.sleep(1.2)
            menu()
        elif (number == '2'):
            rxml = model.import_from_xml()
            if rxml == 1:
                view.show_yellow_string(
                    "Если номера нет в вашей книге, он будет добавлен")
                view.show_green_string('Контакты успешно испортированы')
            elif rxml == -1:
                view.show_red_string('Ошибка импорта')
            time.sleep(1.2)
            menu()
        break
