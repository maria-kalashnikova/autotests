"""
utf-8
Создан 26.10.2021

:author: maria.kalashnikova

Обучающий курс Python QA Engineer.
Домашняя работа №2. Класс квадратов.
"""
from oop_pattern.src.rectangle import Rectangle


class Square(Rectangle):
    """
    Класс для создания квадратов

    Принимает на вход 1 параметра - длину сторон.
    """
    name = "Square"

    def __init__(self, side_val):
        if isinstance(side_val, (int, float)) is False:
            raise ValueError(f"Side value can be an int or float, not {type(side_val)}")
        if side_val <= 0:
            raise ValueError(f"The side length must be a positive value, not {side_val}")
        else:
            self.side_value = side_val

    @property
    def perimeter(self):
        return round(self.side_value * 4, 2)

    @property
    def area(self):
        return round(self.side_value ** 2, 2)
