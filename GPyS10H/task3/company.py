import person

class Company:
    name:str
    type_company:str
    phones:dict
    persons:person.Person

    def __init__(self,name,type_company,phones,*persons):
        self.name=name
        self.type_company=type_company
        self.phones=phones
        self.persons=persons

    def get_persons(self):
        return self.persons

    def get_phone(self):
        phone=self.phones.get("contact")
        if phone!=None: return phone
        else:
            for employee in self.get_persons():
                if employee.contacts.get("work"):return employee.contacts.get("work")

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type_company

    def get_sms_text(self):
        return f"Для компании {self.get_name()} есть супер предложение! Примите участие в нашем беспроигрышном конкурсе для {self.get_type()}."