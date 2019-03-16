from pygame import *
import random

FPS = 8
WIN_WIDTH = 1250
WIN_HEIGHT = 650
SIZE_OF_CELL = 50
COLOR_OF_FIELD = (200, 240, 200)
DEFEAT = False

init()
mainSurface = display.set_mode((WIN_WIDTH, WIN_HEIGHT))         #главное окно
clock = time.Clock()

mainSurface.fill(COLOR_OF_FIELD)

display.set_caption('Snake')        #название окна

#клетка поля
field = Surface((SIZE_OF_CELL, SIZE_OF_CELL))
field.fill(COLOR_OF_FIELD)

#шрифты и текст
text = font.Font(None, WIN_HEIGHT//10)
smallText = font.Font(None, 30)
gameOver = text.render('Game over', 1, (0, 0, 5))
placeOfGameOver = gameOver.get_rect(center = (WIN_WIDTH//2, WIN_HEIGHT//2))

class Snake:

    def __init__(self):

        #координаты головы, хвоста, длина

        self.head = [WIN_WIDTH//(2 * SIZE_OF_CELL), WIN_HEIGHT//(2 * SIZE_OF_CELL)]
        self.tail = [WIN_WIDTH//(2 * SIZE_OF_CELL), WIN_HEIGHT//(2 * SIZE_OF_CELL) + 1]
        self.length = 2

        #наличие в клетке с координатами змеи

        self.location = [[0] * (WIN_WIDTH//SIZE_OF_CELL) for i in range(WIN_HEIGHT//SIZE_OF_CELL)]
        self.location[self.head[1]][self.head[0]] = 1
        self.location[self.tail[1]][self.tail[0]] = 1

        #направление движения элемента змеи

        self.next = [['NULL'] * (WIN_WIDTH // SIZE_OF_CELL) for i in range(WIN_HEIGHT // SIZE_OF_CELL)]
        self.next[self.head[1]][self.head[0]] = 'UP'
        self.next[self.tail[1]][self.tail[0]] = 'UP'

        #змея в окне

        #внешний вид тела

        self.body_look = Surface((SIZE_OF_CELL, SIZE_OF_CELL))
        self.body_look.fill(COLOR_OF_FIELD)

        self.head_look = Surface((SIZE_OF_CELL, SIZE_OF_CELL))
        self.head_look.fill(COLOR_OF_FIELD)
        draw.circle(self.body_look, (255, 0, 70), (SIZE_OF_CELL//2, SIZE_OF_CELL//2), SIZE_OF_CELL//2)
        draw.circle(self.body_look, (0, 0, 0), (SIZE_OF_CELL//2, SIZE_OF_CELL//2), SIZE_OF_CELL//2, 3)
        draw.circle(self.head_look, (0, 0, 0), (SIZE_OF_CELL//2, SIZE_OF_CELL//2), SIZE_OF_CELL//2)

        r1 = Rect((WIN_WIDTH//(2 * SIZE_OF_CELL)) * SIZE_OF_CELL, (WIN_HEIGHT//(2 * SIZE_OF_CELL)) * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL)
        r2 = Rect((WIN_WIDTH//(2 * SIZE_OF_CELL)) * SIZE_OF_CELL, (WIN_HEIGHT//(2 * SIZE_OF_CELL)) * SIZE_OF_CELL + SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL)

        mainSurface.blit(self.head_look, r1)
        mainSurface.blit(self.body_look, r2)

        display.update(r1.union(r2))


    #перемещение змеи на одну клетку

    def move(self):

        self.moveHead()
        self.moveTail()

        r = Rect(self.head[0] * SIZE_OF_CELL, self.head[1] * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL)

        mainSurface.blit(self.head_look, r)

        display.update(r)


    def moveHead(self):

        if (self.next[self.head[1]][self.head[0]] == 'UP'):

            #если змея уперлась в стенку или в себя

            if (self.location[(self.head[1] - 1) % (WIN_HEIGHT//SIZE_OF_CELL)][self.head[0]] == 1):

                mainSurface.blit(gameOver, placeOfGameOver)
                score = text.render('Your score: {}'.format(s.length), 1, (0, 0, 5))
                placeOfScore = score.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 + 100))
                mainSurface.blit(score, placeOfScore)
                display.update(placeOfGameOver)
                display.update(placeOfScore)
                while True:

                    for i in event.get():

                        if (i.type == QUIT):

                            exit()

                        elif (i.type == KEYDOWN and i.key == K_SPACE) or (i.type == MOUSEBUTTONDOWN):

                            RunGame()

            #если можно переместиться

            else:

                #перемещаем голову

                r = Rect(self.head[0] * SIZE_OF_CELL, self.head[1] * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL)

                mainSurface.blit(self.body_look, r)

                display.update(r)

                self.head[1] -= 1
                self.head[1] %= (WIN_HEIGHT//SIZE_OF_CELL)
                self.location[self.head[1]][self.head[0]] = 1
                self.next[self.head[1]][self.head[0]] = 'UP'

        elif (self.next[self.head[1]][self.head[0]] == 'DOWN'):

            # если змея уперлась в стенку или в себя

            if (self.location[(self.head[1] + 1) % (WIN_HEIGHT//SIZE_OF_CELL)][self.head[0]] == 1):

                mainSurface.blit(gameOver, placeOfGameOver)
                score = text.render('Your score: {}'.format(s.length), 1, (0, 0, 5))
                placeOfScore = score.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 + 100))
                mainSurface.blit(score, placeOfScore)
                display.update(placeOfGameOver)
                display.update(placeOfScore)
                while True:

                    for i in event.get():

                        if (i.type == QUIT):

                            exit()

                        elif (i.type == KEYDOWN and i.key == K_SPACE) or (i.type == MOUSEBUTTONDOWN):

                            RunGame()

            # если можно переместиться

            else:

                # перемещаем голову

                r = Rect(self.head[0] * SIZE_OF_CELL, self.head[1] * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL)

                mainSurface.blit(self.body_look, r)

                display.update(r)

                self.head[1] += 1
                self.head[1] %= (WIN_HEIGHT//SIZE_OF_CELL)
                self.location[self.head[1]][self.head[0]] = 1
                self.next[self.head[1]][self.head[0]] = 'DOWN'

        elif (self.next[self.head[1]][self.head[0]] == 'RIGHT'):

            # если змея уперлась в стенку или в себя

            if (self.location[self.head[1]][(self.head[0] + 1) % (WIN_WIDTH//SIZE_OF_CELL)] == 1):

                mainSurface.blit(gameOver, placeOfGameOver)
                score = text.render('Your score: {}'.format(s.length), 1, (0, 0, 5))
                placeOfScore = score.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 + 100))
                mainSurface.blit(score, placeOfScore)
                display.update(placeOfGameOver)
                display.update(placeOfScore)
                while True:

                    for i in event.get():

                        if (i.type == QUIT):

                            exit()

                        elif (i.type == KEYDOWN and i.key == K_SPACE) or (i.type == MOUSEBUTTONDOWN):

                            RunGame()

            # если можно переместиться

            else:

                # перемещаем голову

                r = Rect(self.head[0] * SIZE_OF_CELL, self.head[1] * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL)

                mainSurface.blit(self.body_look, r)

                display.update(r)

                self.head[0] += 1
                self.head[0] %= (WIN_WIDTH//SIZE_OF_CELL)
                self.location[self.head[1]][self.head[0]] = 1
                self.next[self.head[1]][self.head[0]] = 'RIGHT'

        elif (self.next[self.head[1]][self.head[0]] == 'LEFT'):

            # если змея уперлась в стенку или в себя

            if (self.location[self.head[1]][(self.head[0] - 1) % (WIN_WIDTH//SIZE_OF_CELL)] == 1):

                mainSurface.blit(gameOver, placeOfGameOver)
                score = text.render('Your score: {}'.format(s.length), 1, (0, 0, 5))
                placeOfScore = score.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 + 100))
                mainSurface.blit(score, placeOfScore)
                display.update(placeOfGameOver)
                display.update(placeOfScore)
                while True:

                    for i in event.get():

                        if (i.type == QUIT):

                            exit()

                        elif (i.type == KEYDOWN and i.key == K_SPACE) or (i.type == MOUSEBUTTONDOWN):

                            RunGame()

            # если можно переместиться

            else:

                # перемещаем голову

                r = Rect(self.head[0] * SIZE_OF_CELL, self.head[1] * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL)

                mainSurface.blit(self.body_look, r)

                display.update(r)

                self.head[0] -= 1
                self.head[0] %= (WIN_WIDTH//SIZE_OF_CELL)
                self.location[self.head[1]][self.head[0]] = 1
                self.next[self.head[1]][self.head[0]] = 'LEFT'



    def moveTail(self):

        if (self.next[self.tail[1]][self.tail[0]] == 'UP'):

            r = Rect(self.tail[0] * SIZE_OF_CELL, self.tail[1] * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL)

            mainSurface.blit(field, r)

            display.update(r)

            self.next[self.tail[1]][self.tail[0]] = 'NULL'
            self.location[self.tail[1]][self.tail[0]] = 0
            self.tail[1] -= 1
            self.tail[1] %= (WIN_HEIGHT // SIZE_OF_CELL)


        elif (self.next[self.tail[1]][self.tail[0]] == 'DOWN'):

            r = Rect(self.tail[0] * SIZE_OF_CELL, self.tail[1] * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL)

            mainSurface.blit(field, r)

            display.update(r)

            self.next[self.tail[1]][self.tail[0]] = 'NULL'
            self.location[self.tail[1]][self.tail[0]] = 0
            self.tail[1] += 1
            self.tail[1] %= (WIN_HEIGHT // SIZE_OF_CELL)

        elif (self.next[self.tail[1]][self.tail[0]] == 'RIGHT'):

            r = Rect(self.tail[0] * SIZE_OF_CELL, self.tail[1] * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL)

            mainSurface.blit(field, r)

            display.update(r)

            self.next[self.tail[1]][self.tail[0]] = 'NULL'
            self.location[self.tail[1]][self.tail[0]] = 0
            self.tail[0] += 1
            self.tail[0] %= (WIN_WIDTH // SIZE_OF_CELL)

        elif (self.next[self.tail[1]][self.tail[0]] == 'LEFT'):

            r = Rect(self.tail[0] * SIZE_OF_CELL, self.tail[1] * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL)

            mainSurface.blit(field, r)

            display.update(r)

            self.next[self.tail[1]][self.tail[0]] = 'NULL'
            self.location[self.tail[1]][self.tail[0]] = 0
            self.tail[0] -= 1
            self.tail[0] %= (WIN_WIDTH // SIZE_OF_CELL)


    #увеличение длины на единицу

    def increase(self):

        self.moveHead()

        self.length += 1

        r = Rect(self.head[0] * SIZE_OF_CELL, self.head[1] * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL)

        mainSurface.blit(self.head_look, r)

        display.update(r)


class Food:
    def __init__(self):

        #выбираем случайные координаты, чтобы еда не оказалоась на змее

        x, y = random.randint(0, WIN_WIDTH//SIZE_OF_CELL - 1), random.randint(0, WIN_HEIGHT//SIZE_OF_CELL - 1)

        while (s.location[y][x] == 1):
            x, y = random.randint(0, WIN_WIDTH//SIZE_OF_CELL - 1), random.randint(0, WIN_HEIGHT//SIZE_OF_CELL - 1)

        self.x = x
        self.y = y

        #отображаем еду

        self.look = Surface((SIZE_OF_CELL, SIZE_OF_CELL))
        self.look.fill(COLOR_OF_FIELD)
        draw.line(self.look, (50, 200, 20), (0, 0), (SIZE_OF_CELL, SIZE_OF_CELL), 15)
        draw.line(self.look, (50, 200, 20), (0, SIZE_OF_CELL), (SIZE_OF_CELL, 0), 15)

        mainSurface.blit(self.look, Rect(self.x * SIZE_OF_CELL, self.y * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL))

        display.update(Rect(self.x * SIZE_OF_CELL, self.y * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL))


s = Snake()

def RunGame():

    mainSurface.fill(COLOR_OF_FIELD)

    global s

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

    mainSurface.fill(COLOR_OF_FIELD)

    f = Food()

    #главный цикл
    while True:

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

        else:

            s.move()

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
        if ((s.next[s.head[1]][s.head[0]] == 'LEFT' and s.location[s.head[1]][(s.head[0] - 1) % (WIN_WIDTH//SIZE_OF_CELL)] == 1)
                or (s.next[s.head[1]][s.head[0]] == 'UP' and s.location[(s.head[1] - 1) % (WIN_HEIGHT//SIZE_OF_CELL)][s.head[0]] == 1)
                or (s.next[s.head[1]][s.head[0]] == 'RIGHT' and s.location[s.head[1]][(s.head[0] + 1) % (WIN_WIDTH//SIZE_OF_CELL)] == 1)
                or (s.next[s.head[1]][s.head[0]] == 'DOWN' and s.location[(s.head[1] + 1) % (WIN_HEIGHT//SIZE_OF_CELL)][s.head[0]] == 1)):

            clock.tick(FPS - 3)

        else:

            clock.tick(FPS)

#запуск игры
RunGame()