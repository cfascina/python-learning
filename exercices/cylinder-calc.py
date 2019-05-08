import math

class Cylinder:

    pi = math.pi

    def __init__(self, height = 1, radius = 1):
        self.height = height
        self.radius = radius

    def get_volume(self):
        volume = Cylinder.pi * (self.radius ** 2) * self.height

        return volume

    def get_surface_area(self):
        base_area = Cylinder.pi * (self.radius ** 2)
        lateral_area = 2 * Cylinder.pi * self.radius * self.height
        surface_area = (2 * base_area) + lateral_area

        return surface_area

cylinder = Cylinder(2, 3)

print(f'Data given')
print(f'----------')
print(f'Cylinder height: {cylinder.height}')
print(f'Cylinder radius: {cylinder.radius}')

print(f'\nThe cylinder volume is {cylinder.get_volume()}')
print(f'The cylinder surface area is {cylinder.get_surface_area()}')
