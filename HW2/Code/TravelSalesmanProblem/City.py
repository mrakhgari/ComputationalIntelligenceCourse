import math


class City:
    '''
        each city in this problem saved in this class with (x,y) coordinate.
    '''

    def __init__(self, index, x=0, y=0):
        self.index = index
        self.x = x
        self.y = y

    def __repr__(self):
        self.__str__()

    def __str__(self):
        return str(self.index) + '-> (' + str(self.x) + ', ' + str(self.y) + ')'

    # calculate distance of another city with this city

    def distance(self, other):
        return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
