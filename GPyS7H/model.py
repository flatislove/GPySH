import csv
import model
import json
import time
import xml.etree.ElementTree as et

class Record:
    def __init__(self,number,firstname,lastname,description):
        self.number=number
        self.firstname=firstname
        self.lastname=lastname
        self.description=description

    def __str__(self):
        return f"{self.number:15} {self.firstname:10} {self.lastname:10} {self.description}"

def get_all_contacts():
    res=[]
    try:
        with open('GPyS7H/contacts.csv') as csvfile:
            reader = csv.reader(csvfile, quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                contact=model.Record(row[0],row[1],row[2],row[3])
                res.append(contact)
    except EnvironmentError:
        print('\x1b[1;31;40m' + 'Ошибка чтения файла' + '\x1b[0m')
    return res

def write_file(contact):
    try:
        with open('GPyS7H/contacts.csv', 'a', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
            writer.writerow([contact.number, contact.firstname, contact.lastname, contact.description])
    except EnvironmentError:
        print('\x1b[1;31;40m' + 'Ошибка записи в файл' + '\x1b[0m')

def find_by(var,fstr):
    contacts=get_all_contacts()
    res=[]
    for contact in contacts:
        if ((var==1 and fstr in contact.number) or (var==2 and fstr in (contact.firstname or contact.lastname))):
            res.append(model.Record(contact.number,contact.firstname,contact.lastname,contact.description))
    return res

def upload_to_json():
    contacts=get_all_contacts()
    new_l=[]
    for i in contacts:
        new_l.append(json.dumps(i.__dict__))
    try:
        with open('GPyS7H/contacts.json', 'w', encoding='utf-8') as jsonfile:
            jsonfile.write('{'+'\n'+'"contacts":'+'\n'+'['+',\n'.join(new_l)+']'+'\n'+'}')
    except EnvironmentError:
        print('\x1b[1;31;40m' + 'Ошибка записи в файл' + '\x1b[0m')
    print('\x1b[1;32;40m' + 'Создан файл contacts.json' + '\x1b[0m')
    time.sleep(1.2)
    
def upload_to_xml():
    contacts_arr=get_all_contacts()
    root = et.Element("contacts")
    for cont_one in contacts_arr:
        contacts = et.SubElement(root,"contact")
        cnt = et.SubElement(contacts,"number")
        cnt.text = str(cont_one.number)
        cnt = et.SubElement(contacts,"firstname")
        cnt.text = str(cont_one.firstname)
        cnt = et.SubElement(contacts,"lastname")
        cnt.text = str(cont_one.lastname)
        cnt = et.SubElement(contacts,"description")
        cnt.text = str(cont_one.description)
    tree = et.ElementTree(root)
    tree.write("GPyS7H/contacts.xml",encoding='utf-8', xml_declaration=True)
    print('\x1b[1;32;40m' + 'Создан файл contacts.xml' + '\x1b[0m')
    time.sleep(1.2)

def print_contacts():
    contacts=get_all_contacts()
    for contact in contacts:
        print(contact)

def print_find_results(contacts):
    if len(contacts)>0:
        for row in contacts:
            print(row)
    else: print('Ничего не найдено')

def import_from_json():
    with open('GPyS7H/contacts.json') as f:
        data = json.load(f)
    for i in data['contacts']:
        write_file(model.Record(i['number'],i['firstname'],i['lastname'],i['description']))
    print('\x1b[1;32;40m' + 'Контакты успешно испортированы' + '\x1b[0m')
    time.sleep(1.2)

def import_from_xml():
    tree = et.parse('GPyS7H/contacts.xml')
    root = tree.getroot()
    for contact in root.findall('contact'):
        number = contact.find('number').text
        firstname = contact.find('firstname').text
        lastname = contact.find('lastname').text
        description = contact.find('description').text
        write_file(model.Record(number,firstname,lastname,description))
    print('\x1b[1;32;40m' + 'Контакты успешно испортированы' + '\x1b[0m')
    time.sleep(1.2)