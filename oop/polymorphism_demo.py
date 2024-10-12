# polymorphism_demo.py
import math

# Base class
class Shape:
    def area(self):
        """Method to calculate the area of the shape. Should be overridden by subclasses."""
        raise NotImplementedError("Subclass must implement this method")

# Derived class for Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize the rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle."""
        return self.length * self.width

# Derived class for Circle
class Circle(Shape):
    def __init__(self, radius):
        """Initialize the circle with radius."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * (self.radius ** 2)
