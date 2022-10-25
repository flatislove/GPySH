from random import randint
import os
from re import findall

#Напишите программу, удаляющую из текста все слова, содержащие
#  "абв".

def delete_words(word,text):
    res=''
    words=str(text).split()
    for w in words:
        if word not in w:
            res+=w+' '
    return res

#print(delete_words('sdsd','wewrewr sdsd dferfss dsd dfsdsd'))

#На столе лежит 2021 конфета. Играют два игрока делая ход друг
#  после друга. Первый ход определяется жеребьёвкой. За один ход
#  можно забрать не более чем 28 конфет. Все конфеты оппонента 
# достаются сделавшему последний ход. Сколько конфет нужно 
# взять первому игроку, чтобы забрать все конфеты у своего 
# конкурента?
#a) Добавьте игру против бота
#b) Подумайте как наделить бота "интеллектом"    

def candy_game_pvp(candy_count):
    balance=candy_count
    p1_balance,p2_balance=0,0
    active,last_move=0,-1
    game_order=randint(0,1)
    disp_p1,disp_p2='Игрок 1','Игрок 2'
    if game_order==1: disp_p1,disp_p2='Игрок 2','Игрок 1'
    while(balance>0):
        os.system('clear')
        print('{}-({}) vs {}-({})'.format(disp_p1,p1_balance,disp_p2,p2_balance))
        print('{} конфет осталось'.format(balance))
        print('Конфеты набирает {}'.format(disp_p1 if active==0 else disp_p2))
        while(True):
            count_step=int(input('Забрать конфет: '))
            if 0<count_step<29 and count_step<=balance: break
        balance-=count_step
        if active==0: 
            p1_balance+=count_step
            active,last_move=1,0
        else: 
            p2_balance+=count_step
            active,last_move=0,1
    if last_move==0: print('Победил {}'.format(disp_p1))
    elif last_move==1: print('Победил {}'.format(disp_p2))

#candy_game_pvp(20)

def candy_game_pvb(candy_count):
    balance=candy_count
    p1_balance,bot_balance=0,0
    active,last_move=0,-1
    game_order=randint(0,1)
    disp_p1,disp_bot='Игрок 1','Бот'
    if game_order==1: active=1
    while(balance>0):
        os.system('clear')
        print('{}-({}) vs {}-({})'.format(disp_p1,p1_balance,disp_bot,bot_balance))
        print('{} конфет осталось'.format(balance))
        print('Конфеты набирает {}'.format(disp_p1 if active==0 else disp_bot))
        if active==1:
            count_step=randint(1,28)
        else:
            while(True):
                count_step=int(input('Забрать конфет: '))
                if 0<count_step<29 and count_step<=balance: break
        balance-=count_step
        if active==0: 
            p1_balance+=count_step
            active,last_move=1,0
        else: 
            bot_balance+=count_step
            active,last_move=0,1
    if last_move==0: print('Победил {}'.format(disp_p1))
    elif last_move==1: print('Победил {}'.format(disp_bot))

#candy_game_pvb(2021)

def candy_game_pv_cleverbot(candy_count):
    balance=candy_count
    p1_balance,bot_balance=0,0
    active,last_move=0,-1
    game_order=randint(0,1)
    disp_p1,disp_bot='Игрок 1','Бот'
    if game_order==1: active=1
    while(balance>0):
        os.system('clear')
        print('{}-({}) vs {}-({})'.format(disp_p1,p1_balance,disp_bot,bot_balance))
        print('{} конфет осталось'.format(balance))
        print('Конфеты набирает {}'.format(disp_p1 if active==0 else disp_bot))
        if active==1:
            if balance<29: count_step=balance
            else:
                tmp=balance
                while(tmp>29):
                    tmp-=29
                for i in range(29):
                    if tmp-i==0:
                        count_step=i
        else:
            while(True):
                count_step=int(input('Забрать конфет: '))
                if 0<count_step<29 and count_step<=balance: break
        balance-=count_step
        if active==0: 
            p1_balance+=count_step
            active,last_move=1,0
        else: 
            bot_balance+=count_step
            active,last_move=0,1
    if last_move==0: print('Победил {}'.format(disp_p1))
    elif last_move==1: print('Победил {}'.format(disp_bot))

#candy_game_pv_cleverbot(2021)

#Создайте программу для игры в ""Крестики-нолики"".

def tic_tac_toe():
    a = [[' ', ' ', ' '], [' ', ' ', ' '],[' ',' ',' ']]
    marker=['X','O']
    disp=['Игрок 1','Игрок 2']
    active,isWin=0,False
    while(isWin!=True):
        os.system('clear')
        for i in a:
            print(i)
        if active==0: print('Ход {}'.format(disp[0]))
        else: print('Ход {}'.format(disp[1]))
        while(True):
            row=int(input('Введите строку: '))
            column=int(input('Введите столбец: '))
            if 0<row<4 and 0<column<4 and a[int(row)-1][int(column)-1]==' ':
                if active==0: a[int(row)-1][int(column)-1]=marker[0]
                else: a[int(row)-1][int(column)-1]=marker[1]
                break
        if checkWin(a)==True:
            os.system('clear')
            for w in a:
                print(w)
            if active==0: print('Победа {}'.format(disp[0]))
            else: print('Победа {}'.format(disp[1]))
            break
        elif active==0: active=1
        else: active=0

def checkWin(arr):
    check_row=''
    check_column=''
    for idx,valx in enumerate(arr):
        for idy,valy in enumerate(arr[0]):
            check_row+=arr[idx][idy]
        if check_row[0]==check_row[1]==check_row[2]!=' ':
            return True
        else: check_row=''
    for idx,valx in enumerate(arr[0]):
        for idy,valy in enumerate(arr):
            check_column+=arr[idy][idx]
        if check_column[0]==check_column[1]==check_column[2]!=' ':
            return True
        else: check_column=''
    if (arr[0][0]==arr[1][1]==arr[2][2]!=' ') \
        or (arr[2][0]==arr[1][1]==arr[0][2]!=' '):
        return True
    return False

#tic_tac_toe()

#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
    
def compress_run_length_encoding(filename):
    res=''
    counter,i=0,0
    with open('GPyS5H/line.txt','r',encoding='utf-8') as f:
        text=f.readline()
    while(i<len(text)-1):
        counter=1
        while(i<len(text)-1 and text[i]==text[i+1]):
            counter+=1
            i+=1
        res+='{}{}'.format(text[i],counter)
        i+=1
    with open('GPyS5H/fileRLE.txt','w',encoding='utf-8') as f:
        f.write(res)
#compress_run_length_encoding('line.txt')

def recovery_run_lenght_encoding(filename):
    rle=''
    recov_line=''
    with open(filename,'r',encoding='utf-8') as f:
        rle=f.readline()
    chars=findall(r'[a-zA-Z]+', rle)
    count=findall(r'\d+', rle)
    for idx,val in enumerate(chars):
        for c in range(int(count[idx])):
            recov_line+=val
    with open('GPyS5H/recovery_line.txt','w',encoding='utf-8') as f:
        f.write(recov_line)

#recovery_run_lenght_encoding('GPyS5H/fileRLE.txt')