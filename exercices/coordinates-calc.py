import math

class Line():
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

        # Get X and Y axis
        self.x1, self.y1 = self.point1
        self.x2, self.y2 = self.point2

    def get_distance(self):
        distance = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)

        return distance

    def get_slope(self):
        slope = (self.y2 - self.y1) / (self.x2 - self.x1)

        return slope

point1 = (3, 2)
point2 = (8, 10)
line = Line(point1, point2)

print('Coordinates given:')
print('------------------')
print(f'Point 1: X is {point1[0]}, and Y is {point1[1]}')
print(f'Point 2: X is {point2[0]}, and Y is {point2[1]}')

print(f'\nThe distance between these coordinates is {line.get_distance()}')
print(f'The slope of these coordinates is {line.get_slope()}')
