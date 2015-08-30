# module to draw things with tkinter

from tkinter import *
import board_properties as Config
import consts as Consts

DEBUG = False


def get_instance():
    ''' Returns a Tkinter instance for future Tkinter calls '''
    return Tk()


def clickHandler(event, pBoard):
    if DEBUG:
        print('click at x : (%d), y : (%d)' % (event.x, event.y))
    scaledPoint = scaleGraphicToBoard((event.x, event.y))
    if DEBUG:
        print('stupid scale, x : (%d), y : (%d)' % (scaledPoint[0],
                                                    scaledPoint[1]))
    pBoard.setFrame(scaledPoint[0], scaledPoint[1])


def keyboardHandler(event):
#    if DEBUG:
    print('keystroke pressed : ', repr(event.char))


def updateHandler(pInstance, pWindow, pBoard):
    if DEBUG:
        print('update')
    draw_board(pWindow, pBoard)
    attachUpdater(pInstance, pWindow, pBoard)


def get_window(pInstance, pBoard):
    ''' Returns a canvas object to draw on '''
    canvas = Canvas(pInstance, width=Config.WIDTH, height=Config.HEIGHT)
    canvas.bind('<Key>', keyboardHandler)
    canvas.bind('<ButtonPress-1>',
                lambda event, board=pBoard: clickHandler(event, board))
    canvas.pack()
    return canvas


def attachUpdater(pInstance, pWindow, pBoard):
    pInstance.after(Consts.TK_UPDATE_TIMER, updateHandler,
                    pInstance, pWindow, pBoard)


def attachMainloop(pInstance):
    ''' Calls Tkinter mainloop() function '''
    pInstance.mainloop()


def scaleBoardToGraphic(pPoint):
    if len(pPoint) == 2:
        for i in range(2):
            if not isinstance(pPoint[i], int):
                raise Exception('bad point format')
        return ((pPoint[0] * Config.WIDTH) / 3,
                (pPoint[1] * Config.HEIGHT) / 3)


def scaleGraphicToBoard(pPoint):
    if len(pPoint) == 2:
        for i in range(2):
            if (not isinstance(pPoint[i], int)
                    and not isinstance(pPoint[i], float)):
                raise Exception('bad point format')
        return (int((pPoint[0] / Config.WIDTH) * 3),
                int((pPoint[1] / Config.HEIGHT * 3)))


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

def draw_circle(pWindow, pX, pY):
    sPoint = scaleBoardToGraphic((pX, pY))
    ePoint = scaleBoardToGraphic((pX + 1, pY + 1))
    if DEBUG:
        print('CIRCLE:: start point : {}, end point : {}'.format(sPoint,
                                                                 ePoint))
    pWindow.create_oval(sPoint[0],
                        sPoint[1],
                        ePoint[0],
                        ePoint[1],
                        outline=Consts.TK_COLOR_BLACK,
                        fill=Consts.TK_BG_COLOR,
                        width=2)

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
                elif frame == Consts.BOA_P2_REPR:
                    draw_circle(pWindow, x, y)
    return
