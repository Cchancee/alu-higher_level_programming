#!/usr/bin/python3
'''Defining the class Square'''


class Square():
    '''Definition of class here'''
    def __init__(self, size):
        if not isinstance(size, int):
              raise TypeError("size must be an integer")
        elif size < 0:
              raise ValueError("size must be >= 0")
        self.__size = size

    def size(self):
        return self.__size

    def size(self, value):
        self.__size = value

    def area(self):
        return (self.__size * self.__size)
