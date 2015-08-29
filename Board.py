'''
Board class using bit field array in order to store game data
'''

import consts as Consts
import array

# temporary tests waiting for a event manager
from random import randint


class Board(object):

    def __init__(self):
        self.field = array.array(Consts.BOA_FIELD_TYPECODE)
        self.height = Consts.BOA_HEIGHT
        self.width = Consts.BOA_HEIGHT
        self.__ResetBoard()

    def __del__(self):
        pass

    def __ResetBoard(self):
        for y in range(self.height):
            for x in range(self.width):
                self.field.append(0)

        # temporary tests waiting for a event manager
        self.setFrame(randint(0, 2), randint(0, 2), Consts.BOA_P1_REPR)
        self.setFrame(randint(0, 2), randint(0, 2), Consts.BOA_P1_REPR)
        self.setFrame(randint(0, 2), randint(0, 2), Consts.BOA_P1_REPR)
        self.setFrame(randint(0, 2), randint(0, 2), Consts.BOA_P1_REPR)

    def getFrame(self, pX, pY):
        return self.field[self.__TransformCoords(pX, pY)]

    def setFrame(self, pX, pY, pValue):
        localFrame = self.field[self.__TransformCoords(pX, pY)]
        if localFrame == Consts.BOA_EMPTY_REPR:
            self.field[self.__TransformCoords(pX, pY)] = pValue

    def __TransformCoords(self, pX, pY):
        return (pY * self.width) + pX

    @property
    def field(self):
        return self.__field

    @field.setter
    def field(self, pValue):
        self.__field = pValue

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, pValue):
        self.__height = pValue

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, pValue):
        self.__width = pValue
