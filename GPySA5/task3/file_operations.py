def read_file(filename):
    try:
        with open(filename,'r',encoding='utf-8') as f:
            text=f.readline()
        print(f"[INFO] Файл успешно прочитан")
        return text
    except Exception as ex:
        print(f"[ERROR] Ошибка чтения файла {ex}")
    
def write_file(filename, text):
    try:
        with open(filename,'w',encoding='utf-8') as f:
            f.write(text)
        print(f"[INFO] Данные успешно записаны в файл")
    except Exception as ex:
        print(f"[ERROR] Ошибка записи в файл {ex}")