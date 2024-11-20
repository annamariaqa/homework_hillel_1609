from abc import ABC, abstractmethod 

class Figure(ABC):
    def __init__(self, side_a, side_b, side_c, height_len):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.height_len = height_len

    @abstractmethod
    def figure_area(self):
        pass
    
    @abstractmethod
    def figure_perimeter(self):
        pass


class Triangle(Figure):

    def figure_area(self):
        area = 1/2 * self.side_a * self.height_len
        return area

    def figure_perimeter(self):
        perimeter = self.side_a + self.side_b + self.side_c
        return perimeter
    
class Square(Figure):

    def figure_area(self):
        area = self.side_a * self.side_a
        return area
    def figure_perimeter(self):
        perimeter = 4 * self.side_a
        return perimeter
class Rectangle(Figure):

    def figure_area(self):
        area = self.side_a * self.side_b
        return area
    def figure_perimeter(self):
        perimeter = 2 * (self.side_a + self.side_b)
        return perimeter


triangle_a = Triangle(side_a=4, side_b=8, side_c=8, height_len=6)
square_b = Square(side_a=12, side_b=0, side_c=0, height_len=0)
rectangle_c = Rectangle(side_a=10, side_b=4, side_c=0, height_len=0)

for figure in [triangle_a, square_b, rectangle_c]:
    print(figure.figure_area())      
    print(figure.figure_perimeter())  
    print('-'*80)

