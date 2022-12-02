from task1 import write_random_polynomial_to_file
import sympy
from random import randint
import re

#Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

def sum_polynomial(pol1,pol2):
    if pol1=="\n" or pol2=="\n": return "Не удалось сформировать уравнение"
    sub_pol1,sub_pol2=pol1,pol2
    if sub_pol1.startswith('-'):sub_pol1=sub_pol1[1:]
    if sub_pol2.startswith('-'): sub_pol2=sub_pol2[1:]
    sub_list_one=re.split('[+-]',sub_pol1)
    sub_list_two=re.split('[+-]',sub_pol2)
    curr_pow_one,curr_pow_two=sub_list_one[0].split('*')[-1],sub_list_two[0].split('*')[-1]
    position_one,position_two=0,0
    sign_one=re.split('\d+\*x\*\*\d+|\d+',pol1)
    sign_two=re.split('\d+\*x\*\*\d+|\d+',pol2)
    sign_one = list(filter(lambda x: (x!=''), sign_one))
    sign_two = list(filter(lambda x: (x!=''), sign_two))
    if len(sub_list_one)!=len(sign_one): sign_one.insert(0,'+')
    if len(sub_list_two)!=len(sign_two):sign_two.insert(0,'+')
    res=""
    while(True):
        if int(curr_pow_one)>int(curr_pow_two):
            res+=f'{sign_one[position_one]}'
            res+=sub_list_one[position_one]
            position_one+=1
            if '**' in sub_list_one[position_one]: curr_pow_one=sub_list_one[position_one].split('*x**')[-1]
            else: curr_pow_one='0'
        elif int(curr_pow_two)>int(curr_pow_one):
            res+=f'{sign_two[position_two]}'
            res+=sub_list_two[position_two]
            position_two+=1
            if '**' in sub_list_two[position_two]: curr_pow_two=sub_list_two[position_two].split('*x**')[-1]
            else: curr_pow_two='0'
        elif int(curr_pow_one)==int(curr_pow_two) and curr_pow_one!='0':
            parameters_one,parameters_two=sub_list_one[position_one].split('*x**'),sub_list_two[position_two].split('*x**')
            coef=int(f'{sign_one[position_one]}{parameters_one[0]}')+int(f'{sign_two[position_two]}{parameters_two[0]}')
            sign='+' if coef>=0 else ''
            if coef!=0:res+=f'{sign}{coef}*x**{parameters_one[1]}'
            position_one+=1
            position_two+=1
            if '**' in sub_list_one[position_one]:curr_pow_one=sub_list_one[position_one].split('*')[-1]
            else: curr_pow_one='0'
            if '**' in sub_list_two[position_two]:curr_pow_two=sub_list_two[position_two].split('*')[-1]
            else: curr_pow_two='0'
        elif (curr_pow_one=='0' and position_one!=0)and(curr_pow_two=='0' and position_two!=0):break
    c=int(f'{sign_one[-1]}{sub_list_one[position_one]}')+int(f'{sign_two[-1]}{sub_list_two[position_two]}')
    if c>0: c=f'+{c}'
    res+=f'{c},x'
    if res.startswith('+'): res=res[1:]
    return res

def read_polynomial_from_file(file):
    with open('GPySA4/{}'.format(file),'r', encoding='utf-8') as f: res=f.readline()
    return res.split(',')[0]

def write_sum_polynomial(polynomial):
    with open('GPySA4/sum_file.txt','w', encoding='utf-8') as f: f.write(polynomial)

def main():
    f1,f2='file1.txt','file2.txt'
    write_random_polynomial_to_file(randint(2,10),f"GPySA4/{f1}")
    write_random_polynomial_to_file(randint(2,10),f"GPySA4/{f2}")
    poly1,poly2=read_polynomial_from_file(f1),read_polynomial_from_file(f2)
    print(f'Первый многочлен: {poly1}\nВторой многочлен: {poly2}')
    s=sum_polynomial(poly1,poly2)
    print(f'Результат суммирования: {s}')
    write_sum_polynomial(s)
    if "x" in s:
        x=sympy.symbols('x')
        res_polynomial=read_polynomial_from_file("sum_file.txt")
        print(f'Корни уравнения:\n{sympy.solve(res_polynomial)}')
    r="13*x**3-47*x**2+57"
    print(sympy.solve(r,x))

# main()