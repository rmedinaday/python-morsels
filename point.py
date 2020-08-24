class Point():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return (self.x == other.x) & (self.y == other.y) & (self.z == other.z)

    def __repr__(self):
        return f"Point(x={str(self.x)}, y={str(self.y)}, z={str(self.z)})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __rmul__(self, other):
        return Point(self.x * other, self.y * other, self.z * other)

    def __mul__(self, other):
        if type(other) == Point:
            return Point(self.x * other.x, self.y * other.y, self.z * other.z)
        else:
            return Point(self.x * other, self.y * other, self.z * other)

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z