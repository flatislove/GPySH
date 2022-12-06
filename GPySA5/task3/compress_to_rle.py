import re
from file_operations import read_file,write_file

def compress_run_length_encoding(r_filename,w_filename):
    text=read_file(r_filename)
    print(f"Исходная строка:{text}")
    symbols=re.findall(r'(.)\1*',text)
    res,count='',0
    pointer_sym,pointer_text=0,0
    while(pointer_sym<len(symbols)):
        if pointer_text<len(text) and symbols[pointer_sym]==text[pointer_text]:
            count+=1
            pointer_text+=1
        else:
            if count>0: res+='{}{}'.format(symbols[pointer_sym],count)
            pointer_sym+=1
            count=0
    print(f"Преобразованная строка:{res}")
    write_file(w_filename,res)