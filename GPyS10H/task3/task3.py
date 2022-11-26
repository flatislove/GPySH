import company
import person

def send_sms(*objs):
    for obj in objs:
        if obj.get_phone()!=None:
            print(f"Отправлено SMS на номер {obj.get_phone()} c текстом {obj.get_sms_text()}")
        else: print(f"Не удалось отправить сообщение абоненту:{obj.get_name()}")

print("\nСценарий 1\n")
person1=person.Person("Ivan","Ivanovich","Ivanov",{"private":123,"work":456})
person2=person.Person("Ivan","Petrovich","Petrov",{"private":789})
person3=person.Person("Ivan","Petrovich","Sidorov",{"work":789})
person4=person.Person("john","Unknown","Doe",{})
company1 = company.Company("Bell","OOO",{"contact":111},person3,person4)
company2 = company.Company("Cell","AO",{"non_contact":222},person2,person3)
company3 = company.Company("Dell","Ltd",{"non_contact":333},person2,person4)
send_sms(person1,person2,person3,person4,company1,company2,company3)

print("\nСценарий 2\n")
person5=person.Person("Степан","Петрович","Джобсов",{"private":555})
person6=person.Person("Боря","Иванович","Гейтсов",{"private":777,"work":888})
person7=person.Person("Семен","Робертович","Возняцкий",{"work":789})
person8=person.Person("Леонид","Арсенович","Торвальдсон",{})
company4 = company.Company("Яблочный комбинат","OOO",{"contact":111},person5,person7)
company5 = company.Company("ПластОкно","AO",{"non_contact":222},person6)
company6 = company.Company("Пингвинья ферма","Ltd",{"non_contact":333},person8)
send_sms(person5,person6,person7,person8,company4,company5,company6)
