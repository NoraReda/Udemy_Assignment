class Shape():
    def what_am_i(self):
       print('I am a shape')

class Rectangle(Shape):
    pass

rectangle = Rectangle()
rectangle.what_am_i


class Square(Shape):
    pass

square =  Square()
square.what_am_i
