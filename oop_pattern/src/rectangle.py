"""
utf-8
Создан 26.10.2021

:author: maria.kalashnikova

Обучающий курс Python QA Engineer.
Домашняя работа №2. Класс прямоугольников.
"""
from oop_pattern.src.figure import Figure


class Rectangle(Figure):
    """
    Класс для создания прямоугольников

    Принимает на вход 2 параметра - длины сторон.
    """
    name = "Rectangle"

    def __init__(self, *args):
        if len(args) != 2:
            raise ValueError(f"it's not a rectangle. Need to send 2 values, not {len(args)}")
        else:
            self.side_values = []
            for arg in args:
                if isinstance(arg, (int, float)) is False:
                    raise ValueError(f"Side value can be an int or float, not {type(arg)}")
                if arg <= 0:
                    raise ValueError(f"The side length must be a positive value, not {arg}")
                self.side_values.append(arg)

    @property
    def area(self):
        area = self.side_values[0] * self.side_values[1]
        return round(area, 2)

    @property
    def perimeter(self):
        print(self.side_values)
        perimeter = (self.side_values[0] + self.side_values[1]) * 2
        return perimeter
