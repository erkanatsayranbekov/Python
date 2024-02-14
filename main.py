class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __sub__(self, other):
        return Circle(self.radius - other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other.radius)

    def __truediv__(self, other):
        return Circle(self.radius / other.radius)

    def __str__(self) -> str:
        return str(self.radius)