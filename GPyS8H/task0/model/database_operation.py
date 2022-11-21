import psycopg2
from config import host,user,password,db_name
import model.employee as employee
import model.department as department
import model.project as project

def get_from_database(text):
  try:
    connection=psycopg2.connect(
      host=host,
      user=user,
      password=password,
      database=db_name
    )
    connection.autocommit=True
    with connection.cursor() as cursor:
      cursor.execute(text)
      return cursor.fetchall()
  except Exception as ex:
    print("[INFO] Error while working with Postgres",ex)
  finally:
    if connection:
      connection.close()
      # print("[INFO] Postgres connection closed")

def add_to_database(add):
  try:
    connection=psycopg2.connect(
      host=host,
      user=user,
      password=password,
      database=db_name
    )
    connection.autocommit=True
    with connection.cursor() as cursor:
        cursor.execute(add)
        # print("[INFO] Data was successfully inserted")

  except Exception as ex:
    print("[INFO] Error while working with Postgres",ex)
  finally:
    if connection:
      connection.close()

def add_tables():
    sql=        """
        CREATE TABLE IF NOT EXISTS "Department"(
            id serial PRIMARY KEY,
            name varchar(50) NOT NULL
            );

        CREATE TABLE IF NOT EXISTS "Employee"(
            id serial PRIMARY KEY,
            firstname varchar(50) NOT NULL,
            lastname varchar(50) NOT NULL,
            department_id integer NOT NULL,
            number varchar(15),
            position varchar(30),
            FOREIGN KEY (department_id) REFERENCES "Department" (Id)
            ON DELETE CASCADE
            );
        
        CREATE TABLE IF NOT EXISTS "Project"(
            id serial PRIMARY KEY,
            name varchar(50) NOT NULL,
            employee_id integer NOT NULL,
            FOREIGN KEY (employee_id) REFERENCES "Employee" (Id)
            ON DELETE CASCADE
            );"""
    add_to_database(sql)

def add_employee(employee):
    # print(employee)
    add=f"""INSERT INTO "Employee"(firstname,lastname,department_id,number,position)
            VALUES('{employee.firstname}','{employee.lastname}','{int(employee.department)}','{employee.number}','{employee.position}');"""
    add_to_database(add)

def add_department(department):
    add=f"""INSERT INTO "Department"(name) 
            VALUES('{department.name}');"""
    add_to_database(add)

def add_project(project):
    add=f"""INSERT INTO "Project"(name,employee_id)
            VALUES('{project.name}','{project.employee_id}');"""
    add_to_database(add)

def get_all_employee():
    get=get_from_database(""" SELECT id, firstname, lastname, department_id, number,position 
                              FROM "Employee";""")
    employees=[]
    for i in get:
        employees.append(employee.Employee(i[0],i[1],i[2],i[3],i[4],i[5]))
    return employees

def get_all_departments():
    get=get_from_database(""" SELECT id,name 
                              FROM "Department";""")
    departments=[]
    for i in get:
        # print(i)
        departments.append(department.Department(i[0],i[1]))
    return departments

def get_all_projects():
    get=get_from_database(""" SELECT id, name, employee_id 
                              FROM "Project";""")
    projects=[]
    for i in get:
        projects.append(project.Project(i[0],i[1],i[2]))
    return projects

def get_employee_by_department(department):
    get=get_from_database(f""" SELECT "Employee".firstname, "Employee".lastname, "Employee".position
                              FROM public."Employee"
                                LEFT JOIN "Department"
	                                ON "Employee".department_id="Department".id
                              WHERE "Employee".department_id='{department}';""")
    employees=[]
    for i in get:
      employees.append(employee.Employee_By(i[0],i[1],i[2]))
    return employees

def get_employee_by_name(name):
  get=get_from_database(f"""SELECT "Employee".firstname, "Employee".lastname, "Employee".position
                              FROM public."Employee"
                                LEFT JOIN "Department"
	                                ON "Employee".department_id="Department".id
                              WHERE "Employee".firstname LIKE '%{name}%'
                                  OR "Employee".lastname LIKE '%{name}%';""")
  employees=[]
  for i in get:
    employees.append(employee.Employee_By(i[0],i[1],i[2]))
  return employees

def get_employee_by_project(project):
  get=get_from_database(f"""SELECT "Employee".firstname, "Employee".lastname, "Employee".position, "Project".name
                              FROM public."Employee"
                                LEFT JOIN "Project"
	                                ON "Employee".id="Project".employee_id
                              WHERE "Project".id='{project}';""")
  employees=[]
  for i in get:
    employees.append(employee.Employee_By(i[0],i[1],i[2]))
  return employees

def get_employee_by_number(number):
  get=get_from_database(f"""SELECT "Employee".firstname, "Employee".lastname, "Employee".number
                              FROM public."Employee"
                              WHERE "Employee".number LIKE '%{number}%'""")
  employees=[]
  for i in get:
    employees.append(employee.Employee_By(i[0],i[1],i[2]))
  return employees

def delete_employee(id):
  add_to_database(f"""DELETE 
                      FROM "Employee"
                      WHERE "Employee".id = '{int(id)}';""")

def delete_department(id):
  add_to_database(f"""DELETE 
                      FROM "Department"
                      WHERE "Department".id = '{int(id)}';""")

def delete_project(id):
  add_to_database(f"""DELETE 
                      FROM "Project"
                      WHERE "Project".id = '{int(id)}';""")

def add_employees_from_json():
  pass

def add_departments_from_json():
  pass

def add_project_from_json():
  pass
