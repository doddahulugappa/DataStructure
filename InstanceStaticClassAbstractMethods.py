from abc import ABC, abstractmethod


class Polygon(ABC):
    @abstractmethod
    def number_of_sides(self, obj):
        pass


class Rectangle(Polygon):
    name = "Rectangle"

    def __init__(self):
        self.obj = ""

    def number_of_sides(self, obj):
        self.obj = obj
        print(f"{self.obj} have 2 sides inside instance methods")

    @staticmethod
    def info():
        print("inside the Square class static method")
        Rectangle.info_class_name()

    @classmethod
    def info_class_name(cls):
        print(cls.name, "Class Method executed")


if __name__ == "__main__":
    rectangle = Rectangle()
    rectangle.number_of_sides("Rectangle")
    rectangle.info()
    # rectangle.info_class_name()
