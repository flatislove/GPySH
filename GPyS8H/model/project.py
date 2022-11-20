class Project:
    def __init__(self,id,name,employee_id):
        self.id=id
        self.name=name
        self.employee_id=employee_id

    def __str__(self):
        return f"Id:{self.id} Name:{self.name} Employee:{self.employee_id}"