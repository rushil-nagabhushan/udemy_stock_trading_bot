# encoding: utf-8

# Creating a class for stock objects that we will use in other functions.

class Stock:

    def __init__(self,name='INIT'):
        self.name = name
        self.currentPrice = 0
        self.direction = ''

    def set_name(self,name):
        self.name = name
