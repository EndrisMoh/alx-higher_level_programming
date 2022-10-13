#!/usr/bin/python3
"""
This is the "Square"  module.

This module provides a simple Square class with initialize size.
Defaults size to 0. Raise error on invalid size inputs.
Methods Getter and Setter properties for size.
Method area returns size of area of the square.
Methods allow comparisons between Square objects and their sizes.
"""


class Square():
    '''
        Defining a Square
    '''
    def __init__(self, size=0):
        '''Initialization of instance attributes
            Args: size (int): Zero or positve number.
        '''
        self.size = size

    def area(self):
        '''Calculates the area
            Return: The current square area.
        '''
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        '''Updating the private attributes
            Args: value (int): Zero or positve number.
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __lt__(self, other):
        '''
            less than <
        '''
        return (self.area() < other.area())

    def __le__(self, other):
        '''
            less or equal than <=
        '''
        return (self.area() <= other.area())

    def __eq__(self, other):
        '''
            equal to ==
        '''
        return (self.area() == other.area())

    def __ge__(self, other):
        '''
            greater or equal than >=
        '''
        return (self.area() >= other.area())

    def __gt__(self, other):
        '''
            greater than >
        '''
        return (self.area() > other.area())

    def __ne__(self, other):
        '''
            not equal !=
        '''
        return (self.area() != other.area())
