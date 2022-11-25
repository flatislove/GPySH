#Напишите программу, которая принимает на вход вещественное 
# число и показывает сумму его цифр

def sum_digits(number):
    sum=0
    for i in list(number):
        sum+=int(i) if i.isnumeric() else 0
    print(f"Сумма цифр вещественного числа={sum}")
    
sum_digits(input('Введите вещественное число:'))