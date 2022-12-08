#Задайте список из нескольких чисел. Напишите программу, 
#которая найдёт сумму элементов списка с нечетными индексами.

def get_input_number(message):
    inp=0
    while(True):
        try:
            inp=int(input(message))
            if isinstance(inp, int): return inp
        except Exception as ex:
            print(f"[INFO] Ошибка ввода {ex}")

def get_input_int_list():
    count=get_input_number("Введите количество чисел: ")
    numbers=[get_input_number("Введите число: ") for _ in range(count)]
    return numbers

def get_sum_odd_position_list(list):
    sum=0
    for pos,value in enumerate(list):
        sum+=value if pos%2!=0 else 0
    return sum

print(f'Сумма элементов на нечетных позициях: {get_sum_odd_position_list(get_input_int_list())}')