#!/usr/bin/python3
'''Define class'''


class Square():
        '''This is class definition'''
        def __init__(self, size=0):
              '''Defining constructor'''

              '''Validating the private instance attribute'''
              if not isinstance(size, int):
                 raise TypeError("size must be an integer")
              elif size < 0:
                  raise ValueError("size must be >= 0")
              self.__size = size
