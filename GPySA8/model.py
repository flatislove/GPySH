import csv
import json
import xml.etree.ElementTree as et


class Record:
    def __init__(self, id, number, firstname, lastname, description):
        self.id = id
        self.number = number
        self.firstname = firstname
        self.lastname = lastname
        self.description = description

    def __str__(self):
        return f"{self.id:4} {self.number:15} {self.firstname:10} {self.lastname:10} {self.description}"


def get_all_contacts():
    res = []
    try:
        with open('GPySA8/contacts.csv') as csvfile:
            reader = csv.reader(csvfile, quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                contact = Record(row[0], row[1], row[2], row[3], row[4])
                res.append(contact)
    except EnvironmentError:
        print('\x1b[1;31;40m' + 'Ошибка чтения файла' + '\x1b[0m')
    return res


def write_file(contact):
    try:
        with open('GPySA8/contacts.csv', 'a', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
            writer.writerow([contact.id, contact.number, contact.firstname,
                            contact.lastname, contact.description])
    except EnvironmentError:
        return -1


def clear_file():
    try:
        with open('GPySA8/contacts.csv', 'r+', encoding='utf-8') as csvfile:
            csvfile.truncate()
    except EnvironmentError:
        return -1


def find_by(var, fstr):
    contacts = get_all_contacts()
    res = []
    for contact in contacts:
        if ((var == 1 and fstr in contact.number) or (var == 2 and fstr in (contact.firstname or contact.lastname))):
            res.append(Record(contact.id, contact.number,
                       contact.firstname, contact.lastname, contact.description))
    return res


def upload_to_json():
    contacts = get_all_contacts()
    new_l = []
    for i in contacts:
        new_l.append(json.dumps(i.__dict__))
    try:
        with open('GPySA8/contacts.json', 'w', encoding='utf-8') as jsonfile:
            jsonfile.write('{'+'\n'+'"contacts":'+'\n' +
                           '['+',\n'.join(new_l)+']'+'\n'+'}')
    except EnvironmentError:
        return -1
    return 1


def upload_to_xml():
    try:
        contacts_arr = get_all_contacts()
        root = et.Element("contacts")
        for cont_one in contacts_arr:
            contacts = et.SubElement(root, "contact")
            cnt = et.SubElement(contacts, "id")
            cnt.text = str(cont_one.id)
            cnt = et.SubElement(contacts, "number")
            cnt.text = str(cont_one.number)
            cnt = et.SubElement(contacts, "firstname")
            cnt.text = str(cont_one.firstname)
            cnt = et.SubElement(contacts, "lastname")
            cnt.text = str(cont_one.lastname)
            cnt = et.SubElement(contacts, "description")
            cnt.text = str(cont_one.description)
        tree = et.ElementTree(root)
        tree.write("GPySA8/contacts.xml",
                   encoding='utf-8', xml_declaration=True)
    except EnvironmentError:
        return -1
    return 1


def print_contacts():
    contacts = get_all_contacts()
    for contact in contacts:
        print(contact)


def print_find_results(contacts):
    if len(contacts) > 0:
        for row in contacts:
            print(row)
    else:
        print('Ничего не найдено')


def import_from_json():
    contacts = get_all_contacts()
    contacts_from_json = []
    try:
        with open('GPySA8/contacts.json') as f:
            data = json.load(f)
        for i in data['contacts']:
            contacts_from_json.append(Record(i['id'], i['number'],
                                             i['firstname'], i['lastname'], i['description']))
        for contact_json in contacts_from_json:
            isExist = False
            for contact in contacts:
                if contact_json.number == contact.number:
                    isExist = True
            if isExist == False:
                contact_json.id = get_next_id()
                add_contact(contact_json)
    except EnvironmentError:
        return -1
    return 1


def import_from_xml():
    contacts = get_all_contacts()
    try:
        tree = et.parse('GPySA8/contacts.xml')
        root = tree.getroot()
        for contact in root.findall('contact'):
            id = contact.find('id').text
            number = contact.find('number').text
            firstname = contact.find('firstname').text
            lastname = contact.find('lastname').text
            description = contact.find('description').text
            for current_contact in contacts:
                isExist = False
                if number == current_contact.number:
                    isExist = True
                    break
            if isExist == False:
                add_contact(Record(get_next_id(), number,
                            firstname, lastname, description))
    except EnvironmentError:
        return -1
    return 1


def add_contact(contact):
    if contact.id == '0':
        contact.id = get_next_id()
    write_file(contact)


def get_next_id():
    contacts = get_all_contacts()
    max = contacts[0].id
    for contact in contacts:
        if int(contact.id) > int(max):
            max = contact.id
    return int(max)+1


def get_contact_for_edit(id):
    contacts = get_all_contacts()
    for contact in contacts:
        if (contact.id == id):
            return contact
    else:
        return -1


def edit_contact(contact):
    if contact == -1:
        return -1
    else:
        remove_contact(contact.id)
        add_contact(contact)


def remove_contact(id):
    contacts = get_all_contacts()
    result = []
    indicator = False
    for contact in contacts:
        if contact.id != id:
            result.append(contact)
        else:
            indicator = True
    clear_file()
    for c in result:
        write_file(c)
    return -1 if indicator == False else 1
