from random import randint
#Задана натуральная степень k. Сформировать случайным 
# образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.

def write_random_polynomial_to_file(power,filename):
    coefficients=[]
    s_pwrs=['⁰','¹','²','³','⁴','⁵','⁶','⁷','⁸','⁹']
    for i in range(power+1):
        coefficients.append(randint(-100,100))
    s,s_disp='',''
    if power>9:
        for i in range(len(s_pwrs),power+1):
            tmp=''
            for _,val in enumerate(str(i)):
                tmp+=s_pwrs[int(val)]
            s_pwrs.append(tmp)
            tmp=''
    for i in range(power):
        int_tmp=randint(0,2)
        if int_tmp!=0:
            sign_operation=""
            if coefficients[i]>=0 and s!="":sign_operation="+"
            s+='{}{}*x**{}'.format(sign_operation,coefficients[i],power-i)
            s_disp+='{}{}x{}'.format(sign_operation,coefficients[i],s_pwrs[power-i])
    if s!='':
        sign_operation=""
        if coefficients[len(coefficients)-1]>=0: sign_operation="+" 
        s+='{}{},x'.format(sign_operation, coefficients[len(coefficients)-1])
    if s_disp!='': s_disp+='{}{}=0'.format(sign_operation, coefficients[len(coefficients)-1])
    with open(filename,'w', encoding='utf-8') as f:
        f.write(s+'\n'+s_disp)
    return s_disp+'\n'+s

def get_input_number(message):
    inp=0
    while(True):
        try:
            inp=int(input(message))
            if isinstance(inp, int): return inp
        except Exception as ex:
            print(f"[INFO] Ошибка ввода {ex}")

def main():
    filename='GPySA4/write_file.txt'
    pow=get_input_number('Введите степень числа: ')
    print("\n Сформирован следующий многочлен:")
    print(write_random_polynomial_to_file(pow,filename))

main()