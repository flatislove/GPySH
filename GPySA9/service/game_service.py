from random import randint
from src.config import get_comlexity


def is_win(amount: int):
    if amount <= 0:
        return True


def get_candy_amount(amount: int):
    complex = get_comlexity()
    if complex == "EASY":
        return randint(1, 28) if amount > 27 else randint(1, amount)
    elif complex == "HARD":
        for i in range(1, 29):
            if (amount-i) % 29 == 0:
                return i
        return 28
