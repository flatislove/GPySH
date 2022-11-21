import json

# def upload_to_json(data):#employee,department,project
#     new_l=[]
#     for i in data:
#         new_l.append(json.dumps(i.__dict__))
#     try:
#         with open(f"data", 'w', encoding='utf-8') as jsonfile:
#             jsonfile.write('{'+'\n'+'"data":'+'\n'+'['+',\n'.join(new_l)+']'+'\n'+'}')
#     except Exception as ex:
#         print("[INFO] Error while working with upload to Json: ",ex)
#     return 1

    #all data for employee(for export json)

    # SELECT "Employee".firstname, "Employee".lastname, "Department".name,
	# 	"Employee".position, "Employee".number
    # FROM public."Employee"
    # LEFT JOIN "Department"
	#     ON "Department".id="Employee".department_id;

    #all data for projects(for export json)
    # SELECT "Project".name, "Employee".firstname, "Employee".lastname,
	# 	"Employee".position
    # FROM public."Project"
    # LEFT JOIN "Employee"
	#     ON "Employee".id="Project".employee_id;

    #all data for departments(for export json)

    # SELECT "Department".name
    # FROM public."Department"

def export_employee_to_json():
    pass

def export_departments_to_json():
    pass

def export_projects_to_json():
    pass

def import_employee_from_json():#employee,department,project
    pass

def import_departments_from_json():
    pass

def import_projects_from_json():
    pass