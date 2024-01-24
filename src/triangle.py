"""Class Triangle is here"""
import math

from src.figure import Figure


class Triangle(Figure):
    """Class Triangle is here"""
    def __init__(self, side_a, side_b, side_c):
        super().__init__(name="Triangle")
        if side_a <= 0 > side_b or side_c <= 0 \
                or side_a + side_b <= side_c or side_a + side_c <= side_b \
                or side_b + side_c <= side_a:
            raise ValueError("нельзя создать треугольник")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_perimetr(self):
        return self.side_a + self.side_b + self.side_c

    def get_area(self):
        s = (self.side_a + self.side_b + self.side_c) / 2
        area = math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))
        return area
