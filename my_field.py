from pygame import *
import random
import game

FIELD = []

def update_field():
    '''
    This function fills the field with zero
    '''
    global FIELD
    FIELD = [[0] * (game.WIN_WIDTH // game.SIZE_OF_CELL) for i in range(game.WIN_HEIGHT // game.SIZE_OF_CELL)]