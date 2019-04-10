from pygame import *
import random
import snake
import my_field
from food import *

WIN_WIDTH = 1250  # wigth of window
WIN_HEIGHT = 650  # height of window
SIZE_OF_CELL = 50
COLOUR_OF_FIELD = (200, 240, 200)
DEFEAT = False

init()
mainSurface = display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # main window
clock = time.Clock()

mainSurface.fill(COLOUR_OF_FIELD)

display.set_caption('Snake')  # name of window

# cell of field

field = Surface((SIZE_OF_CELL, SIZE_OF_CELL))
field.fill(COLOUR_OF_FIELD)

# font and text
text = font.Font(None, WIN_HEIGHT // 10)
smallText = font.Font(None, 30)

display.update()

# buttons
OnePlayerButton = text.render('One player', 1, (50, 100, 100), (0, 240, 200))
placeOfOnePlayerButton = OnePlayerButton.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 - 100))
mainSurface.blit(OnePlayerButton, placeOfOnePlayerButton)
TwoPlayersButton = text.render('Two players', 1, (50, 100, 100), (220, 220, 220))
placeOfTwoPlayersButton = TwoPlayersButton.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 + 100))
mainSurface.blit(TwoPlayersButton, placeOfTwoPlayersButton)
display.update()

NumOfPalyers = False

def run():
    '''
    This function starts the game
    :return:
    '''
    global NumOfPalyers, WIN_WIDTH, WIN_HEIGHT, SIZE_OF_CELL, COLOUR_OF_FIELD, DEFEAT

    while not NumOfPalyers:

        for i in event.get():

            if i.type == QUIT:
                exit()

            elif (i.type == MOUSEBUTTONDOWN and placeOfOnePlayerButton.collidepoint(i.pos)):

                NumOfPalyers = 1
                break

            elif (i.type == MOUSEBUTTONDOWN and placeOfTwoPlayersButton.collidepoint(i.pos)):

                NumOfPalyers = 2
                break

    # buttons
    mainSurface.fill(COLOUR_OF_FIELD)

    EasyButton = text.render('Easy', 1, (50, 100, 100), (0, 240, 200))
    placeOfEasyButton = EasyButton.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 - 150))
    mainSurface.blit(EasyButton, placeOfEasyButton)
    MediumButton = text.render('Medium', 1, (50, 100, 100), (0, 240, 200))
    placeOfMediumButton = MediumButton.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))
    mainSurface.blit(MediumButton, placeOfMediumButton)
    HardButton = text.render('Hard', 1, (50, 100, 100), (0, 240, 200))
    placeOfHardButton = HardButton.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 + 150))
    mainSurface.blit(HardButton, placeOfHardButton)
    display.update()

    mode = False
    while not mode:

        for i in event.get():

            if i.type == QUIT:
                exit()

            elif (i.type == MOUSEBUTTONDOWN and placeOfEasyButton.collidepoint(i.pos)):

                mode = 1
                break

            elif (i.type == MOUSEBUTTONDOWN and placeOfMediumButton.collidepoint(i.pos)):

                mode = 2
                break

            elif (i.type == MOUSEBUTTONDOWN and placeOfHardButton.collidepoint(i.pos)):

                mode = 3
                break

    def OnePlayerGame(acceleration=False):
        '''
        This function starts the game for one player
        :param acceleration:
        :return:
        '''
        global DEFEAT
        DEFEAT = False
        my_field.update_field()

        mainSurface.fill(COLOUR_OF_FIELD)

        # barriers (for hard mode)
        if (mode == 3):

            for i in [5, (WIN_WIDTH // (2 * SIZE_OF_CELL)) + 1, (WIN_WIDTH // SIZE_OF_CELL) - 6]:

                for j in [(WIN_HEIGHT // (2 * SIZE_OF_CELL)) + 3, (WIN_HEIGHT // (2 * SIZE_OF_CELL)) - 3]:
                    barrier = Surface((SIZE_OF_CELL, SIZE_OF_CELL))
                    barrier.fill(COLOUR_OF_FIELD)
                    draw.line(barrier, (70, 70, 70), (0, 0), (SIZE_OF_CELL, SIZE_OF_CELL), 15)
                    draw.line(barrier, (70, 70, 70), (0, SIZE_OF_CELL), (SIZE_OF_CELL, 0), 15)
                    draw.line(barrier, (70, 70, 70), (0, SIZE_OF_CELL // 2), (SIZE_OF_CELL, SIZE_OF_CELL // 2), 15)
                    draw.line(barrier, (70, 70, 70), (SIZE_OF_CELL // 2, SIZE_OF_CELL), (SIZE_OF_CELL // 2, 0), 15)

                    my_field.FIELD[j][i] = 1

                    mainSurface.blit(barrier, Rect(i * SIZE_OF_CELL, j * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL))

                    display.update(Rect(i * SIZE_OF_CELL, j * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL))

        s = snake.Snake()

        # title "Press ... to start"
        PressToStart = text.render('Press SPACE or click to start', 1, (50, 100, 100))
        placeOfPressToStart = PressToStart.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))
        mainSurface.blit(PressToStart, placeOfPressToStart)
        display.update(placeOfPressToStart)

        gameStarted = False

        while not gameStarted:

            for i in event.get():

                if i.type == QUIT:

                    exit()

                elif ((i.type == KEYDOWN and i.key == K_SPACE) or (i.type == MOUSEBUTTONDOWN)):

                    gameStarted = True
                    break

        mainSurface.fill(COLOUR_OF_FIELD)

        # barriers (for hard mode)
        if (mode == 3):

            for i in [5, (WIN_WIDTH // (2 * SIZE_OF_CELL)) + 1, (WIN_WIDTH // SIZE_OF_CELL) - 6]:

                for j in [(WIN_HEIGHT // (2 * SIZE_OF_CELL)) + 3, (WIN_HEIGHT // (2 * SIZE_OF_CELL)) - 3]:
                    barrier = Surface((SIZE_OF_CELL, SIZE_OF_CELL))
                    barrier.fill(COLOUR_OF_FIELD)
                    draw.line(barrier, (70, 70, 70), (0, 0), (SIZE_OF_CELL, SIZE_OF_CELL), 15)
                    draw.line(barrier, (70, 70, 70), (0, SIZE_OF_CELL), (SIZE_OF_CELL, 0), 15)
                    draw.line(barrier, (70, 70, 70), (0, SIZE_OF_CELL // 2), (SIZE_OF_CELL, SIZE_OF_CELL // 2), 15)
                    draw.line(barrier, (70, 70, 70), (SIZE_OF_CELL // 2, SIZE_OF_CELL), (SIZE_OF_CELL // 2, 0), 15)

                    my_field.FIELD[j][i] = 1

                    mainSurface.blit(barrier, Rect(i * SIZE_OF_CELL, j * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL))

                    display.update(Rect(i * SIZE_OF_CELL, j * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL))

        f = Food()

        FPS = 8

        # main loop
        while not DEFEAT:

            for i in event.get():

                if i.type == QUIT:

                    exit()

                elif (i.type == KEYDOWN):  # changing direction of snake

                    if ((i.key == K_UP or i.key == K_w) and (s.next[s.head[1]][s.head[0]] != 'DOWN') and
                            s.next[s.head[1]][s.head[0]] != 'UP'):

                        s.next[s.head[1]][s.head[0]] = 'UP'

                        break

                    elif ((i.key == K_DOWN or i.key == K_s) and s.next[s.head[1]][s.head[0]] != 'UP' and
                          s.next[s.head[1]][s.head[0]] != 'DOWN'):

                        s.next[s.head[1]][s.head[0]] = 'DOWN'

                        break

                    elif ((i.key == K_RIGHT or i.key == K_d) and s.next[s.head[1]][s.head[0]] != 'LEFT' and
                          s.next[s.head[1]][s.head[0]] != 'RIGHT'):

                        s.next[s.head[1]][s.head[0]] = 'RIGHT'

                        break

                    elif ((i.key == K_LEFT or i.key == K_a) and s.next[s.head[1]][s.head[0]] != 'RIGHT' and
                          s.next[s.head[1]][s.head[0]] != 'LEFT'):

                        s.next[s.head[1]][s.head[0]] = 'LEFT'

                        break

            if (s.head == [f.x, f.y]):  # if snake finds a food

                f = Food()
                s.increase()

                if (acceleration):
                    FPS *= FPS
                    FPS += 2
                    FPS = FPS ** 0.5

            else:

                s.move()

            if DEFEAT:

                s.PrintGameOver()

                restartGame = False
                while not restartGame:

                    for i in event.get():

                        if ((i.type == KEYDOWN and i.key == K_SPACE) or i.type == MOUSEBUTTONDOWN):
                            restartGame = True
                            break

                        elif (i.type == QUIT):
                            exit()

                break

            # score update

            for i in range(3):
                mainSurface.blit(field, Rect(i * SIZE_OF_CELL, 0, 0, 0))
                display.update(Rect(i * SIZE_OF_CELL, 0, 0, 0))

            for i in range(3):

                if (s.location[0][i] == 1):

                    if (s.head == [i, 0]):

                        mainSurface.blit(s.head_look, Rect(i * SIZE_OF_CELL, 0, 0, 0))

                    else:

                        mainSurface.blit(s.body_look, Rect(i * SIZE_OF_CELL, 0, 0, 0))

                elif (f.x == i and f.y == 0):

                    mainSurface.blit(f.look, Rect(i * SIZE_OF_CELL, 0, 0, 0))

            score = smallText.render('Score: {}'.format(s.length), 1, (0, 0, 30))
            placeOfScore = score.get_rect()
            mainSurface.blit(score, placeOfScore)
            display.update(placeOfScore)

            # delay

            # if snake is nearby any barrier
            if ((s.next[s.head[1]][s.head[0]] == 'LEFT' and my_field.FIELD[s.head[1]][
                (s.head[0] - 1) % (WIN_WIDTH // SIZE_OF_CELL)])
                    or (s.next[s.head[1]][s.head[0]] == 'UP' and
                        my_field.FIELD[(s.head[1] - 1) % (WIN_HEIGHT // SIZE_OF_CELL)][s.head[0]])
                    or (s.next[s.head[1]][s.head[0]] == 'RIGHT' and my_field.FIELD[s.head[1]][
                        (s.head[0] + 1) % (WIN_WIDTH // SIZE_OF_CELL)])
                    or (s.next[s.head[1]][s.head[0]] == 'DOWN' and
                        my_field.FIELD[(s.head[1] + 1) % (WIN_HEIGHT // SIZE_OF_CELL)][s.head[0]])):

                clock.tick(FPS - 3)

            else:

                clock.tick(FPS)

    def TwoPlayersGame(acceleration=False):
        '''
        This function starts the game for two players
        :param acceleration:
        :return:
        '''
        global DEFEAT
        DEFEAT = False
        my_field.update_field()

        mainSurface.fill(COLOUR_OF_FIELD)

        # barriers (for hard mode)
        if (mode == 3):

            for i in [5, (WIN_WIDTH // (2 * SIZE_OF_CELL)), (WIN_WIDTH // SIZE_OF_CELL) - 6]:

                for j in [(WIN_HEIGHT // (2 * SIZE_OF_CELL)) + 3, (WIN_HEIGHT // (2 * SIZE_OF_CELL)) - 3]:
                    barrier = Surface((SIZE_OF_CELL, SIZE_OF_CELL))
                    barrier.fill(COLOUR_OF_FIELD)
                    draw.line(barrier, (70, 70, 70), (0, 0), (SIZE_OF_CELL, SIZE_OF_CELL), 15)
                    draw.line(barrier, (70, 70, 70), (0, SIZE_OF_CELL), (SIZE_OF_CELL, 0), 15)
                    draw.line(barrier, (70, 70, 70), (0, SIZE_OF_CELL // 2), (SIZE_OF_CELL, SIZE_OF_CELL // 2), 15)
                    draw.line(barrier, (70, 70, 70), (SIZE_OF_CELL // 2, SIZE_OF_CELL), (SIZE_OF_CELL // 2, 0), 15)

                    my_field.FIELD[j][i] = 1

                    mainSurface.blit(barrier, Rect(i * SIZE_OF_CELL, j * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL))

                    display.update(Rect(i * SIZE_OF_CELL, j * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL))

        sRight = snake.Snake(x=(WIN_WIDTH // SIZE_OF_CELL) * 3 // 4)
        sLeft = snake.Snake(x=(WIN_WIDTH // SIZE_OF_CELL) // 4, colour=(70, 0, 255))

        # title "Press ... to start"
        PressToStart = text.render('Press SPACE or click to start', 1, (50, 100, 100))
        placeOfPressToStart = PressToStart.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))
        mainSurface.blit(PressToStart, placeOfPressToStart)
        display.update(placeOfPressToStart)

        gameStarted = False

        while not gameStarted:

            for i in event.get():

                if i.type == QUIT:

                    exit()

                elif ((i.type == KEYDOWN and i.key == K_SPACE) or (i.type == MOUSEBUTTONDOWN)):

                    gameStarted = True
                    break

        mainSurface.fill(COLOUR_OF_FIELD)

        # barriers (for hard mode)
        if (mode == 3):

            for i in [5, (WIN_WIDTH // (2 * SIZE_OF_CELL)), (WIN_WIDTH // SIZE_OF_CELL) - 6]:

                for j in [(WIN_HEIGHT // (2 * SIZE_OF_CELL)) + 3, (WIN_HEIGHT // (2 * SIZE_OF_CELL)) - 3]:
                    barrier = Surface((SIZE_OF_CELL, SIZE_OF_CELL))
                    barrier.fill(COLOUR_OF_FIELD)
                    draw.line(barrier, (70, 70, 70), (0, 0), (SIZE_OF_CELL, SIZE_OF_CELL), 15)
                    draw.line(barrier, (70, 70, 70), (0, SIZE_OF_CELL), (SIZE_OF_CELL, 0), 15)
                    draw.line(barrier, (70, 70, 70), (0, SIZE_OF_CELL // 2), (SIZE_OF_CELL, SIZE_OF_CELL // 2), 15)
                    draw.line(barrier, (70, 70, 70), (SIZE_OF_CELL // 2, SIZE_OF_CELL), (SIZE_OF_CELL // 2, 0), 15)

                    my_field.FIELD[j][i] = 1

                    mainSurface.blit(barrier, Rect(i * SIZE_OF_CELL, j * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL))

                    display.update(Rect(i * SIZE_OF_CELL, j * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL))

        f = Food()

        FPS = 8

        leftMove = False
        rightMove = False

        # main loop
        while not DEFEAT:

            leftMove = False
            rightMove = False

            for i in event.get():

                if i.type == QUIT:

                    exit()

                elif (i.type == KEYDOWN):  # changing direction of snake

                    if ((i.key == K_UP) and (sRight.next[sRight.head[1]][sRight.head[0]] != 'DOWN')
                            and sRight.next[sRight.head[1]][sRight.head[0]] != 'UP' and not rightMove):

                        sRight.next[sRight.head[1]][sRight.head[0]] = 'UP'
                        rightMove = True

                    elif ((i.key == K_DOWN) and sRight.next[sRight.head[1]][sRight.head[0]] != 'UP'
                          and sRight.next[sRight.head[1]][sRight.head[0]] != 'DOWN' and not rightMove):

                        sRight.next[sRight.head[1]][sRight.head[0]] = 'DOWN'
                        rightMove = True

                    elif ((i.key == K_RIGHT) and sRight.next[sRight.head[1]][sRight.head[0]] != 'LEFT'
                          and sRight.next[sRight.head[1]][sRight.head[0]] != 'RIGHT' and not rightMove):

                        sRight.next[sRight.head[1]][sRight.head[0]] = 'RIGHT'
                        rightMove = True

                    elif ((i.key == K_LEFT) and sRight.next[sRight.head[1]][sRight.head[0]] != 'RIGHT'
                          and sRight.next[sRight.head[1]][sRight.head[0]] != 'LEFT' and not rightMove):

                        sRight.next[sRight.head[1]][sRight.head[0]] = 'LEFT'
                        rightMove = True

                    elif ((i.key == K_w) and (sLeft.next[sLeft.head[1]][sLeft.head[0]] != 'DOWN')
                          and sLeft.next[sLeft.head[1]][sLeft.head[0]] != 'UP' and not leftMove):

                        sLeft.next[sLeft.head[1]][sLeft.head[0]] = 'UP'
                        leftMove = True

                    elif ((i.key == K_s) and sLeft.next[sLeft.head[1]][sLeft.head[0]] != 'UP'
                          and sLeft.next[sLeft.head[1]][sLeft.head[0]] != 'DOWN' and not leftMove):

                        sLeft.next[sLeft.head[1]][sLeft.head[0]] = 'DOWN'
                        leftMove = True

                    elif ((i.key == K_d) and sLeft.next[sLeft.head[1]][sLeft.head[0]] != 'LEFT' and
                          sLeft.next[sLeft.head[1]][sLeft.head[0]] != 'RIGHT' and not leftMove):

                        sLeft.next[sLeft.head[1]][sLeft.head[0]] = 'RIGHT'
                        leftMove = True

                    elif ((i.key == K_a) and sLeft.next[sLeft.head[1]][sLeft.head[0]] != 'RIGHT' and
                          sLeft.next[sLeft.head[1]][sLeft.head[0]] != 'LEFT' and not leftMove):

                        sLeft.next[sLeft.head[1]][sLeft.head[0]] = 'LEFT'
                        leftMove = True

                if (rightMove and leftMove):
                    break

            if (sRight.head == [f.x, f.y]):  # if snake finds a food

                f = Food()
                sRight.increase()

                if (acceleration):
                    FPS *= FPS
                    FPS += 2
                    FPS = FPS ** 0.5

            else:

                sRight.move()

            if DEFEAT:

                sRight.PrintGameOver()
                sLeft.PrintGameOver()

                restartGame = False
                while not restartGame:

                    for i in event.get():

                        if ((i.type == KEYDOWN and i.key == K_SPACE) or i.type == MOUSEBUTTONDOWN):

                            restartGame = True
                            break

                        elif (i.type == QUIT):
                            exit()

                break

            if (sLeft.head == [f.x, f.y]):  # if snake finds a food

                f = Food()
                sLeft.increase()

                if (acceleration):
                    FPS *= FPS
                    FPS += 2
                    FPS = FPS ** 0.5

            else:

                sLeft.move()

            if DEFEAT:

                sRight.PrintGameOver()
                sLeft.PrintGameOver()

                restartGame = False
                while not restartGame:

                    for i in event.get():

                        if ((i.type == KEYDOWN and i.key == K_SPACE) or i.type == MOUSEBUTTONDOWN):
                            restartGame = True
                            break

                        elif (i.type == QUIT):
                            exit()

                break

            # score update

            for i in range(3):
                mainSurface.blit(field, Rect(i * SIZE_OF_CELL, 0, 0, 0))
                display.update(Rect(i * SIZE_OF_CELL, 0, 0, 0))

            for i in range(3):

                if (sRight.location[0][i] == 1):

                    if (sRight.head == [i, 0]):

                        mainSurface.blit(sRight.head_look, Rect(i * SIZE_OF_CELL, 0, 0, 0))

                    else:

                        mainSurface.blit(sRight.body_look, Rect(i * SIZE_OF_CELL, 0, 0, 0))

                elif (sLeft.location[0][i] == 1):

                    if (sLeft.head == [i, 0]):

                        mainSurface.blit(sLeft.head_look, Rect(i * SIZE_OF_CELL, 0, 0, 0))

                    else:

                        mainSurface.blit(sLeft.body_look, Rect(i * SIZE_OF_CELL, 0, 0, 0))

                elif (f.x == i and f.y == 0):

                    mainSurface.blit(f.look, Rect(i * SIZE_OF_CELL, 0, 0, 0))

            score = smallText.render('Score: {}'.format(sLeft.length), 1, (0, 0, 30))
            placeOfScore = score.get_rect()
            mainSurface.blit(score, placeOfScore)
            display.update(placeOfScore)

            for i in range(3):
                mainSurface.blit(field, Rect((WIN_WIDTH // SIZE_OF_CELL - i) * SIZE_OF_CELL + 65, 0, 0, 0))
                display.update(Rect((WIN_WIDTH // SIZE_OF_CELL - i) * SIZE_OF_CELL + 65, 0, 0, 0))

            for i in range(3):

                if (sRight.location[0][(WIN_WIDTH // SIZE_OF_CELL) - i - 1] == 1):

                    if (sRight.head == [(WIN_WIDTH // SIZE_OF_CELL - i - 1), 0]):

                        mainSurface.blit(sRight.head_look,
                                         Rect((WIN_WIDTH // SIZE_OF_CELL - i - 1) * SIZE_OF_CELL, 0, 0, 0))

                    else:

                        mainSurface.blit(sRight.body_look,
                                         Rect((WIN_WIDTH // SIZE_OF_CELL - i - 1) * SIZE_OF_CELL, 0, 0, 0))

                elif (sLeft.location[0][(WIN_WIDTH // SIZE_OF_CELL - i - 1)] == 1):

                    if (sLeft.head == [(WIN_WIDTH // SIZE_OF_CELL - i - 1), 0]):

                        mainSurface.blit(sLeft.head_look,
                                         Rect((WIN_WIDTH // SIZE_OF_CELL - i - 1) * SIZE_OF_CELL, 0, 0, 0))

                    else:

                        mainSurface.blit(sLeft.body_look,
                                         Rect((WIN_WIDTH // SIZE_OF_CELL - i - 1) * SIZE_OF_CELL, 0, 0, 0))

                elif (f.x == (WIN_WIDTH // SIZE_OF_CELL - i - 1) and f.y == 0):

                    mainSurface.blit(f.look, Rect((WIN_WIDTH // SIZE_OF_CELL - i - 1) * SIZE_OF_CELL, 0, 0, 0))

            score = smallText.render('Score: {}'.format(sRight.length), 1, (0, 0, 30))
            placeOfScore = score.get_rect(x=(WIN_WIDTH // SIZE_OF_CELL - 3) * SIZE_OF_CELL + 65)
            mainSurface.blit(score, placeOfScore)
            display.update(placeOfScore)

            # delay
            clock.tick(FPS)

    # game start

    while True:
        if (NumOfPalyers == 1):

            OnePlayerGame(acceleration=(mode > 1))

        else:

            TwoPlayersGame(acceleration=(mode > 1))