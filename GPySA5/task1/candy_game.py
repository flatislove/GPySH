from random import randint
from os import system
from service import get_bot_count,input_number

def candy_game(candy_count,min_value,max_value,bot_difficult):
    balance=candy_count
    p1_balance,p2_balance=0,0
    active,last_move=0,-1
    game_order=randint(0,1)
    disp_p2="Бот" if 2<=bot_difficult<=3 else "Игрок 2"
    disp_p1='Игрок 1'
    act_message="Забрать конфет: "
    neg_message="Введите корректное количество конфет"
    if game_order==1: active=1
    while(balance>0):
        system('clear')
        print('{}-({}) vs {}-({})'.format(disp_p1,p1_balance,disp_p2,p2_balance))
        print('{} конфет осталось'.format(balance))
        print('Конфеты набирает {}'.format(disp_p1 if active==0 else disp_p2))
        tmp=max_value if max_value<=balance else balance
        if disp_p2=="Бот" and active==1: count_step=get_bot_count(balance,min_value,max_value,bot_difficult)
        else: count_step=input_number(min_value,tmp,act_message,neg_message)
        balance-=count_step
        if active==0: 
            p1_balance+=count_step
            active,last_move=1,0
        else: 
            p2_balance+=count_step
            active,last_move=0,1
    if last_move==0: print('Победил {}'.format(disp_p1))
    elif last_move==1: print('Победил {}'.format(disp_p2))