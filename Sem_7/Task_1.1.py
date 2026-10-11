class Vector():
    def __init__(self, x, y=0, z=0):
        if isinstance(x, str):
            try:
                self.x, self.y, self.z = map(int, x.split(', '))
            except:
                print('Coordinates can only be numbers!')
        else:
            self.x = x
            self.y = y
            self.z = z

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
    
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.x + other, self.y + other, self.z + other)

    def __radd__(self, other):
            return self + other

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.x - other, self.y - other, self.z - other)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.x * other, self.y * other, self.z * other)
    
    def __str__(self):
        return f'x = {self.x}, y = {self.y}, z = {self.z}'

dots = [Vector(1, 2, 3), Vector(4, 5, 6), Vector(7, 8, 9)] # list of dots
s = Vector(0, 0, 0)
for v in dots:
    s += v
print(s * (1 / len(dots)))