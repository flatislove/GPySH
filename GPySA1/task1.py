#Напишите программу, которая принимает на вход вещественное 
# число и показывает сумму его цифр

def sum_digits(number):
    sum=0
    for i in list(number):
        sum+=int(i) if i.isnumeric() else 0
    print(f"Сумма цифр вещественного числа={sum}")

def sumdigits(number):
    sum=0
    sum+=[lambda x: x.isnumeric() for x in number]
    print(sum)
    
number=input('Введите вещественное число:')
sum_digits(number)
sumdigits(number)
