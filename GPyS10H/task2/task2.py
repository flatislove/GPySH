import table as t
#  Реализуйте класс Table, который хранит целые числа в двумерной
#  таблице. При инициализации Table(rows, cols) экземпляру передаются 
# число строк и столбцов в таблице. Строки и столбцы нумеруются с нуля.
# table.get_value(row, col) — прочитать значение из ячейки в строке row,
# столбце col. Если ячейка с индексами row и col не лежит внутри 
# таблицы, нужно вернуть None.
# table.set_value(row, col, value) — записать число в ячейку строки row,
# столбца col. Гарантируется, что в тестах будет в запись только в 
# ячейки внутри таблицы.
# table.n_rows() — вернуть число строк в таблице
# table.n_cols() — вернуть число столбцов в таблице
# table.delete_row(row) — удалить строку с номером row
# table.delete_col(col) — удалить колонку с номером col

# table.add_row(row) — добавить в таблицу новую строку с индексом row.
# Номера строк >= row, должны увеличиться на единицу. Новая строка 
# состоит из нулей.
# table.add_col(col) — добавить в таблицу новую колонку с индексом col.
# Номера колонок >= col, должны увеличиться на единицу. Новая колонка 
# состоит из нулей.

print("Сценарий 1\n")
tab=t.Table(3,5)
tab.set_value(0,1,10)
tab.set_value(1,2,20)
tab.set_value(2,3,30)
print(tab)
tab.add_row(1)
print(tab)
print("Сценарий 2\n")
tab2=t.Table(2,2)
print(tab2)
tab2.set_value(0,0,10)
tab2.set_value(0,1,20)
tab2.set_value(1,0,30)
tab2.set_value(1,1,40)
print(tab2)
for i in range(-1,tab2.n_rows()+1):
    for j in range(-1,tab2.n_cols()+1):
        print(tab2.get_value(i,j),end=' ')
    print()
print()
tab2.add_row(0)
tab2.add_column(1)
for i in range(-1,tab2.n_rows()+1):
    for j in range(-1,tab2.n_cols()+1):
        print(tab2.get_value(i,j),end=' ')
    print()
print()
print("Сценарий 3\n")
tab3=t.Table(1,1)
print(tab3)
tab3.set_value(0,0,1000)
print(tab3)
for i in range(-1,tab3.n_rows()+1):
    for j in range(-1,tab3.n_cols()+1):
        print(tab3.get_value(i,j),end=' ')
    print()
print()
tab3.add_row(0)
tab3.add_row(2)
tab3.add_column(0)
tab3.add_column(2)
tab3.set_value(0,0,2000)
tab3.set_value(0,2,3000)
tab3.set_value(2,0,4000)
tab3.set_value(2,2,5000)
for i in range(-1,tab3.n_rows()+1):
    for j in range(-1,tab3.n_cols()+1):
        print(tab3.get_value(i,j),end=' ')
    print()
print()