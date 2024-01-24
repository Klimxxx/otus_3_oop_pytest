"""Class Circle is here"""

import math
from src.figure import Figure


class Circle(Figure):
    """Class Circle is here"""

    def __init__(self, radius):
        super().__init__(name="Circle")
        if radius <= 0:
            raise ValueError("нельзя создать круг")
        self.radius = radius

    def get_area(self):
        return self.radius ** 2 * math.pi

    def get_perimetr(self):
        return self.radius * 2 * math.pi
