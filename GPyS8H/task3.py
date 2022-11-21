#3. Написать функцию thesaurus(), принимающую в качестве аргументов имена 
# сотрудников и возвращающую словарь, в котором ключи — первые буквы имён,
#  а значения — списки, содержащие имена, начинающиеся с соответствующей 
# буквы. Например:thesaurus("Иван", "Мария", "Петр", "Илья")
# {"И": ["Иван", "Илья"],
# "М": ["Мария"], "П": ["Петр"]}

employees=["Иван", "Мария", "Петр", "Илья"]

def thesaurus(data):
    dictionary={}
    letter_set=set()
    [letter_set.add(i[0]) for i in data]
    names=[]
    for i in letter_set:
        names=[]
        for j in data:
            if j[0]==i:
                names.append(j)
        dictionary.update({i:names})
    return dictionary

# print(thesaurus(employees))