from abc import ABC, abstractmethod

class Figure(ABC): #abstract class
  @abstractmethod
  def area(self): #abstract method
    pass

  @abstractmethod
  def perimter(self):
    pass

class Square(Figure): #inheritance
    def __init__(self, l):  # constructor
        self.l = l

    def area(self):
        return self.l * self.l

    def perimter(self):
        return 4 * self.l

class Rectangle(Figure):

    def __init__(self, l, L):
        self.l = l
        self.L = L

    def area(self):
        return self.l* self.L
    def perimter(self):
        return 2*self.l + 2*self.L

square = Square(5)
rectangle = Rectangle(10,5)

print("Square object is %s" % square.l)

print("Rectangle object is %s" % rectangle) # print the memory location

print(f"Square area is {square.area()}")

#TODO
# 1. Print square perimeter
# 2. Print rectangle area, perimeter
# 3. Print square and rectangle atributes

print(f"The square perimeter is: {square.perimter()}")

print(f"Rectangle area is {rectangle.area()} and perimeter is: {rectangle.perimter()}")

print(f"Square attibut is: {square.l} and Rectangle attributes are: {rectangle.l} and {rectangle.L}")

