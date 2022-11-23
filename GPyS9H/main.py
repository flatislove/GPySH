import tic_tac_toe

#Напишите класс TicTacToeBoard для игры в крестики-нолики,
#  который должен иметь следующие методы:
# new_game() – для создания новой игры;
# get_field() – для получения поля (список списков);
# check_field() – для проверки, есть ли победитель, который возвращает X,
#  если победил первый игрок, 0, если второй, D, если ничья 
# и None, если можно продолжать игру;
# make_move(row, col) – который устанавливает значение текущего хода в 
# ячейку поля с координатами row, col, если это возможно, «переключает»
#  ход игрока, а также возвращает сообщение «Победил игрок X» при победе
#  крестиков, «Победил игрок 0» при победе ноликов, «Ничья» в случае ничьей
#  и «Продолжаем играть», если победитель после данного хода неопределён.
# Кроме того, метод make_move должен возвращать сообщение «Клетка <row>, <col> уже занята»,
#  если в клетке уже стоит крестик или нолик, 
# и «Игра уже завершена», если в текущей игре уже выявлен победитель 
# или закончились ячейки для ходов.
# При создании объекта класса должна создаваться новая игра.
# Аргументы row и col метода make_move могут принимать значения от 1 до 3.

def main():
    game=tic_tac_toe.TicTacToeBoard.new_game()
    while(True):
        print(*game.get_field(),sep="\n")
        inp=-1
        while(inp==-1):
            try:
                print(f"Ход игрока {game.active}")
                row=int(input("Введите строку:"))
                column=int(input("Введите столбец:"))
                inp=game.make_move(row,column)
            except Exception as ex:
                print(f"[INFO] Input error {ex}")
        if inp==0: break
    print(*game.get_field(),sep="\n")
    new_game=0
    while(True):
        try:
            print("\n1 - Да, 2 - Нет")
            new_game=int(input("Начать заново?\n->:"))
        except Exception as ex:
            print(f"[INFO] Input error {ex}")
        if new_game==1: main()
        elif new_game==2: exit()

main()