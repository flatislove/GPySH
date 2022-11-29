import math
import random as r
#Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов.

def get_input_float_list():
    numbers=[]
    for _ in range(r.randint(2,10)):
        numbers.append(float(str(r.randint(0,20))+'.'+str(r.randint(0,999))))
    return numbers

def get_fractional_min_max_difference(numbers):
    list_fract=[]
    for i in numbers:
        if i%1!=0: list_fract.append(i%1)
    return round(math.fabs(max(list_fract)-min(list_fract)),5)

def main():
    random_list=get_input_float_list()
    print(f'Сформированный список:\n{random_list}')
    print(f'Разница max и min дробных частей: {get_fractional_min_max_difference(random_list)}')

main()