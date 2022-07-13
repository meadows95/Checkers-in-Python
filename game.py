import random

import pygame

from board import Board

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Game():
    # propertities:
    # player_turn: int (1 or 2)

    def __init__(self, board):
        self.player_turn = random.randrange(1, 3)
        self.board = board

    def show_player_turn(self, screen):

        font = pygame.font.Font('freesansbold.ttf', 30)
        # create a text surface object,
        # on which text is drawn on it.
        text = font.render('Player turn: ' +
                           str(self.player_turn), True, BLACK, WHITE)

        # create a rectangular object for the
        # text surface object
        rect = pygame.Rect(40, 40, 140, 32)

        # set the center of the rectangular object.
        rect.center = (70, 20)
        screen.blit(text, rect)
