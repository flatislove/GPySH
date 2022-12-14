import os
import re


def clear(): return os.system('clear')


def header(headername):
    clear()
    print('0 - Выход')
    show_yellow_string(headername)


def wait_input():
    input("Нажмите любую кнопку: ")


def choiser(var):
    action = input("Введите действие: ")
    if action in var:
        return action


def show_yellow_string(text):
    print('\x1b[1;33;40m' + '       '+f'{text}'+'\x1b[0m')


def menu_view():
    while (True):
        header("Меню")
        print("1 Кнопочный калькулятор")
        print("2 Строчный калькулятор")
        print("3 Отобразить log-файл")
        print()
        return choiser("0123")


def input_number(min, max, action_mess, neg_mess):
    while (True):
        count_step = input(f"{action_mess}: ")
        if count_step.isnumeric() and min <= int(count_step) <= max:
            return count_step
        else:
            print(f"{neg_mess}: ")


def input_line(action_mess, neg_mess, example):
    while (True):
        print(example)
        line = input(f"{action_mess}: ")
        if re.match('^[0-9\*\-\+\/\(\)\s\.]+$', line) != None:
            return line
        else:
            print(f"{neg_mess}")


def input_operation(action_mess, neg_mess):
    while (True):
        operation = input(f"{action_mess}: ")
        if operation in "+-*/":
            return operation
        else:
            print(f"{neg_mess}: ")


def show_example_button_calc(first_number, second_number, operation, result):
    print(f"{first_number}{operation}{second_number}={result}")
    wait_input()


def show_example_line_calc(line, result):
    print(f" Пример: {line}\n Результат: {result}")
    wait_input()


def show_log(log):
    print(*log)
    wait_input()
