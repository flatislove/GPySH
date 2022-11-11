#5. Создать список, содержащий цены на товары (10–20 товаров),
# например:[57.8, 46.51, 97, ...]
#Вывести на экран эти цены через запятую в одну строку, цена 
# должна отображаться в виде <r> руб <kk> коп (например «5 руб 
# 04 коп»). Подумать, как из цены получить рубли и копейки, как
#  добавить нули, если, например, получилось 7 копеек или 0 
# копеек (должно быть 07 коп или 00 коп).
#Вывести цены, отсортированные по возрастанию, новый список не 
# создавать (доказать, что объект списка после сортировки 
# остался тот же).
#Создать новый список, содержащий те же цены, но отсортированные
#  по убыванию. Вывести цены пяти самых дорогих товаров. 
# Сможете ли вывести цены этих товаров по возрастанию, 
# написав минимум кода?

prices=[57.8, 46.51, 97, 42.1, 1.01, 7, 3.21, 0, 12.13, 100]

def check_add_zero(el):
    return el if int(el)>=10 else '0'+el

def print_prices(arr, check=0):
    if check!=0:
        lnk=arr
        arr.sort()
        print(f'Объект тот же: {lnk is arr}\n')
    for x in arr:
        print(f'{int(x)} руб {check_add_zero(str(int(round(x%1,2)*100)))} коп')
    print('\n')

def create_new_list_prices(arr):
    new_arr=arr.copy()
    new_arr.sort(reverse=True)
    return new_arr

def show_5_top_expensive(arr):
    return print_prices(create_new_list_prices(arr)[0:5])

def solve():
    print_prices(prices,1)
    print_prices(create_new_list_prices(prices))
    show_5_top_expensive(prices)

solve()

