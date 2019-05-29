from pygame import *
import random
import snake
from food import *

WIN_WIDTH = 1250  # wigth of window
WIN_HEIGHT = 650  # height of window
SIZE_OF_CELL = 50
COLOUR_OF_FIELD = (200, 240, 200)
DEFEAT = False
FPS = 8
FIELD = []

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

NumOfPlayers = False

class Game:
    def run(self):
        '''
        This function starts the game
        '''
        global NumOfPlayers, WIN_WIDTH, WIN_HEIGHT, SIZE_OF_CELL, COLOUR_OF_FIELD, DEFEAT

        NumOfPlayers = self.NumOfPlayersChoose()

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

        mode = self.modeChoose(placeOfEasyButton, placeOfMediumButton, placeOfHardButton)

        def OnePlayerGame(acceleration=False):
            '''
            This function starts the game for one player
            :param acceleration: True, if snake moves with acceleration
            '''
            global DEFEAT
            DEFEAT = False
            self.update_field()

            mainSurface.fill(COLOUR_OF_FIELD)

            # barriers (for hard mode)
            if (mode == 3):
                self.drawBarriers(1)

            s = snake.Snake()

            # title "Press ... to start"
            self.PressToStartTitle()

            self.startGame()

            mainSurface.fill(COLOUR_OF_FIELD)

            # barriers (for hard mode)
            if (mode == 3):
                self.drawBarriers(1)

            f = Food()

            game.FPS = 8

            # main loop
            while not DEFEAT:

                for i in event.get():

                    if i.type == QUIT:

                        exit()

                    elif (i.type == KEYDOWN):  # changing direction of snake

                        if s.handleKeyPressuresOnePlayer(i.key):

                            break

                if s.checkSnakeFoundFood(f, acceleration):

                    f = Food()

                if DEFEAT:

                    s.PrintGameOver()

                    self.restartGame()

                    break

                # score update

                self.scoreUpdate(s, f)

                # delay

                self.delay(s)

        def TwoPlayersGame(acceleration=False):
            '''
            This function starts the game for two players
            :param acceleration: True, if snakes moves with acceleration
            '''
            global DEFEAT
            DEFEAT = False
            self.update_field()

            mainSurface.fill(COLOUR_OF_FIELD)

            # barriers (for hard mode)
            if (mode == 3):
                self.drawBarriers()

            sRight = snake.Snake(x_coord=(WIN_WIDTH // SIZE_OF_CELL) * 3 // 4)
            sLeft = snake.Snake(x_coord=(WIN_WIDTH // SIZE_OF_CELL) // 4, colour=(70, 0, 255))

            # title "Press ... to start"
            self.PressToStartTitle()

            self.startGame()

            mainSurface.fill(COLOUR_OF_FIELD)

            # barriers (for hard mode)
            if (mode == 3):
                self.drawBarriers()

            f = Food()

            game.FPS = 8

            # main loop
            while not DEFEAT:

                leftMove = False
                rightMove = False

                for i in event.get():

                    if i.type == QUIT:

                        exit()

                    elif (i.type == KEYDOWN):  # changing direction of snake

                        rightMove = sRight.handleKeyPressuresRight(i.key, rightMove)
                        leftMove = sLeft.handleKeyPressuresLeft(i.key, leftMove)

                    if (rightMove and leftMove):
                        break

                if sRight.checkSnakeFoundFood(f, acceleration):
                    f = Food()

                if DEFEAT:

                    sRight.PrintGameOver()
                    sLeft.PrintGameOver()

                    self.restartGame()

                    break

                if sLeft.checkSnakeFoundFood(f, acceleration):
                    f = Food()

                if DEFEAT:

                    sRight.PrintGameOver()
                    sLeft.PrintGameOver()

                    self.restartGame()

                    break

                # score update

                self.scoreUpadateTwoPlayers(sRight, sLeft, f)

                # delay
                clock.tick(game.FPS)

        # game start

        while True:
            if (NumOfPlayers == 1):

                OnePlayerGame(acceleration=(mode > 1))

            else:

                TwoPlayersGame(acceleration=(mode > 1))

    def scoreUpdate(self, s, food):
        '''
        Updaye score on screen
        :param s: snake
        :param food: food
        '''

        for i in range(3):
            mainSurface.blit(field, Rect(i * SIZE_OF_CELL, 0, 0, 0))
            display.update(Rect(i * SIZE_OF_CELL, 0, 0, 0))

        for i in range(3):

            if (s.location[0][i] == 1):

                if (s.head == [i, 0]):

                    mainSurface.blit(s.head_look, Rect(i * SIZE_OF_CELL, 0, 0, 0))

                else:

                    mainSurface.blit(s.body_look, Rect(i * SIZE_OF_CELL, 0, 0, 0))

            elif (food.x_coord == i and food.y_coord == 0):

                mainSurface.blit(food.look, Rect(i * SIZE_OF_CELL, 0, 0, 0))

        score = smallText.render('Score: {}'.format(s.length), 1, (0, 0, 30))
        placeOfScore = score.get_rect()
        mainSurface.blit(score, placeOfScore)
        display.update(placeOfScore)

    def delay(self, s):
        '''
        Delay of game loop
        :param s: snake
        '''

        # if snake is nearby any barrier
        if ((s.next[s.head[1]][s.head[0]] == 'LEFT' and FIELD[s.head[1]][
            (s.head[0] - 1) % (WIN_WIDTH // SIZE_OF_CELL)])
                or (s.next[s.head[1]][s.head[0]] == 'UP' and
                    FIELD[(s.head[1] - 1) % (WIN_HEIGHT // SIZE_OF_CELL)][s.head[0]])
                or (s.next[s.head[1]][s.head[0]] == 'RIGHT' and FIELD[s.head[1]][
                    (s.head[0] + 1) % (WIN_WIDTH // SIZE_OF_CELL)])
                or (s.next[s.head[1]][s.head[0]] == 'DOWN' and
                    FIELD[(s.head[1] + 1) % (WIN_HEIGHT // SIZE_OF_CELL)][s.head[0]])):

            clock.tick(FPS - 3)

        else:

            clock.tick(FPS)

    def drawBarriers(self, d=0):
        '''
        Drawing of barriers
        :param d: 1, if one player
        '''

        for i in [5, (WIN_WIDTH // (2 * SIZE_OF_CELL) + d), (WIN_WIDTH // SIZE_OF_CELL) - 6]:

            for j in [(WIN_HEIGHT // (2 * SIZE_OF_CELL)) + 3, (WIN_HEIGHT // (2 * SIZE_OF_CELL)) - 3]:
                barrier = Surface((SIZE_OF_CELL, SIZE_OF_CELL))
                barrier.fill(COLOUR_OF_FIELD)
                draw.line(barrier, (70, 70, 70), (0, 0), (SIZE_OF_CELL, SIZE_OF_CELL), 15)
                draw.line(barrier, (70, 70, 70), (0, SIZE_OF_CELL), (SIZE_OF_CELL, 0), 15)
                draw.line(barrier, (70, 70, 70), (0, SIZE_OF_CELL // 2), (SIZE_OF_CELL, SIZE_OF_CELL // 2), 15)
                draw.line(barrier, (70, 70, 70), (SIZE_OF_CELL // 2, SIZE_OF_CELL), (SIZE_OF_CELL // 2, 0), 15)

                FIELD[j][i] = 1

                mainSurface.blit(barrier, Rect(i * SIZE_OF_CELL, j * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL))
                display.update(Rect(i * SIZE_OF_CELL, j * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL))

    def PressToStartTitle(self):
        '''
        Drawing of title 'Press ... to start'
        :return:
        '''

        PressToStart = game.text.render('Press SPACE or click to start', 1, (50, 100, 100))
        placeOfPressToStart = PressToStart.get_rect(center=(game.WIN_WIDTH // 2, game.WIN_HEIGHT // 2))
        game.mainSurface.blit(PressToStart, placeOfPressToStart)
        display.update(placeOfPressToStart)

    def scoreUpadateTwoPlayers(self, sRight, sLeft, f):
        '''
        Update score fo two players
        :param sRight: right snake
        :param sLeft: left snake
        :param f: food
        '''

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

            elif (f.x_coord == i and f.y_coord == 0):

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

            elif (f.x_coord == (WIN_WIDTH // SIZE_OF_CELL - i - 1) and f.y_coord == 0):

                mainSurface.blit(f.look, Rect((WIN_WIDTH // SIZE_OF_CELL - i - 1) * SIZE_OF_CELL, 0, 0, 0))

        score = smallText.render('Score: {}'.format(sRight.length), 1, (0, 0, 30))
        placeOfScore = score.get_rect(x=(WIN_WIDTH // SIZE_OF_CELL - 3) * SIZE_OF_CELL + 65)
        mainSurface.blit(score, placeOfScore)
        display.update(placeOfScore)

    def restartGame(self):
        '''
        Restarting game
        '''

        restartedGame = False
        while not restartedGame:

            for i in event.get():

                if ((i.type == KEYDOWN and i.key == K_SPACE) or i.type == MOUSEBUTTONDOWN):
                    restartedGame = True
                    break

                elif (i.type == QUIT):
                    exit()

    def startGame(self):
        '''
        Start the game
        '''

        gameStarted = False

        while not gameStarted:

            for i in event.get():

                if i.type == QUIT:

                    exit()

                elif ((i.type == KEYDOWN and i.key == K_SPACE) or (i.type == MOUSEBUTTONDOWN)):

                    gameStarted = True
                    break

    def NumOfPlayersChoose(self):
        '''
        Choose the number of players
        :return: number of players
        '''

        NumOfPlayers = False

        while not NumOfPlayers:

            for i in event.get():

                if i.type == QUIT:
                    exit()

                elif (i.type == MOUSEBUTTONDOWN and placeOfOnePlayerButton.collidepoint(i.pos)):

                    NumOfPlayers = 1
                    break

                elif (i.type == MOUSEBUTTONDOWN and placeOfTwoPlayersButton.collidepoint(i.pos)):

                    NumOfPlayers = 2
                    break

        return NumOfPlayers

    def modeChoose(self, placeOfEasyButton, placeOfMediumButton, placeOfHardButton):
        '''
        Choose the mode
        :param placeOfEasyButton: plcae of button 'Easy'
        :param placeOfMediumButton: place of button 'Medium'
        :param placeOfHardButton: place of button 'Hard'
        :return: mode
        '''

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

        return mode

    def update_field(self):
        '''
        This function fills the field with zero
        '''
        global FIELD
        FIELD = [[0] * (game.WIN_WIDTH // game.SIZE_OF_CELL) for i in range(game.WIN_HEIGHT // game.SIZE_OF_CELL)]
