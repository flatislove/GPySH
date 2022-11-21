import view as view
import model.database_operation as db
import model.department as dep_mod
import model.project as proj
import model.employee as emp
import service

#menu

def menu():
    action=view.menu_view()
    if action=="1":
        menu_add()
    if action=="2":
        menu_get()
    if action=="3":
        menu_get_with_parameter()
    if action=="4":
        menu_delete()
    if action=="5":
        menu_export()
    if action=="6":
        menu_import()
    if action=="0":
        exit()
    else: menu()
    
def menu_add():
    add=view.add_menu_view()
    if add=="1":
        add_employee()
    if add=="2":
        add_department()
    if add=="3":
        add_project()
    if add=="0":
        menu()
    else: menu_add()

def menu_get():
    get=view.get_menu_view()
    if get=="1":
        get_all_employees()
    if get=="2":
        get_all_departments()
    if get=="3":
        get_all_projects()
    if get=="0":
        menu()
    else: menu_get()

def menu_get_with_parameter():
    get=view.get_menu_parameter_view()
    if get=="1":
        get_employees_by_department()
    if get=="2":
        get_employee_by_name()
    if get=="3":
        get_employee_by_project()
    if get=="4":
        get_employee_by_number()
    if get=="0":
        menu()
    else: menu_get_with_parameter()

def menu_delete():
    get=view.delete_menu_view()
    if get=="1":
        delete_employee()
    if get=="2":
        delete_department()
    if get=="3":
        delete_project()
    if get=="0":
        menu()
    else: menu_delete()

def menu_export():
    exp=view.export_menu_view()
    if exp=="1":
        export_employees()
    if exp=="2":
        export_departments()
    if exp=="3":
        export_projects()
    if exp=="0":
        menu()
    else: menu_export()

def menu_import():
    imp=view.import_menu_view()
    if imp=="1":
        import_employees()
    if imp=="2":
        import_departments()
    if imp=="3":
        import_projects()
    if imp=="0":
        menu()
    else: menu_import()

#add

def add_employee():
    departments=db.get_all_departments()
    data=view.add_employee_view(departments)
    employee=emp.Employee(1,data[0],data[1],data[2],data[3],data[4])
    res=db.add_employee(employee)
    view.status_add(res)
    menu_add()

def add_department():
    data=view.add_department_view()
    department=dep_mod.Department(1,data)
    res=db.add_department(department)
    view.status_add(res)
    menu_add()

def add_project():
    data=view.add_project_view(db.get_all_employee())
    project=proj.Project(1,data[0],data[1])
    res=db.add_project(project)
    view.status_add(res)
    menu_add()

#get

def get_all_employees():
    data=db.get_all_employee()
    view.get_employee_view(data)
    menu_get()

def get_all_departments():
    data=db.get_all_departments()
    view.get_departments_view(data)
    menu_get()

def get_all_projects():
    data=db.get_all_projects()
    view.get_projects_view(data)
    menu_get()

def get_employees_by_department():
    data_dep=db.get_all_departments()
    department=view.get_employees_by_department_view(data_dep)
    data=db.get_employee_by_department(department)
    view.get_employee_view(data)
    menu_get_with_parameter()

def get_employee_by_name():
    name=view.get_employees_by_name_view()
    data=db.get_employee_by_name(name)
    if not len(data):
        view.show_red_string("results not found")
        input("press any key: ")
    else: 
        view.get_employee_view(data)
    menu_get_with_parameter()

def get_employee_by_project():
    data_proj=db.get_all_projects()
    project=view.get_employees_by_project_view(data_proj)
    data=db.get_employee_by_project(project)
    view.get_employee_view(data)
    menu_get_with_parameter()

def get_employee_by_number():
    number=view.get_employee_by_number_view()
    data=db.get_employee_by_number(number)
    if not len(data):
        view.show_red_string("Results not found")
        input("Press any key: ")
    else: 
        view.get_employee_view(data)
    menu_get_with_parameter()

#delete

def delete_employee():
    emp_data=db.get_all_employee()
    id=view.delete_employee_view(emp_data) 
    if id!=-1: db.delete_employee(id)    
    menu_delete()

def delete_department():
    dep_data=db.get_all_departments()
    id=view.delete_department_view(dep_data)
    if id!=-1: db.delete_department(id)
    menu_delete()

def delete_project():
    proj_data=db.get_all_projects()
    id=view.delete_employee_view(proj_data)
    if id!=-1: db.delete_employee(id)
    menu_delete()

#export

def export_employees():
    res=service.export_employee_to_json()
    if res==1: view.show_green_string("Data was successfully export to JSON")
    elif res==-1: view.show_red_string("Error while working with export to JSON")
    input("Press any key: ")
    menu_export()

def export_departments():
    res=service.export_departments_to_json()
    if res==1: view.show_green_string("Data was successfully export to JSON")
    elif res==-1: view.show_red_string("Error while working with export to JSON")
    input("Press any key: ")
    menu_export()

def export_projects():
    res=service.export_projects_to_json()
    if res==1: view.show_green_string("Data was successfully export to JSON")
    elif res==-1: view.show_red_string("Error while working with export to JSON")
    input("press any key: ")
    menu_export()

#import

def import_employees():
    res=service.import_employee_from_json()
    if res==1: view.show_green_string("Data was successfully import from JSON or already exists")
    elif res==-1: view.show_red_string("Error while working with import from JSON or the same data exist")
    input("press any key: ")
    menu_import()

def import_departments():
    res=service.import_departments_from_json()
    if res==1: view.show_green_string("Data was successfully import from JSON or already exists")
    elif res==-1: view.show_red_string("Error while working with import from JSON or the same data exist")
    input("press any key: ")
    menu_import()

def import_projects():
    res=service.import_projects_from_json()
    if res==1: view.show_green_string("Data was successfully import from JSON or already exists")
    elif res==-1: view.show_red_string("Error while working with import from JSON or the same data exist")
    input("press any key: ")
    menu_import()