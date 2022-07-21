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