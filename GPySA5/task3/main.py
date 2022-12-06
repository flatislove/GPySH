##Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
from compress_to_rle import compress_run_length_encoding
from recovery_rle import recovery_run_lenght_encoding

def main():
    comp_input_file='GPySA5/task3/files/start_data.txt'
    comp_output_file='GPySA5/task3/files/rle_expression.txt'
    compress_run_length_encoding(comp_input_file,comp_output_file)

    rec_input_file='GPySA5/task3/files/rle_expression.txt'
    rec_output_file='GPySA5/task3/files/recovery_data.txt'
    recovery_run_lenght_encoding(rec_input_file,rec_output_file)

main()