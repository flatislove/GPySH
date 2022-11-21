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
        menu_export()
    if action=="5":
        menu_import()
    if action=="0":
        exit()
    
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

#add

def add_employee():
    departments=db.get_all_departments()
    data=view.add_employee_view(departments)
    employee=emp.Employee(1,data[0],data[1],data[2],data[3],data[4])
    db.add_employee(employee)
    menu_add()

def add_department():
    data=view.add_department_view()
    department=dep_mod.Department(1,data)
    db.add_department(department)
    menu_add()

def add_project():
    data=view.add_project_view(db.get_all_employee())
    project=proj.Project(1,data[0],data[1])
    db.add_project(project)
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

def get_employee_by_name():
    name=view.get_employees_by_name_view()
    data=db.get_employee_by_name(name)
    if len(data)==0:
        view.show_red_string("Результаты не найдены")
        input("press any key: ")
    else: 
        view.get_employee_view(data)
    menu_get_with_parameter()


def get_employee_by_project():
    pass

def get_employee_by_number():
    pass

#export

def export_employees():
    pass

def export_departments():
    pass

def export_projects():
    pass

#import

def import_employees():
    pass

def import_departments():
    pass

def import_projects():
    pass