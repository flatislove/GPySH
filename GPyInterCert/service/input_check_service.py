from typing import List
from model.note import Note
from datetime import datetime


def check_date(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        return False
    except AttributeError:
        return False
    return True


def check_correct_index(notes: List[Note], index):
    if not index.isdigit():
        return False
    else:
        index = int(index)

    if index > len(notes) or index <= 0:
        return False
    return True
