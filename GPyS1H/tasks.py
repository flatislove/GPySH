import math

# 1
#Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот 
# день выходным.

def is_weekend(day):
    return 'Да' if 5<day<8 else 'Нет' if 0<day<6 else "Некорректный ввод"

#print(is_weekend(int(input('Введите день недели(число): '))))


# 2
#Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def print_truth_table():
    for x in range(2):
        for y in range(2):
            for z in range(2):
                print('¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z',' x=',x,' y=',y,' z=',z, 
                not (x or y or z) == (not x) and (not y) and (not z))

#print_truth_table()


# 3
#Напишите программу, которая принимает на вход координаты 
# точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти 
# плоскости, в которой находится эта точка (или на какой оси
#  она находится).

def get_quarter_coordinate_number(x,y):
    return (1 if x>0 and y>0 else 2 if x<0 and y>0 
    else 3 if x<0 and y<0 else 4 if x>0 and y<0 
    else 'Центр' if x==0 and y==0 else 'Ось Y' if x==0 
    else 'Ось X' if y==0 else 'Некорретный ввод')

#print(get_quarter_coordinate_number(
#    int(input('Введите координату X: ')),
#    int(input('Введите координату Y: '))))


# 4
#Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой 
# четверти (x и y).

def get_range(number_quarter):
    return (f'x,y=({0}:{math.inf})({0}:{math.inf})' if number_quarter==1 
    else f'x,y=({-math.inf}:{0})({0}:{math.inf})' if number_quarter==2
    else f'x,y=({-math.inf}:{0})({-math.inf}:{0})' if number_quarter==3
    else f'x,y=({0}:{math.inf})({-math.inf}:{0})' if number_quarter==4
    else 'Некорректный ввод')

#print(get_range(int(input('Введите коодинатную четверть: '))))


# 5
# Напишите программу, которая принимает на вход координаты 
# двух точек и находит расстояние между ними в 2D пространстве.

def get_distance(ax,ay,bx,by):
    return round(math.sqrt(math.pow(bx-ax,2)+math.pow(by-ay,2)),23)

#print(get_distance(int(input('Введите A(x): ')),int(input('Введите A(y): ')),
#int(input('Введите B(x): ')),int(input('Введите B(y): '))))