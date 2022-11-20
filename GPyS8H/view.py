import os

clear = lambda: os.system('clear')

def menu_view():
    while(True):
        clear()
        print("    Menu")
        print("1 Add")
        print("2 Get")
        print("3 Export")
        print("4 Import")
        print()
        action=input("Введите действие: ")
        if action in "01234": return action

def add_menu_view():
    while(True):
        clear()
        print("    Add")
        print("1 add employee")
        print("2 add department")
        print("3 add project")
        print()
        action=input("enter action:")
        if action in "0123": return action

def get_menu_view():
    while(True):
        clear()
        print("    Get")
        print("1 get all employees")
        print("2 get all departments")
        print("3 get all projects")
        print()
        action=input("enter action:")
        if action in "0123": return action

def export_menu_view():
    while(True):
        clear()
        print("    Export")
        print("1 export employees")
        print("2 export departments")
        print("3 export projects")
        print()
        action=input("enter action:")
        if action in "0123": return action

def import_menu_view():
    while(True):
        clear()
        print("    Import")
        print("1 import employees")
        print("2 import departments")
        print("3 import projects")
        print()
        action=input("enter action:")
        if action in "0123": return action

def add_employee_view(departments):
    while(True):
        clear()
        fname=input("enter firstname:")
        lname=input("enter lastname:")
        str_dep=""
        for i in departments:
            print(i)
            str_dep+=str(i.id)
        print(str_dep)
        while(True):
            department=input("enter department:")
            if department in str_dep: break
        number=input("enter phone number:")
        position=input("enter position:")
        return fname,lname,int(department),number,position

def add_department_view():
    while(True):
        clear()
        name=input("enter name department:")
        return name

def add_project_view(employess):
    while(True):
        clear()
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
    clear()
    for i in employees:
        print(i)
    print()
    input("press any key: ")

def get_departments_view(departments):
    clear()
    for i in departments:
        print(i)
    print()
    input("press any key: ")

def get_projects_view(projects):
    clear()
    for i in projects:
        print(i)
    print()
    input("press any key: ")

