"""
utf-8
Создан 26.10.2021

:author: maria.kalashnikova

Обучающий курс Python QA Engineer.
Домашняя работа №2. Юнит-тесты класса Rectangle
"""
from oop_pattern.src.triangle import Triangle
import pytest


def test_create_triangle():
    triangle = Triangle(2)
    assert isinstance(triangle, Triangle)


@pytest.mark.parametrize("side", ["22", {"dd": 33}])
def test_create_triangle_incor_type_val(side):
    try:
        Triangle(side)
    except ValueError as e:
        assert str(e) == f"Side value can be an int or float, not {type(side)}"


@pytest.mark.parametrize("side", [0, -1])
def test_create_triangle_incor_type_val(side):
    try:
        Triangle(side)
    except ValueError as e:
        assert str(e) == f"The side length must be a positive value, not {side}"


def test_create_triangle_incor_num_of_params():
    try:
        Triangle(13, 14, 15, 16)
    except ValueError as e:
        assert str(e) == f"it's not a triangle. Maximum 3 values can be passed"


def test_create_triangle_non_existent():
    triangle = Triangle(2, 12, 6)
    assert triangle is None


def test_check_name_triangle():
    triangle = Triangle(10, 19)
    name = triangle.name
    assert name == "Triangle"


def test_check_perimeter():
    triangle = Triangle(10, 19)
    perimeter = triangle.perimeter
    assert isinstance(perimeter, (int, float))


def test_check_perimeter_val():
    triangle = Triangle(13, 14, 15)
    perimeter = 13 + 14 + 15
    perimeter = round(perimeter, 2)
    assert triangle.perimeter == perimeter


def test_check_area():
    triangle = Triangle(10, 19, 10)
    area = triangle.area
    assert isinstance(area, (int, float))


def test_check_add_area():
    triangle_1 = Triangle(10, 19, 10)
    area_1 = triangle_1.area
    triangle_2 = Triangle(13, 14, 15)
    area_2 = triangle_2.area
    assert triangle_1.add_area(triangle_2) == area_1 + area_2


@pytest.mark.parametrize("figure", [22, "some text", int()])
def test_add_area_incor(figure):
    try:
        rectangle = Triangle(10, 19, 10)
        rectangle.add_area(figure)
    except ValueError as e:
        assert str(e) == "The passed object is not a geometry figure"
