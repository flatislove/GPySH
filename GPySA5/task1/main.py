#Создайте программу для игры с конфетами человек против компьютера.
#Условие задачи: На столе лежит 150 конфет. Играют игрок против компьютера. 
#Первый ход определяется жеребьёвкой.За один ход можно забрать не более чем 28 конфет.
#Все конфеты оппонента достаются сделавшему последний ход. 
#Подумайте как наделить бота "интеллектом"

from service import input_number
from candy_game import candy_game
from model import Rival
from os import system

MIN_VALUE=1
MAX_VALUE=28
COUNT_CANDY=150

def main():
    while(True):
        system('clear')
        print("      Меню")
        print("1 - Игра PVP")
        print("2 - Игра против компьютера")
        print("3 - Игра против компьютера(Кошмар)")
        print("0 - Выход\n")
        action=input_number(0,3,"Введите номер пункта: ","Некорректный ввод")
        match action:
            case 1:
                candy_game(COUNT_CANDY,MIN_VALUE,MAX_VALUE,Rival.HUMAN.value)
            case 2:
                candy_game(COUNT_CANDY,MIN_VALUE,MAX_VALUE,Rival.BOT_EASY.value)
            case 3:
                candy_game(COUNT_CANDY,MIN_VALUE,MAX_VALUE,Rival.BOT_HARD.value)
            case 0:
                exit()
        input_number(0,0,"Выход - 0\n->:","Некорректное значение")
main()