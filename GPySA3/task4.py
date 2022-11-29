#Напишите программу, которая будет преобразовывать десятичное число в двоичное. 
#Без применения встроеных методов (арифметически)

def get_input_number(message):
    inp=0
    while(True):
        try:
            inp=int(input(message))
            if isinstance(inp, int): return inp
        except Exception as ex:
            print(f"[INFO] Ошибка ввода {ex}")

def get_binary_from_int(number):
    if number==0: return 0
    binary=[]
    while(number>0):
        binary.insert(0,number%2)
        number//=2
    return ''.join(map(str,binary))

print(f'В двоичной системе: {get_binary_from_int(get_input_number("Введите число: "))}')