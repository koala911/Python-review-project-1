from pygame import *
import random
from game import *
import my_field
from food import *

class Snake:

    def __init__(self, colour=(255, 0, 70), x_coord=WIN_WIDTH // (2 * SIZE_OF_CELL), y_coord=WIN_HEIGHT // (2 * SIZE_OF_CELL)):

        '''
        Constructor of class Snake
        :param colour: colour of snake, tuple of 3 integers (n_1, n_2, n_3), 0 <= n_i <= 255
        :param x_coord: start x coordinate, integer
        :param y_coord: start y coordinate, integer
        '''

        # coordinates of head, tail, length

        self.initial = [x_coord, y_coord]
        self.head = [x_coord, y_coord]
        self.tail = [x_coord, y_coord + 1]
        self.length = 2

        # presence in cell of snake

        self.location = [[0] * (WIN_WIDTH // SIZE_OF_CELL) for i in range(WIN_HEIGHT // SIZE_OF_CELL)]
        self.location[y_coord][x_coord] = 1
        self.location[y_coord + 1][x_coord] = 1
        my_field.FIELD[y_coord][x_coord] = 1
        my_field.FIELD[y_coord + 1][x_coord] = 1

        # direction of move of element of snake

        self.next = [['NULL'] * (WIN_WIDTH // SIZE_OF_CELL) for i in range(WIN_HEIGHT // SIZE_OF_CELL)]
        self.next[self.head[1]][self.head[0]] = 'UP'
        self.next[self.tail[1]][self.tail[0]] = 'UP'

        # look of snake's body

        self.body_look = Surface((SIZE_OF_CELL, SIZE_OF_CELL))
        self.body_look.fill(COLOUR_OF_FIELD)

        self.head_look = Surface((SIZE_OF_CELL, SIZE_OF_CELL))
        self.head_look.fill(COLOUR_OF_FIELD)
        draw.circle(self.body_look, colour, (SIZE_OF_CELL // 2, SIZE_OF_CELL // 2), SIZE_OF_CELL // 2)
        draw.circle(self.body_look, (0, 0, 0), (SIZE_OF_CELL // 2, SIZE_OF_CELL // 2), SIZE_OF_CELL // 2, 3)
        draw.circle(self.head_look, (0, 0, 0), (SIZE_OF_CELL // 2, SIZE_OF_CELL // 2), SIZE_OF_CELL // 2)

        r1 = Rect(x_coord * SIZE_OF_CELL, y_coord * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL)
        r2 = Rect(x_coord * SIZE_OF_CELL, (y_coord + 1) * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL)

        mainSurface.blit(self.head_look, r1)
        mainSurface.blit(self.body_look, r2)

        display.update(r1.union(r2))

    # move of snake on one cell

    def move(self):
        '''
        Moves the snake on one cell
        '''
        self.moveHead()
        if not game.DEFEAT:
            self.moveTail()

        if game.DEFEAT:
            return

        r = Rect(self.head[0] * SIZE_OF_CELL, self.head[1] * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL)

        mainSurface.blit(self.head_look, r)

        display.update(r)

    def moveHead(self):
        '''
        Moves the head on one cell
        '''
        if (self.next[self.head[1]][self.head[0]] == 'UP'):

            # if snake bumped

            if (my_field.FIELD[(self.head[1] - 1) % (WIN_HEIGHT // SIZE_OF_CELL)][self.head[0]] == 1):

                game.DEFEAT = True

            # if snake can move

            else:

                r = Rect(self.head[0] * SIZE_OF_CELL, self.head[1] * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL)

                mainSurface.blit(self.body_look, r)

                display.update(r)

                self.head[1] -= 1
                self.head[1] %= (WIN_HEIGHT // SIZE_OF_CELL)
                self.location[self.head[1]][self.head[0]] = 1
                my_field.FIELD[self.head[1]][self.head[0]] = 1
                self.next[self.head[1]][self.head[0]] = 'UP'

        elif (self.next[self.head[1]][self.head[0]] == 'DOWN'):

            # if snake bumped

            if (my_field.FIELD[(self.head[1] + 1) % (WIN_HEIGHT // SIZE_OF_CELL)][self.head[0]] == 1):

                game.DEFEAT = True

            # if snake can move

            else:

                r = Rect(self.head[0] * SIZE_OF_CELL, self.head[1] * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL)

                mainSurface.blit(self.body_look, r)

                display.update(r)

                self.head[1] += 1
                self.head[1] %= (WIN_HEIGHT // SIZE_OF_CELL)
                self.location[self.head[1]][self.head[0]] = 1
                my_field.FIELD[self.head[1]][self.head[0]] = 1
                self.next[self.head[1]][self.head[0]] = 'DOWN'

        elif (self.next[self.head[1]][self.head[0]] == 'RIGHT'):

            # if snake bumped

            if (my_field.FIELD[self.head[1]][(self.head[0] + 1) % (WIN_WIDTH // SIZE_OF_CELL)] == 1):

                game.DEFEAT = True

            # if snake can move

            else:

                r = Rect(self.head[0] * SIZE_OF_CELL, self.head[1] * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL)

                mainSurface.blit(self.body_look, r)

                display.update(r)

                self.head[0] += 1
                self.head[0] %= (WIN_WIDTH // SIZE_OF_CELL)
                self.location[self.head[1]][self.head[0]] = 1
                my_field.FIELD[self.head[1]][self.head[0]] = 1
                self.next[self.head[1]][self.head[0]] = 'RIGHT'

        elif (self.next[self.head[1]][self.head[0]] == 'LEFT'):

            # if snake bumped

            if (my_field.FIELD[self.head[1]][(self.head[0] - 1) % (WIN_WIDTH // SIZE_OF_CELL)] == 1):

                game.DEFEAT = True

            # if snake can move

            else:

                r = Rect(self.head[0] * SIZE_OF_CELL, self.head[1] * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL)

                mainSurface.blit(self.body_look, r)

                display.update(r)

                self.head[0] -= 1
                self.head[0] %= (WIN_WIDTH // SIZE_OF_CELL)
                self.location[self.head[1]][self.head[0]] = 1
                my_field.FIELD[self.head[1]][self.head[0]] = 1
                self.next[self.head[1]][self.head[0]] = 'LEFT'

    def moveTail(self):
        '''
        Moves the tail on one cell
        '''
        if (self.next[self.tail[1]][self.tail[0]] == 'UP'):

            r = Rect(self.tail[0] * SIZE_OF_CELL, self.tail[1] * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL)

            mainSurface.blit(field, r)

            display.update(r)

            self.next[self.tail[1]][self.tail[0]] = 'NULL'
            self.location[self.tail[1]][self.tail[0]] = 0
            my_field.FIELD[self.tail[1]][self.tail[0]] = 0
            self.tail[1] -= 1
            self.tail[1] %= (WIN_HEIGHT // SIZE_OF_CELL)


        elif (self.next[self.tail[1]][self.tail[0]] == 'DOWN'):

            r = Rect(self.tail[0] * SIZE_OF_CELL, self.tail[1] * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL)

            mainSurface.blit(field, r)

            display.update(r)

            self.next[self.tail[1]][self.tail[0]] = 'NULL'
            self.location[self.tail[1]][self.tail[0]] = 0
            my_field.FIELD[self.tail[1]][self.tail[0]] = 0
            self.tail[1] += 1
            self.tail[1] %= (WIN_HEIGHT // SIZE_OF_CELL)

        elif (self.next[self.tail[1]][self.tail[0]] == 'RIGHT'):

            r = Rect(self.tail[0] * SIZE_OF_CELL, self.tail[1] * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL)

            mainSurface.blit(field, r)

            display.update(r)

            self.next[self.tail[1]][self.tail[0]] = 'NULL'
            self.location[self.tail[1]][self.tail[0]] = 0
            my_field.FIELD[self.tail[1]][self.tail[0]] = 0
            self.tail[0] += 1
            self.tail[0] %= (WIN_WIDTH // SIZE_OF_CELL)

        elif (self.next[self.tail[1]][self.tail[0]] == 'LEFT'):

            r = Rect(self.tail[0] * SIZE_OF_CELL, self.tail[1] * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL)

            mainSurface.blit(field, r)

            display.update(r)

            self.next[self.tail[1]][self.tail[0]] = 'NULL'
            self.location[self.tail[1]][self.tail[0]] = 0
            my_field.FIELD[self.tail[1]][self.tail[0]] = 0
            self.tail[0] -= 1
            self.tail[0] %= (WIN_WIDTH // SIZE_OF_CELL)

    # increase of length on one point

    def increase(self):
        '''
        Increases the length on one point, when snake eat the food
        '''
        self.moveHead()

        self.length += 1

        r = Rect(self.head[0] * SIZE_OF_CELL, self.head[1] * SIZE_OF_CELL, SIZE_OF_CELL, SIZE_OF_CELL)

        mainSurface.blit(self.head_look, r)

        display.update(r)

    def PrintGameOver(self):
        '''
        Prints 'Game over' and score
        '''
        gameOver = text.render('Game over', 1, (0, 0, 5))
        placeOfGameOver = gameOver.get_rect(center=(self.initial[0] * SIZE_OF_CELL, self.initial[1] * SIZE_OF_CELL))
        mainSurface.blit(gameOver, placeOfGameOver)
        score = text.render('Your score: {}'.format(self.length), 1, (0, 0, 5))
        placeOfScore = score.get_rect(center=(self.initial[0] * SIZE_OF_CELL, self.initial[1] * SIZE_OF_CELL + 100))
        mainSurface.blit(score, placeOfScore)
        display.update(placeOfGameOver)
        display.update(placeOfScore)