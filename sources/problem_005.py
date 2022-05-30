import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __sub__(self, no):
        result = Points(0.0,0.0,0.0)
        result.x = self.x - no.x
        result.y = self.y - no.y
        result.z = self.z - no.z
        return result
    def dot(self, no):
        result = (self.x * no.x) + (self.y * no.y) + (self.z * no.z)
        return result
    def cross(self, no):
        result = Points(0.0,0.0,0.0)
        result.x = ((self.y * no.z) - (self.z * no.y))
        result.y = ((self.z * no.x) - (self.x * no.z))
        result.z = ((self.x * no.y) - (self.y * no.x))
        return result
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)


if __name__ == '__main__':
    x, y, z = map(float, input().split())
    A = Points(x, y ,z)
    x, y, z = map(float, input().split())
    B = Points(x, y, z)
    x, y, z = map(float, input().split())
    C = Points(x, y, z)
    x, y, z = map(float, input().split())
    D = Points(x, y, z)

    X = (B - A).cross(C - B)
    Y = (C - B).cross(D - C)
    result = Points.dot(X,Y) / (Points.absolute(X) * Points.absolute(Y))
    result = math.acos(result)


    print(f"%.2f" % math.degrees(result))

