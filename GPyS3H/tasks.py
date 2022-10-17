import math
#Задайте список из нескольких чисел. Напишите программу, которая
#  найдёт сумму элементов списка, стоящих на нечётной позиции.

def get_input_int_list():
    numbers=[]
    count=int(input('Введите количество чисел: '))
    for _ in range(count):
        numbers.append(int(input('Введите число: ')))
    return numbers

def get_sum_odd_position_list(list):
    sum=0
    for pos,value in enumerate(list):
        sum+=value if pos%2!=0 else 0
    return sum

#print(get_sum_odd_position_list(get_input_int_list()))

#Напишите программу, которая найдёт произведение пар чисел 
# списка. Парой считаем первый и последний элемент, второй 
# и предпоследний и т.д.

def get_list_sum_pair_numbers(numbers):
    sum_pair=[]
    for pos in range(0,int((len(numbers)+1)/2)):
        sum_pair.append(numbers[pos]*numbers[-pos-1])
    return sum_pair

#print(get_list_sum_pair_numbers(get_input_int_list()))

#Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов.

def get_input_float_list():
    numbers=[]
    count=int(input('Введите количество чисел: '))
    for _ in range(count):
        numbers.append(float(input('Введите число: ')))
    return numbers

def get_fractional_min_max_difference(numbers):
    list_fract=[]
    for i in numbers:
        if i%1!=0: list_fract.append(i%1)
    return round(math.fabs(max(list_fract)-min(list_fract)),2)

#print(get_fractional_min_max_difference(get_input_float_list()))

#Напишите программу, которая будет преобразовывать десятичное 
# число в двоичное.

def get_binary_from_int(number):
    binary=[]
    while(number>0):
        binary.append(number%2)
        number//=2
    binary.reverse()
    return ''.join(map(str,binary))

#print(get_binary_from_int(int(input('Введите число: '))))

#Задайте число. Составьте список чисел Фибоначчи, в том 
# числе для отрицательных индексов

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

#print(get_negafibonacci_list(int(input('Введите число: '))))