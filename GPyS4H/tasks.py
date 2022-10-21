import sympy
import math
from random import randint

#Вычислить число c заданной точностью d

def get_number_accuracy_math(number,n):
    return round(number,len(str(n+1))-2)

def get_number_accuracy(number,n):
    num_frac=int(math.pow(10,(len(str(n+1))-2))*(number%1))
    if num_frac%10>4: num_frac+=1
    return '{}.{}'.format(int(number), str(num_frac))

#d=0.0001
#print(get_number_accuracy(math.pi,d))
#print(get_number_accuracy_math(math.pi,d))

#Задайте натуральное число N. Напишите программу, которая 
# составит список простых множителей числа N.

def get_list_prime_numbers(number):
    arr=[]
    is_prime=True
    for i in range(1,number):
        if(number%i==0):
                for k in arr:
                    if k==i: is_prime=False
                if is_prime: arr.append(i)
                is_prime=True     
    return arr

#print(get_list_prime_numbers(int(input('Введите число: '))))

#Задайте последовательность чисел. Напишите программу, которая
#  выведет список неповторяющихся элементов исходной 
# последовательности.

def get_input_int_list():
    numbers=[]
    count=int(input('Введите количество чисел: '))
    for _ in range(count):
        numbers.append(int(input('Введите число: ')))
    return numbers

def get_unique_numbers(numbers):
    numbers_dict = {}
    count=0
    for num in numbers:
        numbers_dict.update({num:0})
    for n in numbers_dict:
        for i in numbers:
            if n==i: count+=1
        numbers_dict.update({n:count})
        count=0
    result_set = []
    for i in numbers_dict:
        if numbers_dict.get(i)==1: result_set.append(i)
    return result_set

#print(get_unique_numbers(get_input_int_list()))

#Задана натуральная степень k. Сформировать случайным 
# образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.

def write_random_polynomial_to_file(power):
    coefficients=[]
    s_pwrs=['⁰','¹','²','³','⁴','⁵','⁶','⁷','⁸','⁹']
    for i in range(power+1):
        coefficients.append(randint(0,100))
    s,s_disp='',''
    if power>9:
        for i in range(len(s_pwrs),power+1):
            tmp=''
            for _,val in enumerate(str(i)):
                tmp+=s_pwrs[int(val)]
            s_pwrs.append(tmp)
            tmp=''
    for i in range(power):
        int_tmp=randint(0,1)
        if int_tmp!=0:
            s+='{}*x**{}+'.format(coefficients[i],power-i)
            s_disp+='{}x{}+'.format(coefficients[i],s_pwrs[power-i])
    if s!='': s+='{},x'.format(coefficients[len(coefficients)-1])
    if s_disp!='': s_disp+='{}=0'.format(coefficients[len(coefficients)-1])
    with open('GPyS4H/write_file.txt','w', encoding='utf-8') as f:
        f.write(s+'\n'+s_disp)
    return s_disp+'\n'+s

#print(write_random_polynomial_to_file(int(input('Введите степень числа: '))))

#Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

def sum_polynomial(pol_one,pol_two):
    c1,c2=pol_one.split('+'),pol_two.split('+')
    str_pow1,str_pow2=c1[0],c2[0]
    max_pow=max(str_pow1[len(str_pow1)-1],str_pow2[len(str_pow2)-1])
    ctr1,ctr2=0,0
    result=''
    for i in range(int(max_pow)):
        if i+ctr1<=len(c1) and i+ctr2<=len(c2) \
            and int(max_pow)-i==int(c1[i+ctr1][-1]) \
            and int(max_pow)-i==int(c2[i+ctr2][-1]):
            temp_st1=str(c1[i+ctr1]).split('*')
            temp_st2=str(c2[i+ctr2]).split('*')
            result+='{}*x**{}+'.format(int(temp_st1[0])+\
            int(temp_st2[0]),int(max_pow)-i)
        elif i+ctr1<=len(c1) and i+ctr2<=len(c2) \
            and int(max_pow)-i!=int(c1[i+ctr1][-1]) \
            and int(max_pow)-i==int(c2[i+ctr2][-1]):
            result+=c2[i+ctr2]+'+'
            ctr1-=1
        elif i+ctr1<len(c1) and i+ctr2<len(c2) \
            and int(max_pow)-i==int(c1[i+ctr1][-1]) \
            and int(max_pow)-i!=int(c2[i+ctr2][-1]):
            result+=c1[i+ctr1]+'+'
            ctr2-=1
        elif i+ctr1<len(c1) and i+ctr2<len(c2) \
            and int(max_pow)-i!=int(c1[i+ctr1][-1]) \
            and int(max_pow)-i!=int(c2[i+ctr2][-1]):
            ctr1-=1
            ctr2-=1
        elif i+ctr1>=len(c1) and i+ctr2<len(c2):
            result+=c2[i+ctr2]+'+'
            ctr1-=1
        elif i+ctr1<len(c1) and i+ctr2>=len(c2):
            result+=c1[i+ctr1]+'+'
            ctr2-=1
    if(len(c1[-1])<3 and len(c2[-1])<3): 
        result+='{},x'.format(int(c1[-1])+int(c2[-1]))
    elif(len(c1[-1])>2 and len(c2[-1])<3): 
        result+='{},x'.format(int(c2[-1]))
    elif(len(c1[-1])<3 and len(c2[-1])>2): 
        result+='{},x'.format(int(c1[-1]))
    elif(len(c1[-1])>2 and len(c2[-1])>2): 
        result+='{},x'.format(0)
    return result

def read_polynomial_from_file(file):
    with open('GPyS4H/{}'.format(file),'r', encoding='utf-8') as f:
        res=f.readline()
    return res.split(',')[0]

def write_sum_polynomial(polynomial):
    with open('GPyS4H/sum_file.txt','w', encoding='utf-8') as f:
        f.write(polynomial)

poly1=read_polynomial_from_file('file1.txt')
poly2=read_polynomial_from_file('file2.txt')
write_sum_polynomial(sum_polynomial(poly1,poly2))

#x=sympy.symbols('x')
#print(sympy.solve(97*x**9+14*x**8+1*x**7+31*x**6+85*x**5+81*x**4+22*x**3+81*x**2+70*x**1+77,x))