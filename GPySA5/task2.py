#Создайте программу для игры в ""Крестики-нолики"".
import os

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
    for idx in range(len(arr)):
        for idy in range(len(arr[0])):
            check_row+=arr[idx][idy]
        if check_row[0]==check_row[1]==check_row[2]!=' ':
            return True
        else: check_row=''
    for idx in range(len(arr[0])):
        for idy in range(len(arr)):
            check_column+=arr[idy][idx]
        if check_column[0]==check_column[1]==check_column[2]!=' ':
            return True
        else: check_column=''
    if (arr[0][0]==arr[1][1]==arr[2][2]!=' ') \
        or (arr[2][0]==arr[1][1]==arr[0][2]!=' '):
        return True
    return False

tic_tac_toe()