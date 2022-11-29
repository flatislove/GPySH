#Напишите программу, которая найдёт произведение пар чисел 
# списка. Парой считаем первый и последний элемент, второй 
# и предпоследний и т.д.

def get_input_number(message):
    inp=0
    while(True):
        try:
            inp=int(input(message))
            if isinstance(inp, int): return inp
        except Exception as ex:
            print(f"[INFO] Ошибка ввода {ex}")

def get_input_int_list():
    numbers=[]
    count=get_input_number("Введите количество чисел: ")
    for _ in range(count):
        numbers.append(get_input_number("Введите число: "))
    return numbers

def get_list_sum_pair_numbers(numbers):
    sum_pair=[]
    for pos in range(0,int((len(numbers)+1)/2)):
        sum_pair.append(numbers[pos]*numbers[-pos-1])
    return sum_pair

print(f'Произведение пар элементов: {get_list_sum_pair_numbers(get_input_int_list())}')