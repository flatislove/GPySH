import math
from random import randint

#Напишите программу, которая принимает на вход вещественное 
# число и показывает сумму его цифр

def sum_digits(number):
    sum=0
    for i in list(number):
        sum+=int(i) if i.isnumeric() else 0
    print(sum)
    
#sum_digits(input('Введите число:'))

#Напишите программу, которая принимает на вход число N и выдает 
# набор произведений чисел от 1 до N.

def multiplication_set(number):
    m_set = []
    m_prev=1
    for i in range(1,number+1):
        m_set.append(m_prev*i)
        m_prev*=i
    print(m_set)

#multiplication_set(int(input('Введите число:')))

#Задайте список из n чисел последовательности $(1+\frac 1 n)^n$
# и выведите на экран их сумму.

def sequence_numbers(number):
    numbers={}
    for i in range(1,number+1):
        numbers.update({i:round(math.pow((1+1/i),i),2)})
    print(numbers,' сумма=',sum(numbers.values()))

#sequence_numbers(int(input('Введите число:')))

#Задайте список из N элементов, заполненных числами из промежутка
#  [-N, N]. Найдите произведение элементов на указанных позициях.
#  Позиции хранятся в файле file.txt в одной строке одно число.

def multiplication_file_position(number):
    positions=[]
    numbers=[]
    with open('GPyS2H/file.txt','r', encoding='utf-8') as f:
        positions = [line.rstrip('\n') for line in f]
    for i in range(number):
        numbers.append(randint(-number,number))
    multipl=1
    for _,pp in enumerate(positions):
        for n,nn in enumerate(numbers):
            if int(pp)==n: multipl*=nn
    print(multipl)

#multiplication_file_position(int(input('Введите количество чисел:')))

#Реализуйте алгоритм перемешивания списка

def shuffle_list(number):
    numbers=[]
    for i in range(number):
        numbers.append(randint(0,100))
    print(numbers)
    for index,value in enumerate(numbers):
        rand_pos=randint(0,number-1)
        if index!=rand_pos:
            tmp=numbers[index]
            numbers[index]=numbers[rand_pos]
            numbers[rand_pos]=tmp
    print(numbers)

#shuffle_list(int(input('Введите количество чисел:')))

#Даны два массива. Нужно вернуть их пересечение

def inner_join(array_one,array_two):
    array_result=[]
    for one_ind,one_val in enumerate(array_one):
        for two_ind,two_val in enumerate(array_two):
            if one_val==two_val:
                array_result.append(array_one[one_ind])
                array_two[two_ind]=None
                break
    print(array_one)
    print(array_two)
    print(array_result)

#array_one=[1, 2, 3, 2, 0]
#array_two=[5, 1, 2, 7, 3, 2]
#inner_join(array_one, array_two)