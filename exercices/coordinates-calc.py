import math

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

        # Get X and Y axis
        self.axis_x1 = self.point1[0]
        self.axis_y1 = self.point1[1]
        self.axis_x2 = self.point2[0]
        self.axis_y2 = self.point2[1]

    def get_distance(self):
        distance = math.sqrt((self.axis_x2 - self.axis_x1) ** 2 + (self.axis_y2 - self.axis_y1) ** 2)

        return distance

    def get_slope(self):
        slope = (self.axis_y2 - self.axis_y1) / (self.axis_x2 - self.axis_x1)

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
