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
        radius = (cell_side_length / 2) - 7
        drawn_checker = pygame.draw.circle(screen, self.color,
                                           [cell_x + (cell_side_length / 2), cell_y + (cell_side_length / 2)], radius, 0)
        if self.is_queen:
            font = pygame.font.Font('freesansbold.ttf', 30)
            # create a text surface object,
            # on which text is drawn on it.
            text = font.render('Q', True, BLACK, self.color)
            screen.blit(text, drawn_checker)

    def __str__(self):
        return "Checker belonging to player " + str(self.player)
