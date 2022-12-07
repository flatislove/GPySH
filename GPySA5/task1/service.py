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
        return (current_count-((current_count//max_value)*(max_value+1))) if current_count%(max_value+1)!=0 else max_value