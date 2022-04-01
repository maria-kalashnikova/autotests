"""
utf-8
Создан 26.10.2021

:author: maria.kalashnikova

Обучающий курс Python QA Engineer.
Домашняя работа №2. Базовый класс фигур.
"""


class Figure:
    """
    Базовый класс для создания двухмерных(плоских) геометрических фигур
    """
    name = "Polygon"
    side_values = []
    apothem_value = None

    def __init__(self, *args, apothem=None):
        self.apothem_value = apothem
        if len(args) == 0 or len(args) == 2:
            raise ValueError("Incorrect number of sides")
        for arg in args:
            if isinstance(arg, (int, float)) is False:
                raise ValueError(f"Side value can be an int or float, not {type(arg)}")
            if arg <= 0:
                raise ValueError(f"The side length must be a positive value, not {arg}")
            self.side_values.append(arg)

    @property
    def perimeter(self):
        """
        Общая формула вычисления периметра любого многоугольника
        """
        perimeter = 0
        for side_value in self.side_values:
            perimeter += side_value
        return perimeter

    @property
    def area(self):
        """
        Общая формула вычисления площади любого многоугольника
        """
        area = (self.perimeter * self.apothem_value)/2
        return round(area, 2)

    def add_area(self, figure_name):
        """
        Суммирует площадь фигуры класса и переданной фигуры

        :param figure_name: фигура, чья площадь прибавляется
        :type figure_name: object

        :return: сумма площадей двух фигур
        :rtype: float
        """
        if isinstance(figure_name, Figure) is False:
            raise ValueError("The passed object is not a geometry figure")
        else:
            figure_area = figure_name.area
            return self.area + figure_area
