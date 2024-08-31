import math

class Polygon:
    def __init__(self, *sides_tuple):
        self.num_sides = len(sides_tuple)
        self.sides_list = list(sides_tuple)
    
    def input_ploygon(self, *sides_tuple):
        self.num_sides = len(sides_tuple)
        sides_list = list(sides_tuple)
    
    def set_sides_Num(self,num_sides):
        self.num_sides = num_sides
        
    def set_sides(self, *sides_tuple):
        sides_list = list(sides_tuple)
    
class Triangle(Polygon):
    def __init__(self, *sides_tuple):
        super().__init__(*sides_tuple)
        
    def input_triangle(self, *sides_tuple):
        super().__init__(*sides_tuple)
        
    def triangle_area(self):
        sides_sum = sum(self.sides_list) 
        s = sides_sum/2
        area = s * (s-self.sides_list[0]) * (s-self.sides_list[1]) * (s-self.sides_list[2])
        return math.sqrt(area)

obj = Triangle(3,4,5)
print(obj.triangle_area())

