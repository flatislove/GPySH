from enum import Enum


class Number_mode(Enum):
    CONVERTER = 1
    GAME = 2
    DEFAULT = 0


class Complexity(Enum):
    EASY = 0
    HARD = 1


class Candy_amount(Enum):
    FEW = 150
    NORMAL = 500
    MANY = 1000
