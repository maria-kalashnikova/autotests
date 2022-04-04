"""
utf-8
Создан 26.10.2021

:author: maria.kalashnikova

Обучающий курс Python QA Engineer.
Домашняя работа №2. Класс треугольников.
"""
from oop_pattern.src.figure import Figure


class Triangle(Figure):
    """
    Класс для создания треугольников

    Могут быть созданы треугольники:
    - равносторонний - необходимо передать 1 аргумент (длинну стороны)
    - равнобедренный - необходимо передать 2 аргумента (длинну основания и длину стороны)
    - обыкновенный - необходимо передать 3 аргумента (длинну каждой стороны)
    """
    name = "Triangle"

    def __new__(cls, *args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) is False:
                raise ValueError(f"Side value can be an int or float, not {type(arg)}")
            if arg <= 0:
                raise ValueError(f"The side length must be a positive value, not {arg}")
        if len(args) == 3:
            if (args[0] + args[1] > args[2] and args[0] + args[2] > args[1] and args[1] + args[2] > args[0]) is False:
                return None
            else:
                new_obj = object.__new__(cls)
                return new_obj
        else:
            new_obj = object.__new__(cls)
            return new_obj

    def __init__(self, *args):
        if len(args) == 1:
            self.side_values = [args[0], args[0], args[0]]
        elif len(args) == 2:
            self.side_values = [args[0], args[1], args[1]]
        elif len(args) == 3:
            self.side_values = []
            for arg in args:
                self.side_values.append(arg)
        else:
            raise ValueError("it's not a triangle. Maximum 3 values can be passed")

    @property
    def area(self):
        semi_perimeter = self.perimeter/2
        base_of_degree = 1
        for side in self.side_values:
            factor = (semi_perimeter - side)
            base_of_degree *= factor
        area = (base_of_degree * semi_perimeter) ** 0.5
        return round(area, 2)

a = Triangle(13, 14, 15)
print(a.perimeter)