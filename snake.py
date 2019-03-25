from pygame import *
import random


WIN_WIDTH = 1250        #ширина окна
WIN_HEIGHT = 650        #высота окна
SIZE_OF_CELL = 50       #размер клетки
FIELD = [[0] * (WIN_WIDTH//SIZE_OF_CELL) for i in range(WIN_HEIGHT//SIZE_OF_CELL)]      #поле
COLOUR_OF_FIELD = (200, 240, 200)
DEFEAT = False

init()
mainSurface = display.set_mode((WIN_WIDTH, WIN_HEIGHT))         #главное окно
clock = time.Clock()

mainSurface.fill(COLOUR_OF_FIELD)

display.set_caption('Snake')        #название окна

#клетка поля
field = Surface((SIZE_OF_CELL, SIZE_OF_CELL))
field.fill(COLOUR_OF_FIELD)

#шрифты и текст
text = font.Font(None, WIN_HEIGHT//10)
smallText = font.Font(None, 30)

display.update()

class Snake:

    def __init__(self, colour=(255, 0, 70), x=WIN_WIDTH//(2 * SIZE_OF_CELL), y=WIN_HEIGHT//(2 * SIZE_OF_CELL)):

        #координаты головы, хвоста, длина

        self.initial = [x, y]
        self.head = [x, y]
        self.tail = [x, y + 1]
        self.length = 2

        #наличие в клетке с координатами змеи

        self.location = [[0] * (WIN_WIDTH//SIZE_OF_CELL) for i in range(WIN_HEIGHT//SIZE_OF_CELL)]
        self.location[y][x] = 1
        self.location[y + 1][x] = 1
        FIELD[y][x] = 1
        FIELD[y + 1][x] = 1

        #направление движения элемента змеи

        self.next = [['NULL'] * (WIN_WIDTH // SIZE_OF_CELL) for i in range(WIN_HEIGHT // SIZE_OF_CELL)]
        self.next[self.head[1]][self.head[0]] = 'UP'
        self.next[self.tail[1]][self.tail[0]] = 'UP'

        #змея в окне

        #внешний вид тела

        self.body_look = Surface((SIZE_OF_CELL, SIZE_OF_CELL))
        self.body_look.fill(COLOUR_OF_FIELD)

        self.head_look = Surface((SIZE_OF_CELL, SIZE_OF_CELL))
        self.head_look.fill(COLOUR_OF_FIELD)
        draw.circle(self.body_look, colour, (SIZE_OF_CELL//2, SIZE_OF_CELL//2), SIZE_OF_CELL//2)
        draw.circle(self.body_look, (0, 0, 0), (SIZE_OF_CELL//2, SIZE_OF_CELL//2), SIZE_OF_CELL//2, 3)
        draw.circle(self.head_look, (0, 0, 0), (SIZE_OF_CELL//2, SIZE_OF_CELL//2), SIZE_OF_CELL//2)

        r1 = Rect(x * SIZE_OF_CELL, y * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL)
        r2 = Rect(x * SIZE_OF_CELL, (y + 1) * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL)

        mainSurface.blit(self.head_look, r1)
        mainSurface.blit(self.body_look, r2)

        display.update(r1.union(r2))


    #перемещение змеи на одну клетку

    def move(self):

        self.moveHead()
        if not DEFEAT:
            self.moveTail()

        if DEFEAT:
            return

        r = Rect(self.head[0] * SIZE_OF_CELL, self.head[1] * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL)

        mainSurface.blit(self.head_look, r)

        display.update(r)


    def moveHead(self):

        global DEFEAT

        if (self.next[self.head[1]][self.head[0]] == 'UP'):

            #если змея уперлась

            if (FIELD[(self.head[1] - 1) % (WIN_HEIGHT//SIZE_OF_CELL)][self.head[0]] == 1):

                DEFEAT = True

            # если можно переместиться

            else:

                # перемещаем голову

                r = Rect(self.head[0] * SIZE_OF_CELL, self.head[1] * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL)

                mainSurface.blit(self.body_look, r)

                display.update(r)

                self.head[1] -= 1
                self.head[1] %= (WIN_HEIGHT//SIZE_OF_CELL)
                self.location[self.head[1]][self.head[0]] = 1
                FIELD[self.head[1]][self.head[0]] = 1
                self.next[self.head[1]][self.head[0]] = 'UP'

        elif (self.next[self.head[1]][self.head[0]] == 'DOWN'):

            # если змея уперлась

            if (FIELD[(self.head[1] + 1) % (WIN_HEIGHT//SIZE_OF_CELL)][self.head[0]] == 1):

                DEFEAT = True

            # если можно переместиться

            else:

                # перемещаем голову

                r = Rect(self.head[0] * SIZE_OF_CELL, self.head[1] * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL)

                mainSurface.blit(self.body_look, r)

                display.update(r)

                self.head[1] += 1
                self.head[1] %= (WIN_HEIGHT//SIZE_OF_CELL)
                self.location[self.head[1]][self.head[0]] = 1
                FIELD[self.head[1]][self.head[0]] = 1
                self.next[self.head[1]][self.head[0]] = 'DOWN'

        elif (self.next[self.head[1]][self.head[0]] == 'RIGHT'):

            # если змея уперлась

            if (FIELD[self.head[1]][(self.head[0] + 1) % (WIN_WIDTH//SIZE_OF_CELL)] == 1):

                DEFEAT = True

            # если можно переместиться

            else:

                # перемещаем голову

                r = Rect(self.head[0] * SIZE_OF_CELL, self.head[1] * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL)

                mainSurface.blit(self.body_look, r)

                display.update(r)

                self.head[0] += 1
                self.head[0] %= (WIN_WIDTH//SIZE_OF_CELL)
                self.location[self.head[1]][self.head[0]] = 1
                FIELD[self.head[1]][self.head[0]] = 1
                self.next[self.head[1]][self.head[0]] = 'RIGHT'

        elif (self.next[self.head[1]][self.head[0]] == 'LEFT'):

            # если змея уперлась

            if (FIELD[self.head[1]][(self.head[0] - 1) % (WIN_WIDTH//SIZE_OF_CELL)] == 1):

                DEFEAT = True

            # если можно переместиться

            else:

                # перемещаем голову

                r = Rect(self.head[0] * SIZE_OF_CELL, self.head[1] * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL)

                mainSurface.blit(self.body_look, r)

                display.update(r)

                self.head[0] -= 1
                self.head[0] %= (WIN_WIDTH//SIZE_OF_CELL)
                self.location[self.head[1]][self.head[0]] = 1
                FIELD[self.head[1]][self.head[0]] = 1
                self.next[self.head[1]][self.head[0]] = 'LEFT'



    def moveTail(self):

        if (self.next[self.tail[1]][self.tail[0]] == 'UP'):

            r = Rect(self.tail[0] * SIZE_OF_CELL, self.tail[1] * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL)

            mainSurface.blit(field, r)

            display.update(r)

            self.next[self.tail[1]][self.tail[0]] = 'NULL'
            self.location[self.tail[1]][self.tail[0]] = 0
            FIELD[self.tail[1]][self.tail[0]] = 0
            self.tail[1] -= 1
            self.tail[1] %= (WIN_HEIGHT // SIZE_OF_CELL)


        elif (self.next[self.tail[1]][self.tail[0]] == 'DOWN'):

            r = Rect(self.tail[0] * SIZE_OF_CELL, self.tail[1] * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL)

            mainSurface.blit(field, r)

            display.update(r)

            self.next[self.tail[1]][self.tail[0]] = 'NULL'
            self.location[self.tail[1]][self.tail[0]] = 0
            FIELD[self.tail[1]][self.tail[0]] = 0
            self.tail[1] += 1
            self.tail[1] %= (WIN_HEIGHT // SIZE_OF_CELL)

        elif (self.next[self.tail[1]][self.tail[0]] == 'RIGHT'):

            r = Rect(self.tail[0] * SIZE_OF_CELL, self.tail[1] * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL)

            mainSurface.blit(field, r)

            display.update(r)

            self.next[self.tail[1]][self.tail[0]] = 'NULL'
            self.location[self.tail[1]][self.tail[0]] = 0
            FIELD[self.tail[1]][self.tail[0]] = 0
            self.tail[0] += 1
            self.tail[0] %= (WIN_WIDTH // SIZE_OF_CELL)

        elif (self.next[self.tail[1]][self.tail[0]] == 'LEFT'):

            r = Rect(self.tail[0] * SIZE_OF_CELL, self.tail[1] * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL)

            mainSurface.blit(field, r)

            display.update(r)

            self.next[self.tail[1]][self.tail[0]] = 'NULL'
            self.location[self.tail[1]][self.tail[0]] = 0
            FIELD[self.tail[1]][self.tail[0]] = 0
            self.tail[0] -= 1
            self.tail[0] %= (WIN_WIDTH // SIZE_OF_CELL)


    #увеличение длины на единицу

    def increase(self):

        self.moveHead()

        self.length += 1

        r = Rect(self.head[0] * SIZE_OF_CELL, self.head[1] * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL)

        mainSurface.blit(self.head_look, r)

        display.update(r)

    def PrintGameOver(self):

        gameOver = text.render('Game over', 1, (0, 0, 5))
        placeOfGameOver = gameOver.get_rect(center=(self.initial[0] * SIZE_OF_CELL, self.initial[1] * SIZE_OF_CELL))
        mainSurface.blit(gameOver, placeOfGameOver)
        score = text.render('Your score: {}'.format(self.length), 1, (0, 0, 5))
        placeOfScore = score.get_rect(center=(self.initial[0] * SIZE_OF_CELL, self.initial[1] * SIZE_OF_CELL + 100))
        mainSurface.blit(score, placeOfScore)
        display.update(placeOfGameOver)
        display.update(placeOfScore)


class Food:
    def __init__(self):

        #выбираем случайные координаты, чтобы еда не оказалоась на змее

        x, y = random.randint(0, WIN_WIDTH//SIZE_OF_CELL - 1), random.randint(0, WIN_HEIGHT//SIZE_OF_CELL - 1)

        while (FIELD[y][x]):
            x, y = random.randint(0, WIN_WIDTH//SIZE_OF_CELL - 1), random.randint(0, WIN_HEIGHT//SIZE_OF_CELL - 1)

        self.x = x
        self.y = y

        #отображаем еду

        self.look = Surface((SIZE_OF_CELL, SIZE_OF_CELL))
        self.look.fill(COLOUR_OF_FIELD)
        draw.line(self.look, (50, 200, 20), (0, 0), (SIZE_OF_CELL, SIZE_OF_CELL), 15)
        draw.line(self.look, (50, 200, 20), (0, SIZE_OF_CELL), (SIZE_OF_CELL, 0), 15)

        mainSurface.blit(self.look, Rect(self.x * SIZE_OF_CELL, self.y * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL))

        display.update(Rect(self.x * SIZE_OF_CELL, self.y * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL))

# кнопки
OnePlayerButton = text.render('One player', 1, (50, 100, 100), (0, 240, 200))
placeOfOnePlayerButton = OnePlayerButton.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 - 100))
mainSurface.blit(OnePlayerButton, placeOfOnePlayerButton)
TwoPlayersButton = text.render('Two players', 1, (50, 100, 100), (220, 220, 220))
placeOfTwoPlayersButton = TwoPlayersButton.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 + 100))
mainSurface.blit(TwoPlayersButton, placeOfTwoPlayersButton)
display.update()

NumOfPalyers = False

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

# кнопки
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

    global DEFEAT
    DEFEAT = False
    global FIELD
    FIELD = [[0] * (WIN_WIDTH // SIZE_OF_CELL) for i in range(WIN_HEIGHT // SIZE_OF_CELL)]

    mainSurface.fill(COLOUR_OF_FIELD)

    # препятствия (для сложного режима)
    if (mode == 3):

        for i in [5, (WIN_WIDTH // (2 * SIZE_OF_CELL)) + 1, (WIN_WIDTH // SIZE_OF_CELL) - 6]:

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

    s = Snake()

    # надпись "Нажмите ... чтобы начать"
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

    # препятствия (для сложного режима)
    if (mode == 3):

        for i in [5, (WIN_WIDTH // (2 * SIZE_OF_CELL)) + 1, (WIN_WIDTH // SIZE_OF_CELL) - 6]:

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

    f = Food()

    FPS = 8

    #главный цикл
    while not DEFEAT:

        for i in event.get():

            if i.type == QUIT:

                exit()

            elif (i.type == KEYDOWN):       #меняем направление змеи

                if ((i.key == K_UP or i.key == K_w) and (s.next[s.head[1]][s.head[0]] != 'DOWN') and s.next[s.head[1]][s.head[0]] != 'UP'):

                    s.next[s.head[1]][s.head[0]] = 'UP'

                    break

                elif ((i.key == K_DOWN or i.key == K_s) and s.next[s.head[1]][s.head[0]] != 'UP' and s.next[s.head[1]][s.head[0]] != 'DOWN'):

                    s.next[s.head[1]][s.head[0]] = 'DOWN'

                    break

                elif ((i.key == K_RIGHT or i.key == K_d) and s.next[s.head[1]][s.head[0]] != 'LEFT' and s.next[s.head[1]][s.head[0]] != 'RIGHT'):

                    s.next[s.head[1]][s.head[0]] = 'RIGHT'

                    break

                elif ((i.key == K_LEFT or i.key == K_a) and s.next[s.head[1]][s.head[0]] != 'RIGHT' and s.next[s.head[1]][s.head[0]] != 'LEFT'):

                    s.next[s.head[1]][s.head[0]] = 'LEFT'

                    break

        if (s.head == [f.x, f.y]):      #если змея находит еду

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

        #обновление счета

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

        #задержка

        #если вот-вот наткнется
        if ((s.next[s.head[1]][s.head[0]] == 'LEFT' and FIELD[s.head[1]][(s.head[0] - 1) % (WIN_WIDTH//SIZE_OF_CELL)])
                or (s.next[s.head[1]][s.head[0]] == 'UP' and FIELD[(s.head[1] - 1) % (WIN_HEIGHT//SIZE_OF_CELL)][s.head[0]])
                or (s.next[s.head[1]][s.head[0]] == 'RIGHT' and FIELD[s.head[1]][(s.head[0] + 1) % (WIN_WIDTH//SIZE_OF_CELL)])
                or (s.next[s.head[1]][s.head[0]] == 'DOWN' and FIELD[(s.head[1] + 1) % (WIN_HEIGHT//SIZE_OF_CELL)][s.head[0]])):

            clock.tick(FPS - 3)

        else:

            clock.tick(FPS)


def TwoPlayersGame(acceleration=False):
    global DEFEAT
    DEFEAT = False
    global FIELD
    FIELD = [[0] * (WIN_WIDTH // SIZE_OF_CELL) for i in range(WIN_HEIGHT // SIZE_OF_CELL)]

    mainSurface.fill(COLOUR_OF_FIELD)

    # препятствия (для сложного режима)
    if (mode == 3):

        for i in [5, (WIN_WIDTH // (2 * SIZE_OF_CELL)), (WIN_WIDTH // SIZE_OF_CELL) - 6]:

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

    sRight = Snake(x = (WIN_WIDTH//SIZE_OF_CELL) * 3 // 4)
    sLeft = Snake(x=(WIN_WIDTH // SIZE_OF_CELL) // 4, colour=(70, 0, 255))

    # надпись "Нажмите ... чтобы начать"
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

    # препятствия (для сложного режима)
    if (mode == 3):

        for i in [5, (WIN_WIDTH // (2 * SIZE_OF_CELL)), (WIN_WIDTH // SIZE_OF_CELL) - 6]:

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


    f = Food()

    FPS = 8

    leftMove = False
    rightMove = False

    # главный цикл
    while not DEFEAT:

        leftMove = False
        rightMove = False

        for i in event.get():

            if i.type == QUIT:

                exit()

            elif (i.type == KEYDOWN):  # меняем направление змеи

                if ((i.key == K_UP) and (sRight.next[sRight.head[1]][sRight.head[0]] != 'DOWN')
                        and sRight.next[sRight.head[1]][sRight.head[0]] != 'UP' and not rightMove):

                    sRight.next[sRight.head[1]][sRight.head[0]] = 'UP'
                    rightMove = True
                    #break

                elif ((i.key == K_DOWN) and sRight.next[sRight.head[1]][sRight.head[0]] != 'UP'
                      and sRight.next[sRight.head[1]][sRight.head[0]] != 'DOWN' and not rightMove):

                    sRight.next[sRight.head[1]][sRight.head[0]] = 'DOWN'
                    rightMove = True
                    #break

                elif ((i.key == K_RIGHT) and sRight.next[sRight.head[1]][sRight.head[0]] != 'LEFT'
                      and sRight.next[sRight.head[1]][sRight.head[0]] != 'RIGHT' and not rightMove):

                    sRight.next[sRight.head[1]][sRight.head[0]] = 'RIGHT'
                    rightMove = True
                    #break

                elif ((i.key == K_LEFT) and sRight.next[sRight.head[1]][sRight.head[0]] != 'RIGHT'
                      and sRight.next[sRight.head[1]][sRight.head[0]] != 'LEFT' and not rightMove):

                    sRight.next[sRight.head[1]][sRight.head[0]] = 'LEFT'
                    rightMove = True
                    #break

                elif ((i.key == K_w) and (sLeft.next[sLeft.head[1]][sLeft.head[0]] != 'DOWN')
                      and sLeft.next[sLeft.head[1]][sLeft.head[0]] != 'UP' and not leftMove):

                    sLeft.next[sLeft.head[1]][sLeft.head[0]] = 'UP'
                    leftMove = True
                    #break

                elif ((i.key == K_s) and sLeft.next[sLeft.head[1]][sLeft.head[0]] != 'UP'
                      and sLeft.next[sLeft.head[1]][sLeft.head[0]] != 'DOWN' and not leftMove):

                    sLeft.next[sLeft.head[1]][sLeft.head[0]] = 'DOWN'
                    leftMove = True
                    #break

                elif ((i.key == K_d) and sLeft.next[sLeft.head[1]][sLeft.head[0]] != 'LEFT' and
                      sLeft.next[sLeft.head[1]][sLeft.head[0]] != 'RIGHT' and not leftMove):

                    sLeft.next[sLeft.head[1]][sLeft.head[0]] = 'RIGHT'
                    leftMove = True
                    #break

                elif ((i.key == K_a) and sLeft.next[sLeft.head[1]][sLeft.head[0]] != 'RIGHT' and
                      sLeft.next[sLeft.head[1]][sLeft.head[0]] != 'LEFT' and not leftMove):

                    sLeft.next[sLeft.head[1]][sLeft.head[0]] = 'LEFT'
                    leftMove = True
                    #break

            if (rightMove and leftMove):
                break



        if (sRight.head == [f.x, f.y]):  # если змея находит еду

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

        if (sLeft.head == [f.x, f.y]):  # если змея находит еду

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

        # обновление счета

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
            mainSurface.blit(field, Rect((WIN_WIDTH//SIZE_OF_CELL - i) * SIZE_OF_CELL + 65, 0, 0, 0))
            display.update(Rect((WIN_WIDTH//SIZE_OF_CELL - i) * SIZE_OF_CELL + 65, 0, 0, 0))

        for i in range(3):

            if (sRight.location[0][(WIN_WIDTH//SIZE_OF_CELL) - i - 1] == 1):

                if (sRight.head == [(WIN_WIDTH//SIZE_OF_CELL - i - 1), 0]):

                    mainSurface.blit(sRight.head_look, Rect((WIN_WIDTH//SIZE_OF_CELL - i - 1) * SIZE_OF_CELL, 0, 0, 0))

                else:

                    mainSurface.blit(sRight.body_look, Rect((WIN_WIDTH//SIZE_OF_CELL - i - 1) * SIZE_OF_CELL, 0, 0, 0))

            elif (sLeft.location[0][(WIN_WIDTH//SIZE_OF_CELL - i - 1)] == 1):

                if (sLeft.head == [(WIN_WIDTH//SIZE_OF_CELL - i - 1), 0]):

                    mainSurface.blit(sLeft.head_look, Rect((WIN_WIDTH//SIZE_OF_CELL - i - 1) * SIZE_OF_CELL, 0, 0, 0))

                else:

                    mainSurface.blit(sLeft.body_look, Rect((WIN_WIDTH//SIZE_OF_CELL - i - 1) * SIZE_OF_CELL, 0, 0, 0))

            elif (f.x == (WIN_WIDTH//SIZE_OF_CELL - i - 1) and f.y == 0):

                mainSurface.blit(f.look, Rect((WIN_WIDTH//SIZE_OF_CELL - i - 1) * SIZE_OF_CELL, 0, 0, 0))

        score = smallText.render('Score: {}'.format(sRight.length), 1, (0, 0, 30))
        placeOfScore = score.get_rect(x=(WIN_WIDTH//SIZE_OF_CELL - 3) * SIZE_OF_CELL + 65)
        mainSurface.blit(score, placeOfScore)
        display.update(placeOfScore)

        # задержка
        clock.tick(FPS)

#запуск игры

while True:
    if (NumOfPalyers == 1):

        OnePlayerGame(acceleration=(mode > 1))

    else:

        TwoPlayersGame(acceleration=(mode > 1))