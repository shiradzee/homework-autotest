class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = self.calculate_area()
    def calculate_area(self):
        return self.width * self.height
    def __eq__(self, rec):
        return self.width == rec.width and self.height == rec.height
    def __lt__(self, rec):
        return self.width < rec.width and self.height < rec.height
    def __le__(self, rec):
        return self.width <= rec.width and self.height <= rec.height
    def __gt__(self, rec):
        return self.width > rec.width and self.height > rec.height
    def __ge__(self, rec):
        return self.width >= rec.width and self.height >= rec.height
rectangle1 = Rectangle(1, 1)
rectangle2 = Rectangle(2, 2)
rectangle3 = Rectangle(2, 2)
print(rectangle1 == rectangle2)
print(rectangle2 == rectangle3)
print(rectangle1 < rectangle2)
print(rectangle2 < rectangle3)
print(rectangle2 <= rectangle3)