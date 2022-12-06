from re import findall
from file_operations import read_file,write_file

def recovery_run_lenght_encoding(r_filename,w_filename):
    recov_line=''
    rle=read_file(r_filename)
    print(f"Исходные строка:{rle}")
    chars=findall(r'[a-zA-Z]+', rle)
    count=findall(r'\d+', rle)
    for idx,val in enumerate(chars):
        for c in range(int(count[idx])):
            recov_line+=val
    print(f"Преобразованная строка:{recov_line}")
    write_file(w_filename,recov_line)