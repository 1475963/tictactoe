'''
Board class using bit field array in order to store game data
'''

import consts as Consts
import array
from random import sample

DEBUG = False


class Board(object):

    def __init__(self):
        self.turn = sample(Consts.BOA_VALID_REPR[1:], 1)[0]
        self.field = array.array(Consts.BOA_FIELD_TYPECODE)
        self.height = Consts.BOA_HEIGHT
        self.width = Consts.BOA_HEIGHT
        self.__ResetBoard()

    def __del__(self):
        pass

    def __ResetBoard(self):
        for y in range(self.height):
            for x in range(self.width):
                self.field.append(Consts.BOA_EMPTY_REPR)

    def getFrame(self, pX, pY):
        return self.field[self.__TransformCoords(pX, pY)]

    def setFrame(self, pX, pY):
        localFrame = self.field[self.__TransformCoords(pX, pY)]
        if localFrame == Consts.BOA_EMPTY_REPR:
            self.field[self.__TransformCoords(pX, pY)] = self.turn
            if self.checkWinnance(pX, pY):
                winner = 'VOID LOL'
                if self.turn == Consts.BOA_P1_REPR:
                    winner = 'P1 - CROSS'
                elif self.turn == Consts.BOA_P2_REPR:
                    winner = 'P2 - CIRCLE'
                raise Exception('ALLER CHAMPION (%s) A GAGNER' % winner)
            self.fireNextTurn()

    def checkWinnance(self, pX, pY):
        def adjustX(self, pX):
            return pX % self.width

        def adjustY(self, pY):
            return pY % self.height

        if ((self.getFrame(pX, pY) == self.getFrame(adjustX(self, pX + 1), pY)
                 and self.getFrame(pX, pY) == self.getFrame(adjustX(self, pX - 1), pY))
            or (self.getFrame(pX, pY) == self.getFrame(pX, adjustY(self, pY + 1))
                and self.getFrame(pX, pY) == self.getFrame(pX, adjustY(self, pY - 1)))
            or (self.getFrame(pX, pY) == self.getFrame(adjustX(self, pX + 1), adjustY(self, pY + 1))
                and self.getFrame(pX, pY) == self.getFrame(adjustX(self, pX - 1), adjustY(self, pY - 1)))
            or (self.getFrame(pX, pY) == self.getFrame(adjustX(self, pX + 1), adjustY(self, pY - 1))
                and self.getFrame(pX, pY) == self.getFrame(adjustX(self, pX - 1), adjustY(self, pY + 1)))):
            return True
        if not any(True if elem == Consts.BOA_EMPTY_REPR else False for elem in self.field):
            raise Exception('TIE BREAKER BOYS')
        return False

    def fireNextTurn(self):
        players = Consts.BOA_VALID_REPR[1:]
        try:
            if DEBUG:
                print('players : ', players)
                print('turn : ', self.turn)
            currentFoundAt = players.index(self.turn)
            if DEBUG:
                print('current : ', currentFoundAt)
            self.turn = players[(currentFoundAt + 1) % len(players)]
        except Exception:
            print('currentPlayerNotFound !!!')

    def __TransformCoords(self, pX, pY):
        return (pY * self.width) + pX

    @property
    def turn(self):
        return self.__turn

    @turn.setter
    def turn(self, pValue):
        self.__turn = pValue

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
