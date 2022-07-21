class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"
    
    def __eq__(self, p):
        if isinstance(p, Point):
            if self.x == p.x and self.y == p.y and self.z == p.z:
                return True
        return False

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y, self.z + p.z)

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y, self.z - p.z)

    def __mul__(self, num):
        return Point(self.x * num, self.y * num, self.z * num)

    def __rmul__(self, num):
        return Point(self.x * num, self.y * num, self.z * num)

    def __iter__(self):
        return iter((self.x, self.y, self.z))