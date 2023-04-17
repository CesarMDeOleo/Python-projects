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
    

cur_Point = Point(1, 2, 3)
p2 = Point(4, 5, 6)


print(cur_Point) 
print(cur_Point.r)
print(cur_Point == p2)
print(cur_Point < p2)


p3 = cur_Point + p2
print(p3)

cur_Point += p2
print(cur_Point)

print(cur_Point.asdict())