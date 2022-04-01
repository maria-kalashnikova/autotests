"""
utf-8
Создан 26.10.2021

:author: maria.kalashnikova

Обучающий курс Python QA Engineer.
Домашняя работа №2. Класс окружностей.
"""
import math

from oop_pattern.src.figure import Figure


class Circle(Figure):
    """
    Класс для создания окружностей

    Принимает на вход 1 параметра - радиус окружности.
    """
    name = "Circle"
    pi_const = math.radians(180)

    def __init__(self, radius_val, *args):
        if isinstance(radius_val, (int, float)) is False:
            raise ValueError(f"Radius can be an int or float, not {type(radius_val)}")
        if radius_val <= 0:
            raise ValueError(f"Radius must be a positive value, not {radius_val}")
        else:
            self.radius = radius_val

    @property
    def perimeter(self):
        return round(self.radius * 2 * self.pi_const, 2)

    @property
    def area(self):
        return round(self.radius ** 2 * self.pi_const, 2)


