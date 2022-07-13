import pygame
from pygame.locals import *

from cell import Cell

BLACK = (0, 0, 0)
RED = (255, 0, 0)


class Checker():
    # properties:
    # player: int (1 or 2)
    # is_queen: boolean

    def __init__(self, player):
        self.is_queen = False
        self.player = player
        self.color = BLACK if self.player == 1 else RED

    def draw(self, screen, cell_x, cell_y, cell_side_length):
        radius = (cell_side_length / 2) - 3
        pygame.draw.circle(screen, self.color,
                           [cell_x + (cell_side_length / 2), cell_y + (cell_side_length / 2)], radius, 0)
        # pygame.display.update()
