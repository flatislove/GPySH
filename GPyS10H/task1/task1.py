import operation_stat as s

# Реализуйте классы MinStat, MaxStat, AverageStat, которые будут находить
# минимум, максимум и среднее арифметическое последовательности целых 
# чисел. Экземпляры классов инициализируются без аргументов. Метод add_number
# должен добавлять в статистику число, которое будет учтено  при вычислении 
# финального результата методом result. Для экземпляров MinStat и MaxStat 
# result должен возвращать целое число, для AverageStat — число типа float
# (это число будет сравниваться с правильным ответом до седьмой значащей цифры).
#  Если в последовательности отсутствуют числа и статистические величины 
# вычислить невозможно, метод result должен возвращать None.

#Сценарий из требований
print("Сценарий 1")
values=[1,2,4,5]
mins=s.MinStat()
maxs=s.MaxStat()
average=s.AverageStat()
for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)
print(mins.result(),maxs.result(),'{:<05.3}'.format(average.result()))
print("\nСценарий 2")
values=[1,2,4,5]
mins=s.MinStat()
maxs=s.MaxStat()
average=s.AverageStat()
print(mins.result(),maxs.result(),average.result())
print("\nСценарий 3")
values=[1,0,0]
mins=s.MinStat()
maxs=s.MaxStat()
average=s.AverageStat()
for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)
print(mins.result(),maxs.result(),'{:<05.3}'.format(average.result()))