from pygame import *
import random
from snake import *
import game
import my_field

class Food:
    def __init__(self):
        # choose random coordinates, that don't lie on snake

        x, y = random.randint(0, game.WIN_WIDTH // game.SIZE_OF_CELL - 1), random.randint(0, game.WIN_HEIGHT // game.SIZE_OF_CELL - 1)

        while (my_field.FIELD[y][x]):
            x, y = random.randint(0, game.WIN_WIDTH // game.SIZE_OF_CELL - 1), random.randint(0, game.WIN_HEIGHT // game.SIZE_OF_CELL - 1)

        self.x = x
        self.y = y

        # display food

        self.look = Surface((game.SIZE_OF_CELL, game.SIZE_OF_CELL))
        self.look.fill(game.COLOUR_OF_FIELD)
        draw.line(self.look, (50, 200, 20), (0, 0), (game.SIZE_OF_CELL, game.SIZE_OF_CELL), 15)
        draw.line(self.look, (50, 200, 20), (0, game.SIZE_OF_CELL), (game.SIZE_OF_CELL, 0), 15)

        game.mainSurface.blit(self.look, Rect(self.x * game.SIZE_OF_CELL, self.y * game.SIZE_OF_CELL, game.SIZE_OF_CELL, game.SIZE_OF_CELL))

        display.update(Rect(self.x * game.SIZE_OF_CELL, self.y * game.SIZE_OF_CELL, game.SIZE_OF_CELL, game.SIZE_OF_CELL))
