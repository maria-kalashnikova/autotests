"""
utf-8
Создан 26.10.2021

:author: maria.kalashnikova

Обучающий курс Python QA Engineer.
Домашняя работа №2. Юнит-тесты класса Сircle
"""
from oop_pattern.src.circle import Circle
import pytest
import math

pi = math.radians(180)


def test_create_circle():
    circle = Circle(22)
    assert isinstance(circle, Circle)


@pytest.mark.parametrize("radius", ["22", {"radius": 22}, [2, 3]])
def test_create_circle_incor_type_val(radius):
    try:
        Circle(radius)
    except ValueError as e:
        assert str(e) == f"Radius can be an int or float, not {type(radius)}"


@pytest.mark.parametrize("radius", [0, -2])
def test_create_circle_incor_val(radius):
    try:
        Circle(radius)
    except ValueError as e:
        assert str(e) == f"Radius must be a positive value, not {radius}"


def test_check_name_circle():
    circle = Circle(10)
    name = circle.name
    assert name == "Circle"


def test_check_perimeter():
    circle = Circle(3)
    perimeter = circle.perimeter
    assert isinstance(perimeter, (int, float))


def test_check_perimeter_val():
    circle = Circle(3)
    perimeter = 2 * pi * 3
    perimeter = round(perimeter, 2)
    assert circle.perimeter == perimeter


def test_check_area():
    circle = Circle(3)
    area = circle.area
    assert isinstance(area, (int, float))


def test_check_area_val():
    circle = Circle(3)
    area = pi * (3 ** 2)
    area = round(area, 2)
    assert circle.area == area


def test_check_add_area():
    circle_1 = Circle(20)
    area_1 = circle_1.area
    circle_2 = Circle(22)
    area_2 = circle_2.area
    assert circle_1.add_area(circle_2) == area_1 + area_2


@pytest.mark.parametrize("figure", [22, "some text", int()])
def test_add_area_incor(figure):
    try:
        circle = Circle(20)
        circle.add_area(figure)
    except ValueError as e:
        assert str(e) == "The passed object is not a geometry figure"
