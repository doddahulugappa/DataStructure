"""
The Interface Segregation Principle (ISP)
states that a client should not be exposed to methods it doesn't need.
"""

from abc import ABC, abstractmethod


class Movable(ABC):
    @abstractmethod
    def go(self):
        pass


class Flyable(Movable):
    @abstractmethod
    def fly(self):
        pass


class Aircraft(Flyable):
    def go(self):
        print("Flight is Taxiing")

    def fly(self):
        print("Flight is Flying")


class Car(Movable):
    def go(self):
        print("Car is Going")


if __name__ == "__main__":
    car = Car()
    car.go()

    aircraft = Aircraft()
    aircraft.go()
    aircraft.fly()
