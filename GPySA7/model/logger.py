from datetime import datetime
from enum import Enum


class Status(Enum):
    error = "[ERROR]"
    info = "[INFO]"
    debug = "[DEBUG]"


def add(data: str, status: Status):
    current_time = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    try:
        with open(f'GPySA7/log.log', 'a', encoding='utf-8') as log:
            log.write(f"{current_time} - {status} - {data}\n")
    except Exception as ex:
        print(f"{Status.error.value} Ошибка записи в файл log {ex}")


def print_log():
    try:
        with open(f'GPySA7/log.log', 'r', encoding='utf-8') as log:
            logs = log.readlines()
            return logs
    except Exception as ex:
        add(str(ex), Status.error.value)
