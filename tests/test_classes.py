"""Proverka testami klassa krug"""

from src.circle import Circle
from src.figure import Figure
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle


def test_circle_positive():
    """Pozitiv test circle"""
    circle_1 = Circle(5)
    assert circle_1.get_area() == 78.53981633974483, \
        f"Ploshad y kruga s radiusom {circle_1.radius} nevernaya"



def test_rectangle_positive():
    """Pozitiv test rectangle"""
    rectangle_1 = Rectangle(side_b=20, side_a=10)
    assert rectangle_1.get_area() == 200
    assert rectangle_1.get_perimetr() == 60


def test_square_negative():
    """Negative test square"""
    try:
        square_1 = Square(-10)
    except ValueError as e:
        assert str(e) == "нельзя создать квадрат"
    else:
        raise AssertionError("Expected ValueError but no exception was raised")


def test_triangle_negative():
    """Negative test triangle"""
    try:
        triangle_1 = Triangle(-10)
    except TypeError as e:
        assert str(e) == "Triangle.__init__() missing 2 required " \
                         "positional arguments: 'side_b' and 'side_c'"


def test_figure_negative():
    """Negative test figure"""
    try:
        Figure_1 = Figure(name=Rectangle)
        Figure_1.get_area() == 1
    except TypeError as e:
        assert str(e) == "Can't instantiate abstract class Figure with " \
                         "abstract methods get_area, get_perimetr"
