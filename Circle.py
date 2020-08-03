class Circle():
    def __init__(self, radius=1):
        self.pi = 3.141592653589793
        self._radius = radius

    def __str__(self):
        return "Circle({})".format(self.radius)

    def __repr__(self):
        return "Circle({})".format(self.radius)
    


    @property
    def diameter(self):
        return 2 * self.radius

    @diameter.setter
    def diameter(self, diameter):
        if diameter < 0:
            raise ValueError("Diameter cannot be negative")
        self.radius = diameter / 2

    @property
    def area(self):
        return (self.radius ** 2) * self.pi

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        if r < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = r

c = Circle(5)
print(c.radius)
print(c.diameter)
print(c.area)
print(c)
c.radius = 6
print(c.radius)
print(c.diameter)
print(c.area)
print(c)
print(repr(c))
