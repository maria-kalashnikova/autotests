"""
utf-8
Создан 26.10.2021

:author: maria.kalashnikova

Обучающий курс Python QA Engineer.
Домашняя работа №2. Юнит-тесты класса Square
"""
from oop_pattern.src.square import Square
import pytest


def test_create_square():
    square = Square(22)
    assert isinstance(square, Square)


@pytest.mark.parametrize("side", [["22", [4, 4, 4], {"side": 22}]])
def test_create_square_incor_type_val(side):
    try:
        Square(side)
    except ValueError as e:
        assert str(e) == f"Side value can be an int or float, not {type(side)}"


@pytest.mark.parametrize("side", [0, -2])
def test_create_square_incor_val(side):
    try:
        Square(side)
    except ValueError as e:
        assert str(e) == f"The side length must be a positive value, not {side}"


def test_check_name_square():
    square = Square(4)
    name = square.name
    assert name == "Square"


def test_check_perimeter():
    square = Square(4)
    perimeter = square.perimeter
    assert isinstance(perimeter, (int, float))


def test_check_perimeter_val():
    square = Square(4)
    perimeter = 4 * 4
    perimeter = round(perimeter, 2)
    assert square.perimeter == perimeter


def test_check_area():
    square = Square(4)
    area = square.area
    assert isinstance(area, (int, float))


def test_check_area_val():
    square = Square(4)
    area = 4 ** 2
    area = round(area, 2)
    assert square.area == area


def test_check_add_area():
    square_1 = Square(4)
    area_1 = square_1.area
    square_2 = Square(10)
    area_2 = square_2.area
    assert square_1.add_area(square_2) == area_1 + area_2


@pytest.mark.parametrize("figure", [22, "some text", int()])
def test_add_area_incor(figure):
    try:
        square = Square(6)
        square.add_area(figure)
    except ValueError as e:
        assert str(e) == "The passed object is not a geometry figure"
