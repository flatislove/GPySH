from random import randint

# #Написать программу, которая состоит 4 из этапов:
# - создает список из рандомных четырехзначных чисел
# - принимает с консоли цифру и удаляет ее из всех элементов списка
# - цифры каждого элемента суммирует пока результат не станет однозначным числом
# - из финального списка убирает все дублирующиеся элементы
# - после каждого этапа выводить результат в консоль

def get_list_random_numbers(count):
    return [randint(1000,9999) for i in range(count)]

def get_input_number():
    inp=0
    while(True):
        try:
            inp=int(input("Введите цифру: "))
            if (0<inp<10): return inp
        except Exception as ex:
            print(f"[INFO] Ошибка ввода {ex}")
        

def get_list_remove_number(nums,number):
    for index in range(len(nums)):
        if str(number) in str(nums[index]):
            value=""
            for symbs in str(nums[index]):
                if symbs!=str(number): value+=symbs
            nums[index]=int(value) if value.isnumeric() else nums.remove(nums[index])
    return nums

def get_list_sum_elements(nums):
    return [get_sum_digit(number) for number in nums]
        

def get_sum_digit(number):
    result_string=f"{number}"
    while(True):
        result_string+='->'
        sum_numbers=0
        if number>=10:
            digits_for_print=[]
            while(number>0):
                sum_numbers+=number%10
                digits_for_print.append(number%10)
                number//=10
            digits_for_print.reverse()
            result_string+="+".join(map(str, digits_for_print))
            result_string+='->'
            number=sum_numbers
            result_string+=f'{number}'
        else:
            print(result_string[0:-2])
            return number

def get_list_unique(nums):
    return list(set(nums))

def main():
    r_numbers=get_list_random_numbers(10)
    print(f'\n Сформированный список: {r_numbers}')
    digit=get_input_number()
    rem_list=get_list_remove_number(r_numbers,digit)
    print(f'{"":6}Удалена цифра {digit}: {rem_list}')
    print(f'\n{"":10}Результаты расчета:\n')
    sum_list=get_list_sum_elements(rem_list)
    print(f"\n Суммирован до цифры: {sum_list}")
    uniq_list=get_list_unique(sum_list)
    print(f"\n Удалены повторяющиеся: {uniq_list}\n")

main()