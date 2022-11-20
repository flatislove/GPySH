import view
import model.database_operation as db
import model.department as dep_mod
import model.project as proj
import model.employee as emp
import model.service as service

def menu():
    action=view.menu_view()
    if action=="1":
        menu_add()
    if action=="2":
        menu_get()
    if action=="3":
        menu_export()
    if action=="4":
        menu_import()
    
def menu_add():
    add=view.add_menu_view()
    if add=="1":
        add_employee()
    if add=="2":
        add_department()
    if add=="3":
        add_project()

def menu_get():
    get=view.get_menu_view()
    if get=="1":
        get_all_employees()
    if get=="2":
        get_all_departments()
    if get=="3":
        get_all_projects()

def menu_export():
    exp=view.export_menu_view()
    if exp=="1":
        export_employees()
    if exp=="2":
        export_departments()
    if exp=="3":
        export_projects()

def menu_import():
    imp=view.import_menu_view()
    if imp=="1":
        import_employees()
    if imp=="2":
        import_departments()
    if imp=="3":
        import_projects()

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

def export_employees():
    data=db.get_all_employee()
    service.export()
    pass

def export_departments():
    pass

def export_projects():
    pass

def import_employees():
    pass

def import_departments():
    pass

def import_projects():
    pass