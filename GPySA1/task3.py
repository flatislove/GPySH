from random import randint

#Реализуйте алгоритм перемешивания списка

def shuffle_list(number):
    numbers = [randint(0,100) for i in range(number)]
    print(f'{"":8}Исходный список: {numbers}')
    for index in range(len(numbers)):
        rand_pos=randint(0,number-1)
        if index!=rand_pos: 
            numbers[index],numbers[rand_pos]=numbers[rand_pos],numbers[index]
    print(f'Результат перемешивания: {numbers}')

shuffle_list(int(input('Введите количество чисел в списке:')))