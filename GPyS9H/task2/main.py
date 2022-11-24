import sea_battle

#Напишите класс, который будет строить карту для игры в морской бой
# Класс SeaMap должен иметь следующие методы
#(sm-экземпяр SeaMap):
#  sm.shoot(row,col,result) - добавить на карту результат выстрела, где
#row- индекс ряда карты
#col-индекс вертикальной колонки
#result-одна из строк: miss(промах), hit(попадание), sink(потопление корабля)
# sm.sell(row,col) который
# возвращает '.' если в клетке с координатами row,col может находиться корабль,
# возвращает '*', если в клетку уже стреляли или она находится рядом с потопленным кораблем,
# возвращает 'x', если в клетке было попадание.
# учтите, что не нужно помечать '*' клетки рядом с кораблем, в который попали, но не потопили до конца

#Cценарий из требований
def main():
    sm=sea_battle.SeaMap()
    sm.shoot(2,0,"miss")
    sm.shoot(6,9,"miss")

    sm.shoot(2,0,"sink")
    sm.shoot(6,9,"hit")

    sm.shoot(0,0,"sink")
    sm.shoot(0,9,"sink")
    sm.shoot(9,0,"sink")
    sm.shoot(9,9,"sink")

    sm.shoot(0,0,"hit")
    sm.shoot(0,1,"sink")
    
    sm.shoot(3,4,"hit")
    sm.shoot(3,5,"hit")
    sm.shoot(3,3,"sink")

    for row in range(10):
        print()
        for col in range(10):
            print(sm.sell(row,col),end=' ')
    print("\n")

main()