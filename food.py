from pygame import *
import random
from snake import *
import game

class Food:
    def __init__(self):
        '''
        Constructor of class Food
        '''
        # choose random coordinates, that don't lie on snake

        x_coord, y_coord = random.randint(0, game.WIN_WIDTH // game.SIZE_OF_CELL - 1), random.randint(0, game.WIN_HEIGHT // game.SIZE_OF_CELL - 1)

        while (game.FIELD[y_coord][x_coord]):
            x_coord, y_coord = random.randint(0, game.WIN_WIDTH // game.SIZE_OF_CELL - 1), random.randint(0, game.WIN_HEIGHT // game.SIZE_OF_CELL - 1)

        self.x_coord = x_coord
        self.y_coord = y_coord

        # display food

        self.look = Surface((game.SIZE_OF_CELL, game.SIZE_OF_CELL))
        self.look.fill(game.COLOUR_OF_FIELD)
        draw.line(self.look, (50, 200, 20), (0, 0), (game.SIZE_OF_CELL, game.SIZE_OF_CELL), 15)
        draw.line(self.look, (50, 200, 20), (0, game.SIZE_OF_CELL), (game.SIZE_OF_CELL, 0), 15)

        game.mainSurface.blit(self.look, Rect(self.x_coord * game.SIZE_OF_CELL, self.y_coord * game.SIZE_OF_CELL, game.SIZE_OF_CELL, game.SIZE_OF_CELL))

        display.update(Rect(self.x_coord * game.SIZE_OF_CELL, self.y_coord * game.SIZE_OF_CELL, game.SIZE_OF_CELL, game.SIZE_OF_CELL))
