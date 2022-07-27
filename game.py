import random

import pygame

from board import Board

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Game():
    # properties:
    # player_turn: int (1 or 2)
    # board: Board
    # selected_cell: Cell or None

    def __init__(self, board):
        self.player_turn = random.randrange(1, 3)
        self.board = board
        self.selected_cell = None

    def draw(self, screen, screen_width, screen_height, cell_font):
        self.board.draw(screen, screen_width, screen_height,
                        cell_font, self.selected_cell)
        self.show_player_turn(screen)

    def move_checker(self, from_cell, to_cell):
        to_cell.occupant = from_cell.occupant
        from_cell.occupant = None
        self.player_turn = 1 if self.player_turn == 2 else 2

    def validate_move_checker(self, from_cell, to_cell):
        if not from_cell.is_playable() or not to_cell.is_playable():
            return False
        if from_cell == to_cell:
            return False
        if to_cell.occupant != None:
            return False
        return True

    def cell_clicked(self, clicked_cell):
        if self.selected_cell == None:
            if clicked_cell.is_playable() and clicked_cell.occupant and clicked_cell.occupant.player == self.player_turn:
                self.selected_cell = clicked_cell
        else:
            if clicked_cell.occupant and clicked_cell.occupant.player == self.player_turn:
                self.selected_cell = clicked_cell
                return

            if self.validate_move_checker(self.selected_cell, clicked_cell):
                self.move_checker(self.selected_cell, clicked_cell)
                self.selected_cell = None

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
