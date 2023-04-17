import math
import random

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

class Sphere:
    def __init__(self, center: Point, radius):
        self._center = center
        self.radius = radius

    def __str__(self):
        return f"The volume of the sphere centered at {self._center} with a radius of {self.radius:.3f} is equal to {self.vol:.3f}."

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("The radius of a circle must be positive")
        self._radius = value

    @property
    def vol(self):
        return ((4/3) * math.pi * self.radius**3)

class CenteredSphere(Sphere):
    def __init__(self, radius):
        super().__init__(Point(0, 0, 0), radius)

    def __str__(self):
        return f"The volume of the sphere centered at the origin with a radius of {self.radius:.3f} is equal to {self.vol:.3f}."


spheres1 = []
for _ in range(4):
    center = Point(random.randint(0, 5), random.randint(0, 5), random.randint(0, 5))
    radius = random.uniform(1, 5)
    sphere = Sphere(center, radius)
    spheres1.append(sphere)

spheres2 = []
for _ in range(2):
    radius = random.uniform(5, 10)
    sphere = CenteredSphere(radius)
    spheres2.append(sphere)

spheres = spheres1 + spheres2

for sphere in spheres:
    print(sphere)