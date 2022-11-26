class Person:
    lastname:str
    firstname:str
    middlename:str
    contacts:dict
    
    def __init__(self,firstname,middlename,lastname,contacts):
        self.lastname=lastname
        self.firstname=firstname
        self.middlename=middlename
        self.contacts=contacts

    def get_phone(self):
        return self.contacts.get("private") 

    def get_name(self):
        return f"{self.lastname} {self.firstname} {self.middlename}" 

    def get_first_and_middle_name(self):
        return f"{self.firstname} {self.middlename}"

    def get_work_phone(self):
        return self.contacts.get("work")

    def get_sms_text(self):
        return f"Уважаемый {self.get_first_and_middle_name()}! Примите участие в беспроигрышном конкурсе для физических лиц."