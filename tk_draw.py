# module to draw things with tkinter

from tkinter import *
import board_properties as Config
import consts as Consts

DEBUG = True


def get_instance():
    ''' Returns a Tkinter instance for future Tkinter calls '''
    return Tk()


def get_window(pInstance):
    ''' Returns a canvas object to draw on '''
    canvas = Canvas(pInstance, width=Config.WIDTH, height=Config.HEIGHT)
    canvas.pack()
    return canvas


def do_mainloop():
    ''' Calls Tkinter mainloop() function '''
    mainloop()
    return


def scaleBoardToGraphic(pPoint):
    if len(pPoint) == 2:
        for i in range(2):
            if not isinstance(pPoint[i], int):
                raise Exception('bad point format')
        return ((pPoint[0] * Config.WIDTH) / 3,
                (pPoint[1] * Config.HEIGHT) / 3)


def draw_cross(pWindow, pX, pY):
    sPoint = scaleBoardToGraphic((pX, pY))
    ePoint = scaleBoardToGraphic((pX + 1, pY + 1))
    if DEBUG:
        print('FIRST LINE:: start point : {}, end point : {}'.format(sPoint,
                                                                     ePoint))
    pWindow.create_line(sPoint[0], sPoint[1], ePoint[0], ePoint[1])

    sPoint = scaleBoardToGraphic((pX + 1, pY))
    ePoint = scaleBoardToGraphic((pX, pY + 1))
    if DEBUG:
        print('SECOND LINE:: start point : {}, end point : {}'.format(sPoint,
                                                                      ePoint))
    pWindow.create_line(sPoint[0], sPoint[1], ePoint[0], ePoint[1])

def draw_board(pWindow, pBoard):
    '''
    Draws the board in the canvas on the window
    Ghost is red, pacman is yellow, path taken is pink
    P1 repr is a cross, P2 repr is a circle
    '''

    pWindow.create_rectangle(0, 0,
                             Config.WIDTH, Config.HEIGHT,
                             fill=Consts.TK_BG_COLOR)

    for i in range(pBoard.height - 1):
        yCustom = (Config.HEIGHT * (i + 1)) / 3
        pWindow.create_line(0, yCustom,
                            Config.WIDTH, yCustom,
                            fill=Consts.TK_BG_STICKS_COLOR)

    for i in range(pBoard.width - 1):
        xCustom = (Config.WIDTH * (i + 1)) / 3
        pWindow.create_line(xCustom, 0,
                            xCustom, Config.HEIGHT,
                            fill=Consts.TK_BG_STICKS_COLOR)

    for y in range(pBoard.height):
        for x in range(pBoard.width):
            frame = pBoard.getFrame(x, y)
            if frame in Consts.BOA_VALID_REPR:
                if frame == Consts.BOA_P1_REPR:
                    draw_cross(pWindow, x, y)
                    # call function to draw a cross
                    pass
                elif frame == Consts.BOA_P2_REPR:
                    # call function to draw a circle
                    pass
    return
