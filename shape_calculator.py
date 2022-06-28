class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width**2 + self.height**2)**0.5

    def get_picture(self):
        pic = ''
        if self.width < 50 and self.height < 50:
            for i in range(self.height):
                pic += '*' * self.width + '\n'
            return pic
        else:
            return 'Too big for picture.'

    def get_amount_inside(self,s):
           area1=self.get_area()
           area2=s.get_area()
           return area1//area2


    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        Rectangle.__init__(self, side, side)

    def set_side(self, side):
        self.side = side
        super().__init__(side, side)
        super().set_width(side)
        super().set_height(side)
    def   set_width(self,side):
            self.side=side
            Rectangle.set_width(self,side)
    def set_height(self,side):
             self.side=side
             Rectangle.height(sel,side)
    def __str__(self):
        return f'Square(side={self.side})'
