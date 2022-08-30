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
        self.winner = None

        if self.player_turn == 1:
            self.make_computer_turn()

    def draw(self, screen, screen_width, screen_height, cell_font):
        self.board.draw(screen, screen_width, screen_height,
                        cell_font, self.selected_cell)
        if self.winner != None:
            self.player_wins_text(screen)
        else:
            self.show_player_turn(screen)

    def move_checker(self, from_cell, to_cell):
        to_cell.occupant = from_cell.occupant
        from_cell.occupant = None

        self.potentially_make_a_queen(to_cell)
        self.potentially_remove_checker(to_cell, from_cell)
        self.check_for_winner()
        self.player_turn = 1 if self.player_turn == 2 else 2

# returns a list of possible to_cells
    def get_possible_destinations_from_cell(self, from_cell):
        if from_cell.occupant == None:
            return []
        possible_destinations = []
        for cell in self.board.cells:
            is_upper_left = cell.x == from_cell.x - 1 and cell.y == from_cell.y + 1
            is_lower_left = cell.x == from_cell.x - 1 and cell.y == from_cell.y - 1
            is_upper_right = cell.x == from_cell.x + 1 and cell.y == from_cell.y + 1
            is_lower_right = cell.x == from_cell.x + 1 and cell.y == from_cell.y - 1

            is_upper_left_2_out = cell.x == from_cell.x - 2 and cell.y == from_cell.y + 2
            is_lower_left_2_out = cell.x == from_cell.x - 2 and cell.y == from_cell.y - 2
            is_upper_right_2_out = cell.x == from_cell.x + 2 and cell.y == from_cell.y + 2
            is_lower_right_2_out = cell.x == from_cell.x + 2 and cell.y == from_cell.y - 2

            is_upper_left_1_out = self.board.find_cell_by_x_and_y_grid_coordinates(
                from_cell.x - 1, from_cell.y + 1)
            is_lower_left_1_out = self.board.find_cell_by_x_and_y_grid_coordinates(
                from_cell.x - 1, from_cell.y - 1)
            is_upper_right_1_out = self.board.find_cell_by_x_and_y_grid_coordinates(
                from_cell.x + 1, from_cell.y + 1)
            is_lower_right_1_out = self.board.find_cell_by_x_and_y_grid_coordinates(
                from_cell.x + 1, from_cell.y - 1)

            if is_upper_left and cell.occupant == None:
                # adding upper left diagonal neighbor
                if from_cell.occupant.is_queen or from_cell.occupant.player == 1:
                    possible_destinations.append(cell)
            elif is_lower_left and cell.occupant == None:
                # adding lower left diagonal neighbor
                if from_cell.occupant.is_queen or from_cell.occupant.player == 2:
                    possible_destinations.append(cell)
            elif is_upper_right and cell.occupant == None:
                # adding upper right diagonal neighbor
                if from_cell.occupant.is_queen or from_cell.occupant.player == 1:
                    possible_destinations.append(cell)
            elif is_lower_right and cell.occupant == None:
                # adding lower right diagonal neighbor
                if from_cell.occupant.is_queen or from_cell.occupant.player == 2:
                    possible_destinations.append(cell)
            elif is_upper_left_2_out and cell.occupant == None and (is_upper_left_1_out.occupant != None and is_upper_left_1_out.occupant.player != self.player_turn):
                # adding upper left diagonal neighbor
                if from_cell.occupant.is_queen or from_cell.occupant.player == 1:
                    possible_destinations.append(cell)
            elif is_lower_left_2_out and cell.occupant == None and (is_lower_left_1_out.occupant != None and is_lower_left_1_out.occupant.player != self.player_turn):
                # adding lower left diagonal neighbor
                if from_cell.occupant.is_queen or from_cell.occupant.player == 2:
                    possible_destinations.append(cell)
            elif is_upper_right_2_out and cell.occupant == None and (is_upper_right_1_out.occupant != None and is_upper_right_1_out.occupant.player != self.player_turn):
                # adding upper right diagonal neighbor
                if from_cell.occupant.is_queen or from_cell.occupant.player == 1:
                    possible_destinations.append(cell)
            elif is_lower_right_2_out and cell.occupant == None and (is_lower_right_1_out.occupant != None and is_lower_right_1_out.occupant.player != self.player_turn):
                # adding lower right diagonal neighbor
                if from_cell.occupant.is_queen or from_cell.occupant.player == 2:
                    possible_destinations.append(cell)
        return possible_destinations

    def make_computer_turn(self):
        for cell in self.board.cells:
            if cell.occupant and cell.occupant.player == 1:
                possible_destinations = self.get_possible_destinations_from_cell(
                    cell)
                if len(possible_destinations) > 0:
                    destination_cell = possible_destinations[0]
                    self.move_checker(cell, destination_cell)
                    return

    def potentially_remove_checker(self, to_cell, from_cell):
        middle_cell_x = (from_cell.x + to_cell.x) / 2
        middle_cell_y = (from_cell.y + to_cell.y) / 2
        middle_cell = self.board.find_cell_by_x_and_y_grid_coordinates(
            middle_cell_x, middle_cell_y)
        if middle_cell == None:
            return

        if middle_cell.occupant.player != self.player_turn:
            middle_cell.occupant = None

    def potentially_make_a_queen(self, to_cell):
        checker = to_cell.occupant
        if self.player_turn == 1 and to_cell.y == self.board.length - 1:
            checker.is_queen = True
        if self.player_turn == 2 and to_cell.y == 0:
            checker.is_queen = True

    def cell_clicked(self, clicked_cell):
        if self.selected_cell == None:
            if clicked_cell.is_playable() and clicked_cell.occupant and clicked_cell.occupant.player == self.player_turn:
                self.selected_cell = clicked_cell
        else:
            if clicked_cell.occupant and clicked_cell.occupant.player == self.player_turn:
                self.selected_cell = clicked_cell
                return

            destinations = self.get_possible_destinations_from_cell(
                self.selected_cell)

            if clicked_cell in destinations:
                self.move_checker(self.selected_cell, clicked_cell)
                self.make_computer_turn()
                self.selected_cell = None

    def check_for_winner(self):
        player_1_count = 0
        player_2_count = 0
        for cell in self.board.cells:
            if cell.occupant == None:
                continue

            if cell.occupant.player == 1:
                player_1_count = player_1_count + 1
            if cell.occupant.player == 2:
                player_2_count = player_2_count + 1
        if player_1_count == 0:
            self.winner = 2
        elif player_2_count == 0:
            self.winner = 2

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

    def player_wins_text(self, screen):
        font = pygame.font.Font('freesansbold.ttf', 30)
        # create a text surface object,
        # on which text is drawn on it.
        text = font.render('Winner: ' +
                           str(self.winner), True, BLACK, WHITE)

        # create a rectangular object for the
        # text surface object
        rect = pygame.Rect(40, 40, 140, 32)

        # set the center of the rectangular object.
        rect.center = (70, 20)
        screen.blit(text, rect)
