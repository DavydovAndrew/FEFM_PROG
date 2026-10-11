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

dots = [Vector(1, 2, 3), Vector(4, 5, 6), Vector(7, 8, 9)] # List of dots
n = len(dots)

s_m = 0
out = 'Пупупуууу...'

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            a, b = dots[j] - dots[i], dots[k] - dots[i]
            # Квадрат площади пар-ма, построенного на a, b
            s = (abs(a) * abs(b)) ** 2 - (a * b) ** 2
            if s >= s_m:
                out = f'({dots[i]}), ({dots[j]}), ({dots[k]})'
                s_m = s

print(out)