#4. * (вместо задачи 3) Написать функцию thesaurus_adv(),
#  принимающую в качестве аргументов строки в формате 
# «Имя Фамилия» и возвращающую словарь, в котором ключи — первые
#  буквы фамилий, а значения — словари, реализованные по схеме
#  предыдущего задания и содержащие записи, в которых фамилия
#  начинается с соответствующей буквы. 
# Например:thesaurus_adv("Иван Сергеев", "Инна Серова", 
# "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {"А": {"П": ["Петр Алексеев"]},
# "И": {"И": ["Илья Иванов"]},
# "С": {"И": ["Иван Сергеев", "Инна Серова"],"А": ["Анна Савельева"]}}
# Как поступить, если потребуется сортировка по ключам?

employees=["Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"]

def thesaurus_adv(data):

    letter_firstname_set,letter_lastname_set=set(),set()
    for i in data:
        flnames=i.split(" ")
        letter_firstname_set.add(flnames[0][0])
        letter_lastname_set.add(flnames[1][0])
    dictionary_last={}
    for last in letter_lastname_set:
        dictionary_first={}
        for first in letter_firstname_set:
            by_names=[]
            for names in data:
                pair_name=names.split(" ")
                if first==pair_name[0][0] and last==pair_name[1][0]:
                    by_names.append(names)
            if len(by_names): dictionary_first.update({first:by_names})
        dictionary_last.update({last: dict(sorted(dictionary_first.items()))})
    print(dict(sorted(dictionary_last.items())))
            
thesaurus_adv(employees)