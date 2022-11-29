#Задайте число. Составьте список чисел Фибоначчи, в том 
# числе для отрицательных индексов

def get_input_number(message):
    inp=0
    while(True):
        try:
            inp=int(input(message))
            if isinstance(inp, int): return inp
        except Exception as ex:
            print(f"[INFO] Ошибка ввода {ex}")

def get_negafibonacci_list(number):
    list_numbers=[0]
    prev_value, curr_value = 0, 1
    list_numbers.append(curr_value)
    list_numbers.insert(0,curr_value)
    for f in range(number-1):
        i=int(curr_value+prev_value)
        list_numbers.append(i)
        list_numbers.insert(0,-i if f%2==0 else i) 
        prev_value, curr_value=curr_value,i
    return list_numbers

print(get_negafibonacci_list(get_input_number('Введите число: ')))