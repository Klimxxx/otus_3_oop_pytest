"""Class Square is here"""

from src.rectangle import Rectangle


class Square(Rectangle):
    """Class Square is here"""

    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError("нельзя создать квадрат")
        super().__init__(side_a, side_a)
