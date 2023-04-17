import matplotlib.pyplot as plt
import numpy as np
import math

class Point:
    def __init__(self, x, y, z=0):
        self._x = x
        self._y = y
        self._z = z

    @property
    def r(self):
        return math.sqrt(self._x**2 + self._y**2 + self._z**2)

    def __str__(self):
        return f"({self._x}, {self._y}, {self._z})"

    def __eq__(self, other):
        return self.r == other.r

    def __lt__(self, other):
        return self.r < other.r

    def __le__(self, other):
        return self.r <= other.r

    def __gt__(self, other):
        return self.r > other.r

    def __ge__(self, other):
        return self.r >= other.r

    def __add__(self, other):
        return Point(self._x + other._x, self._y + other._y, self._z + other._z)

    def __iadd__(self, other):
        self._x += other._x
        self._y += other._y
        self._z += other._z
        return self

    def asdict(self):
        return {'x': self._x, 'y': self._y, 'z': self._z}
    

class Circle:
    
    def __init__(self, center: Point, radius):
        self._center = center
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("The radius of a circle must be positive")
        self._radius = value
    
    def draw(self):
        fig, ax = plt.subplots()
        x = np.arange(self._center._x - self._radius, self._center._x + self._radius + 1)
        y = self._center._y + np.sqrt(self._radius**2 - (x - self._center._x)**2)
        ax.plot(x, y, color='red', label='Circle')
        ax.plot(x, self._center._y - np.sqrt(self._radius**2 - (x - self._center._x)**2), color='red')
        ax.set_title('Circle Plot')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.legend()
        ax.grid(True)
        ax.text(self._center._x - self._radius, self._center._y + self._radius,
                f'({self._center._x}, {self._center._y})\n(x - {self._center._x})^2 + (y - {self._center._y})^2 = {self._radius}^2', fontsize=10)
        plt.show()


p = Point(2, 3)
c = Circle(p, 1000)
c.draw()