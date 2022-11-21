import json
from config import file_path 
import model.database_operation as db
import model.employee as employee
import model.department as department
import model.project as project

def export_to_json(objects,filename,obj_name):
    data=objects
    ret_list=[]
    for i in data:
        ret_list.append(json.dumps(i.__dict__))
    try:
        with open(f'{file_path}{filename}','w',encoding='utf-8') as jsonfile:
            jsonfile.write('{'+'\n'+f'"{obj_name}":'+'\n'+'['+',\n'.join(ret_list)+']'+'\n'+'}')
    except Exception as ex:
        print("[INFO] Error while working with export to JSON",ex)
        return -1
    return 1

def import_employee_from_json():
    current_employees=db.get_all_employee()
    current_department=db.get_all_departments()
    try:
        with open(f'{file_path}employee.json') as f:
            data = json.load(f)
        for json_obj in data['employees']:
            contain=False
            for emp in current_employees:
                if int(json_obj["id"])==emp.id: 
                    contain=True
                    print(f"[INFO] Employee {emp.firstname} {emp.lastname} already exists")
                    break
            if not contain:
                exist_department=False
                for dep in current_department:
                    if int(json_obj["department"])==dep.id:
                        exist_department=True
                if exist_department:
                    db.add_employee(employee.Employee(json_obj['id'],json_obj['firstname'],json_obj['lastname'],int(json_obj['department']),json_obj['number'],json_obj['position']))
    except EnvironmentError:
        return -1
    return 1

def import_departments_from_json():
    current_department=db.get_all_departments()
    try:
        with open(f'{file_path}department.json') as f:
            data = json.load(f)
        for json_obj in data['departments']:
            contain=False
            for dep in current_department:
                if int(json_obj["id"])==dep.id: 
                    contain=True
                    print(f"[INFO] Department {dep.name} already exists")
                    break
            if not contain:
                db.add_department(department.Department(json_obj['id'],json_obj['name']))
    except EnvironmentError:
        return -1
    return 1

def import_projects_from_json():
    current_employees=db.get_all_employee()
    current_projects=db.get_all_projects()
    try:
        with open(f'{file_path}projects.json') as f:
            data = json.load(f)
        for json_obj in data['projects']:
            contain=False
            for proj in current_projects:
                if int(json_obj["id"])==proj.id: 
                    contain=True
                    print(f"[INFO] Project {proj.name} already exists")
                    break
            if not contain:
                exist_employee=False
                for emp in current_employees:
                    if int(json_obj["employee_id"])==emp.id:
                        exist_employee=True
                if exist_employee:
                    db.add_project(project.Project(json_obj['id'],json_obj['name'],json_obj['employee_id']))
    except EnvironmentError:
        return -1
    return 1