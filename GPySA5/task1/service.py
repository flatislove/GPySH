from random import randint

def input_number(min,max,action_mess,neg_mess):
    while(True):
        count_step=input(action_mess)
        if count_step.isnumeric() and min<=int(count_step)<=max: return int(count_step)
        else: print(neg_mess)

def get_bot_count(current_count,min_value,max_value,difficult):
    if difficult==2:
        return randint(min_value,max_value) if current_count>max_value else current_count
    elif difficult==3:
        if current_count<=max_value: return current_count
        else:
            tmp=current_count
            while(tmp>max_value+1):tmp-=(max_value+1)
            for i in range(max_value+1):
                if tmp-i==0: return i