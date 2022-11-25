from math import pow

#Задайте список из n чисел последовательности $(1+\frac 1 n)^n$
# и выведите на экран их сумму.

def sequence_numbers(number):
    numbers={}
    for i in range(1,number+1):
        numbers.update({i:round(pow((1+1/i),i),2)})
    print(f'{numbers}\nCумма последовательности (1+1\u2044n)\u207F= {sum(numbers.values())}')

sequence_numbers(int(input('Введите число:')))