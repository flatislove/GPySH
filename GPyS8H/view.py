import os

clear = lambda: os.system('clear')

def header(headername):
    clear()
    print('0 - Назад')
    show_yellow_string(headername)

def show_yellow_string(text):
    print('\x1b[1;33;40m' + '       '+f'{text}'+'\x1b[0m')

def show_red_string(text):
    print('\x1b[1;31;40m' + f'{text}'+'\x1b[0m')

def show_green_string(text):
    print('\x1b[1;32;40m'+f'{text}'+'\x1b[0m')

def menu_view():
    while(True):
        header("Menu")
        print("1 Add")
        print("2 Get")
        print("3 Get with parameter")
        print("4 Export")
        print("5 Import")
        print()
        action=input("Введите действие: ")
        if action in "012345": return action

def add_menu_view():
    while(True):
        header("Add")
        print("1 add employee")
        print("2 add department")
        print("3 add project")
        print()
        action=input("enter action:")
        if action in "0123": return action

def get_menu_view():
    while(True):
        header("Get")
        print("1 get all employees")
        print("2 get all departments")
        print("3 get all projects")
        print()
        action=input("enter action:")
        if action in "0123": return action

def get_menu_parameter_view():
    while(True):
        header("Get with parameter")
        print("1 get employees by department")
        print("2 get all departments(-)")
        print("3 get all projects(-)")
        print()
        action=input("enter action:")
        if action in "0123": return action

def export_menu_view():
    while(True):
        header("Export")
        print("1 export employees")
        print("2 export departments")
        print("3 export projects")
        print()
        action=input("enter action:")
        if action in "0123": return action

def import_menu_view():
    while(True):
        header("Import")
        print("1 import employees")
        print("2 import departments")
        print("3 import projects")
        print()
        action=input("enter action:")
        if action in "0123": return action

def add_employee_view(departments):
    while(True):
        header("Add employee")
        fname=input("enter firstname:")
        lname=input("enter lastname:")
        str_dep=""
        for i in departments:
            print(i)
            str_dep+=str(i.id)
        print(str_dep)
        while(True):
            department=input("enter department id:")
            if department in str_dep: break
        number=input("enter phone number:")
        position=input("enter position:")
        return fname,lname,int(department),number,position

def add_department_view():
    while(True):
        header("Add department")
        name=input("enter name department:")
        return name

def add_project_view(employess):
    while(True):
        header("Add project")
        name=input("enter project name:")
        str_emp=""
        for i in employess:
            print(i)
            str_emp+=str(i.id)
        while(True):
            employee=input("enter employee id:")
            if employee in str_emp: break
        return name,employee

def get_employee_view(employees):
    header("Employees")
    for i in employees:
        print(i)
    print()
    input("press any key: ")

def get_departments_view(departments):
    header("Departmnets")
    for i in departments:
        print(i)
    print()
    input("press any key: ")

def get_projects_view(projects):
    header("Projects")
    for i in projects:
        print(i)
    print()
    input("press any key: ")

def get_employees_by_department_view(data):
    header("Employee by department")
    str_dep=""
    for i in data:
        print(i)
        str_dep+=str(i.id)
    print()
    while(True):
        dep=input("enter id department:")
        if dep in str_dep: return dep