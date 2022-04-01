"""
utf-8
Создан 26.10.2021

:author: maria.kalashnikova

Обучающий курс Python QA Engineer.
Домашняя работа №2. Юнит-тесты класса Rectangle
"""
from oop_pattern.src.rectangle import Rectangle
import pytest


def test_create_rectangle():
    rectangle = Rectangle(22, 38)
    assert isinstance(rectangle, Rectangle)


@pytest.mark.parametrize("height, width", [["22", 22], ["22", "33"], [[4, 4, 4], {"dd": 33}]])
def test_create_rectangle_incor_type_val(height, width):
    try:
        Rectangle(height, width)
    except ValueError as e:
        assert str(e) == f"Side value can be an int or float, not {type(height)}" or \
               str(e) == f"Side value can be an int or float, not {type(width)}"


@pytest.mark.parametrize("height, width", [[0, -2], [0, 0], [-3, -2]])
def test_create_rectangle_incor_val(height, width):
    try:
        Rectangle(height, width)
    except ValueError as e:
        assert str(e) == f"The side length must be a positive value, not {height}" or \
               str(e) == f"The side length must be a positive value, not {width}"


def test_create_rectangle_incor_num_of_params():
    try:
        Rectangle(33, 22, 55)
    except ValueError as e:
        assert str(e) == f"it's not a rectangle. Need to send 2 values, not 3"


def test_check_name_rectangle():
    rectangle = Rectangle(10, 19)
    name = rectangle.name
    assert name == "Rectangle"


def test_check_perimeter():
    rectangle = Rectangle(3, 29)
    perimeter = rectangle.perimeter
    assert isinstance(perimeter, (int, float))


def test_check_perimeter_val():
    rectangle = Rectangle(3, 5)
    perimeter = 2 * (3 + 5)
    perimeter = round(perimeter, 2)
    assert rectangle.perimeter == perimeter


def test_check_area():
    rectangle = Rectangle(3, 10)
    area = rectangle.area
    assert isinstance(area, (int, float))


def test_check_area_val():
    rectangle = Rectangle(3, 5)
    area = 3 * 5
    area = round(area, 2)
    assert rectangle.area == area


def test_check_add_area():
    rectangle_1 = Rectangle(2, 10)
    area_1 = rectangle_1.area
    rectangle_2 = Rectangle(22, 12)
    area_2 = rectangle_2.area
    assert rectangle_1.add_area(rectangle_2) == area_1 + area_2


@pytest.mark.parametrize("figure", [22, "some text", int()])
def test_add_area_incor(figure):
    try:
        rectangle = Rectangle(20, 10)
        rectangle.add_area(figure)
    except ValueError as e:
        assert str(e) == "The passed object is not a geometry figure"
